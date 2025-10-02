#
# Fibonacci.jl
#

include("Utils.jl")

using .Utils
using Printf
using Plots
# using PyPlot

setprecision(1024)

#周期不过100，因为两位数最多是100种情况，即使没有从前两位开始周期，也会是以其他两位开始的周期。
    #也就是，到这里是不能确定数列会从前两位开始新周期的。
    #也不能假设周期有规律。因为知道结果了，所以可能先入为主，但是面对一个新的数列不能有这种想法。

#这个数列的核心是前两个数字。或者说，后一项依赖前一项的数列重点都是前面的依赖项。
    #初始+规则=规律

#1,1周期为什么是60？
#最大、最小周期。
#周期是否有100种。

function fibonacci_iterative(n)
    a, b = BigInt(1), BigInt(1)
    for _ in 1:n
        a, b = b, a + b
    end

    return a, b
end

function Test0()
    # prev = 1
    # cur = 1
    # for i in 1:100000
    #     prev = cur
    #     cur = fibonacci_iterative(i)
    # end

    prev, cur = fibonacci_iterative(1000)

    println(prev)
    println(cur)

    #第1001个能产生308位相同的小数位。
    println(BigFloat(prev) / BigFloat(cur))
    println(BigFloat(1.0 + sqrt(BigFloat(5))) / 2.0)
end

function Test1()
    n = 3600
    a, b = BigInt(0), BigInt(1)

    result_str = ""
    result_str1 = ""
    result_str2 = ""

    for i in 1:n
        a, b = b, a + b
        result_str *= @sprintf("%d", a % 10)
        result_str1 *= @sprintf("%02d ", a % 100)
        result_str2 *= @sprintf("%d ", a % 10)
        # if i % 100 == 0
        #     result_str *= "\n"
        # end
    end

    open("output/Fibonacci.txt", "w") do file
        write(file, result_str)
    end
    open("output/Fibonacci1.txt", "w") do file
        write(file, result_str1)
    end
    open("output/Fibonacci2.txt", "w") do file
        write(file, result_str2)
    end
end

function Test2()
    n = 60
    a, b = BigInt(1), BigInt(1)
    result = BigInt[]
    result1 = BigInt[]
    for i in 1:n
        push!(result, a % 10)
        push!(result1, a)
        a, b = b, a + b
    end

    WriteOutList(result, "Fibonacci.txt")
    WriteOutList(result1, "Fibonacci1.txt", " ")

    if true
        plot_output = plot(result)
        display(plot_output)

        readline()
    end

    if false
        figure(1)
        plot_output = plot(result)
        figure(2)
        plot_output1 = plot(result1)
        display(plot_output)
        display(plot_output1)

        readline()
    end
end

#可以依赖任意数量的前置元素。
    #依赖一个很有意思。
    #依赖多个类似记忆。
    #和马尔科夫神似。
function GenerateList(result, a1, a2, fn, n)
    a, b = a1, a2

    for i in 1:n
        push!(result, a)
        a, b = b, fn(a, b)
    end
end

function Test3()
    n = 100

    if false
        result = BigInt[]
        fibonacci(a::BigInt, b::BigInt) = a + b
        GenerateList(result, BigInt(1), BigInt(1), fibonacci, n)
        println(result)
    end

    if false
        result = BigInt[]
        fn0(a::BigInt, b::BigInt) = a - b
        GenerateList(result, BigInt(1), BigInt(1), fn0, n)
        println(result)
    end

    if false
        result = BigInt[]
        fn1(a::BigInt, b::BigInt) = 2 * a + b
        GenerateList(result, BigInt(1), BigInt(1), fn1, n)
        println(result)
    end

    if true
        result = BigFloat[]
        fn2(a::BigFloat, b::BigFloat) = a^-1 + b
        GenerateList(result, BigFloat(1), BigFloat(2), fn2, n)
        println(result)
    end

    if false
        result = BigFloat[]
        fn3(a::BigFloat, b::BigFloat) = sin(a) + sin(b)
        GenerateList(result, BigFloat(1), BigFloat(1), fn3, n)
        println(result)
    end

    if true
        plot_output = plot(result)
        display(plot_output)

        readline()
    end
end

# Test0()
# Test1()
Test2()
# Test3()
println("done!")
