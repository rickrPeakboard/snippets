fn main() {
    println!("starting...");
    const N: usize = 10000000;
    println!("n is {0}", N);
    let mut arr = vec![0; N];
    for i in 0..arr.len() - 1 {
        arr[i] += 1;
    }

    println!("done");
}
