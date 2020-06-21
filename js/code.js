function hello() {
    console.log("hello world");
}

function demo(parameter) {
    if (parameter) {
        console.log("One");
    } else {
        console.log("Two");
    }
}

function factorial(n) {
    var result = 1;
    for (; n > 0; n--) {
        result = result * n;
    }

    console.log(result);
}

hello()
demo(true)
demo(false)
factorial(10)