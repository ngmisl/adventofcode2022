use std::fs::File;
use std::io::Result;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn main() {
    let raw_data = get_lines_from_file(get_input_file_name());
    dbg!(raw_data);
}

fn get_lines_from_file(filename: impl AsRef<Path>) -> Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn get_input_file_name() -> &'static str {
    "src/input1.txt"
}
