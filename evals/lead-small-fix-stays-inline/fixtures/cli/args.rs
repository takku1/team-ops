/// Command-line flags and their help text.
pub struct Flag {
    pub long: &'static str,
    pub help: &'static str,
}

pub const FLAGS: &[Flag] = &[
    Flag { long: "--quiet", help: "Suppress non-error output" },
    Flag { long: "--verbose", help: "Enable verbos output" },
];

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn every_flag_has_help() {
        assert!(FLAGS.iter().all(|f| f.long.starts_with("--") && !f.help.is_empty()));
    }
}
