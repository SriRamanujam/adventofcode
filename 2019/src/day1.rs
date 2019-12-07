use std::fs::File;
use std::io::{self, prelude::*, BufReader, SeekFrom};

fn main() -> io::Result<()> {
    let path = std::env::args().nth(1).expect("need to pass input file");

    let file = File::open(path)?;
    let mut reader = BufReader::new(file);

    // part 1
    let mut total: u32 = 0;
    for line in reader.by_ref().lines() {
        let thing = line?;
        let thing2: u32 = thing.parse().unwrap();
        total += thing2 / 3 - 2;
    }

    println!("part 1: {}", total);

    // part 2
    reader.seek(SeekFrom::Start(0))?;

    let mut total2: i32 = 0;
    for line in reader.by_ref().lines() {
        let mut inner_total: i32 = 0;
        let thing = line?;
        let mut module_mass: i32 = thing.parse().unwrap();
        loop {
            let fuel: i32 = module_mass / 3 - 2;
            if fuel > 0 {
                inner_total += fuel;
                module_mass = fuel;
            } else {
                break
            }
        }
        total2 += inner_total;
    }

    println!("part 2: {}", total2);

    Ok(())
}