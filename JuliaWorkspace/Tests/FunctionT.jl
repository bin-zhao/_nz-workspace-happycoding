#
# FunctionT.jl
#

include("../Utils.jl")

using .Utils
using Plots

setprecision(10000)

function Test0()
    f(x) = x
    a = -10
    b = 10

    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")

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
