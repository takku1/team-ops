# Install both current plugins for an explicitly selected project.
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory = $true)][string]$Workspace,
    [switch]$CoreOnly
)

$ErrorActionPreference = 'Stop'
$suiteRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$projectRoot = (Resolve-Path -LiteralPath $Workspace).Path
if (-not (Test-Path -LiteralPath $projectRoot -PathType Container)) { throw 'Workspace must be a directory.' }
$pluginNames = @('team-ops')
if (-not $CoreOnly) { $pluginNames += 'team-ops-delivery' }
$oldUpdateSetting = $env:MUSE_NO_AUTO_UPDATE
Push-Location -LiteralPath $projectRoot
try {
    # Installing plugins must not also update the Muse application.
    if (-not $WhatIfPreference) { $env:MUSE_NO_AUTO_UPDATE = '1' }
    foreach ($pluginName in $pluginNames) {
        $sourcePath = Join-Path $suiteRoot "plugins\$pluginName"
        $manifest = Get-Content -Raw -LiteralPath (Join-Path $sourcePath '.claude-plugin\plugin.json') | ConvertFrom-Json
        if (-not $PSCmdlet.ShouldProcess($projectRoot, "Install $pluginName $($manifest.version) from $sourcePath")) { continue }
        # Earlier Muse versions returned misleading exit codes. Verify observed state.
        $ErrorActionPreference = 'Continue'
        $installOutput = & muse plugins install $sourcePath --scope project --json 2>&1 | Out-String
        $listOutput = & muse plugins list --json 2>$null | Out-String
        $ErrorActionPreference = 'Stop'
        try { $installed = $listOutput | ConvertFrom-Json }
        catch { throw "Cannot inspect Muse plugin state after install. $installOutput" }
        $entry = $installed.plugins | Where-Object { $_.record.id -eq $pluginName } | Select-Object -First 1
        $errors = @($entry.diagnostics | Where-Object { $_.severity -eq 'error' })
        $expectedSkills = @(Get-ChildItem -LiteralPath (Join-Path $sourcePath 'skills') -Directory).Count
        $actualSkills = @($entry.plugin.capabilities.skills).Count
        if (-not $entry -or -not $entry.active -or -not $entry.record.enabled -or
            $entry.record.version -ne $manifest.version -or $errors.Count -gt 0 -or
            $actualSkills -ne $expectedSkills) {
            throw "Installation not verified for $pluginName $($manifest.version). $installOutput"
        }
        $requiredResources = @('references\research-evidence.md', 'references\host-compatibility.md')
        if ($pluginName -eq 'team-ops') {
            $requiredResources += @('skills\team-lead\references\coordination.md', 'skills\team-lead\scripts\check_runner.py')
        }
        foreach ($relative in $requiredResources) {
            $cachedFile = Join-Path $entry.record.cache_path $relative
            if (-not (Test-Path -LiteralPath $cachedFile)) { throw "Installed package is missing $relative" }
            if ((Get-FileHash -LiteralPath $cachedFile).Hash -ne
                (Get-FileHash -LiteralPath (Join-Path $sourcePath $relative)).Hash) {
                throw "Installed resource differs from source: $relative"
            }
        }
        Write-Output "OK: $pluginName $($entry.record.version), active, $actualSkills skills, zero errors."
    }
    if (-not $WhatIfPreference) { Write-Output 'Start a fresh Muse session in the project to load the updated skills.' }
}
finally {
    Pop-Location
    if (-not $WhatIfPreference) {
        [Environment]::SetEnvironmentVariable('MUSE_NO_AUTO_UPDATE', $oldUpdateSetting, 'Process')
    }
}
