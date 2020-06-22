function hello()
    print('hello world')
end

function demo(parameter)
    if parameter then
        print('one')
    else
        print('two')
    end
end

function factorial(n)
    local result = 1
    for i = 1, n do
        result = result * i
    end

    print(result)
end

hello()
demo(true)
demo(0)
demo(false)
factorial(10)