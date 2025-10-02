#
# Function1.jl
#

include("../Utils.jl")

using .Utils
using Plots

setprecision(10000)

function Test0()
    function f(x)
        x = BigFloat(x)
        Result = BigFloat(0)

        # 正弦函数级数。
        CurrentUnit = 1
        for i in 1:2:100
            Result += CurrentUnit * x^i / factorial(BigFloat(i))
            CurrentUnit = -CurrentUnit
        end

        return Result
    end
    g(x) = sin(x)
    a = -10
    b = 10

    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")
    plot!(plot_inst0, g, label = "g(x)")

    display(plot_inst0)
    readline()
end

function Test1()
    f(x) = x
    a = -10
    b = 10

    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")

    display(plot_inst0)
    readline()
end

function Test2()
    f(x) = x
    a = -10
    b = 10

    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")

    display(plot_inst0)
    readline()
end

function UnitTest()
    Test0()
    # Test1()
    # Test2()
end

UnitTest()
println("done!")
