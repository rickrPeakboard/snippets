fn hello() {
    println!("hello world");
}

fn demo(bool parameter) {
    if parameter {
        println!("One");
    } else {
        println!("Two");
    }
}

fn factorial(i32 n) {
    let mut result = 1;
    for i in 1..n {
        result = result * i;
    }

    println!("{}", result);
}