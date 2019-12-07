use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn do_the_thing(mut program: Vec<u32>, noun: u32, verb: u32) -> Option<u32> {
    program[1] = noun;
    program[2] = verb;

    let mut ip = 0;
    loop {
        let opcode_option = program.get(ip);

        if let Some(opcode) = opcode_option {
            match opcode {
                99 => {
                    //println!("Halt!");
                    break
                }
                1 => {
                    //println!("Addition!");
                    let op1_pos = *program.get(ip+1).unwrap();
                    let op2_pos = *program.get(ip+2).unwrap();
                    let op1 = program.get(op1_pos as usize).unwrap();
                    let op2 = program.get(op2_pos as usize).unwrap();
                    let dst = *program.get(ip+3).unwrap();

                    //println!("Adding {}:{} + {}:{}", op1_pos, op1, op2_pos, op2);

                    let new = op1 + op2;
                    //println!("Inserting new value {} into dst {}", new, dst);
                    program[dst as usize] = new;
                },
                2 => {
                    //println!("Multilpication!");
                    let op1_pos = *program.get(ip+1).unwrap();
                    let op2_pos = *program.get(ip+2).unwrap();
                    let op1 = program.get(op1_pos as usize).unwrap();
                    let op2 = program.get(op2_pos as usize).unwrap();
                    let dst = *program.get(ip+3).unwrap();

                    //println!("Multiplying {}:{} * {}:{}", op1_pos, op1, op2_pos, op2);
                    let new = op1 * op2;
                    //println!("Inserting new value {} into dst {}", new, dst);
                    program[dst as usize] = new;
                },
                _ => {
                    println!("Unknown instruction {}!", opcode);
                    break
                }
            }
            ip += 4;
        }
    } 
    //println!("Program halted at ip {}, position 0 is {}", ip, *program.get(0).unwrap());
    Some(*program.get(0).unwrap())
}

fn main() -> io::Result<()> {
    let path = std::env::args().nth(1).expect("need to pass input file");

    let file = File::open(path)?;
    let mut reader = BufReader::new(file);

    // setup
    let mut input = String::new();
    reader.read_line(&mut input)?;
    let program: Vec<u32> = input
        .split(',')
        .filter_map(|s| s.parse().ok())
        .collect();

    println!("Parsed input into program {} elements long", program.len());

    // part 1
    let out = do_the_thing(program.clone(), 12, 2);
    println!("Part 1: {}", out.unwrap());

    // part 2
    'outer: for noun in 0..99 {
        for verb in 0..99 {
            match do_the_thing(program.clone(), noun, verb) {
                Some(19690720) => {
                    println!("Part 2: 100 * {} + {} = {}", noun, verb, 100 * noun + verb);
                    break 'outer
                },
                Some(_) => {},
                None => {}
            }
        }
    }

    Ok(())
}