fn main() {
    hello();
    demo(true);
    demo(false);
    factorial(10)
}

fn hello() {
    println!("hello world");
}

fn demo(parameter: bool) {
    if parameter {
        println!("One");
    } else {
        println!("Two");
    }
}

fn factorial(n: i32) {
    let mut result = 1;
    for i in 1..n + 1 {
        result = result * i;
    }

    println!("{}", result);
}
