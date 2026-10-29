# Installs (or re-verifies) the team-ops plugin on Muse.
#
# `muse plugins install` exits 1 when the only issues are unsupported-field
# warnings, even though the plugin lands enabled and active. Scripts must not
# read that exit code as failure, so this wrapper judges by observed plugin
# state instead: enabled + active + zero error-severity diagnostics.
# Exit 0 means installed and active; exit 1 means it really failed.
param(
    [string]$Path = (Join-Path (Split-Path -Parent (Split-Path -Parent $PSCommandPath)) "plugins/team-ops"),
    [string]$Scope = "project",
    [string]$Id = "team-ops"
)

$ErrorActionPreference = "Continue"
& muse plugins install --scope $Scope $Path 2>&1 | ForEach-Object { "$_" } | Out-Null
& muse plugins update $Id 2>&1 | ForEach-Object { "$_" } | Out-Null
$wantVersion = (Get-Content (Join-Path $Path ".claude-plugin/plugin.json") | ConvertFrom-Json).version

$list = & muse plugins list --json 2>$null | Out-String | ConvertFrom-Json
$entry = $list.plugins | Where-Object { $_.record.id -eq $Id } | Select-Object -First 1
if (-not $entry) {
    Write-Error "Plugin '$Id' not found after install."
    exit 1
}

$errors = @($entry.diagnostics | Where-Object { $_.severity -eq "error" })
$warnings = @($entry.diagnostics | Where-Object { $_.severity -ne "error" }).Count
if ($entry.record.enabled -and $entry.active -and $errors.Count -eq 0 -and $entry.record.version -eq $wantVersion) {
    Write-Output "OK: '$Id' $($entry.record.version) enabled=$($entry.record.enabled) active=$($entry.active) warnings=$warnings errors=0."
    exit 0
}

Write-Error ("FAIL: want={0} got={1} enabled={2} active={3} errors={4}." -f $wantVersion, $entry.record.version, $entry.record.enabled, $entry.active, $errors.Count)
$errors | Select-Object -First 5 | ForEach-Object { Write-Error $_.message }
exit 1
