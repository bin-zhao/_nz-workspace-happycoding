#
# DrawSimpleFunctions.jl
#

include("Utils.jl")

using .Utils
using Plots

setprecision(10000)

function Fn0(x, a, b, n)
    y = 0

    for i = 1:n
        y += b^i * cos(a^i * x)
    end

    return y
end

function UnitTest()
    # f(x) = (x^2 - 3x + 2) / (x - 2)
    # f(x) = x^5 + x^4 - x^3 + x^2 - x^1 + x^0 - x^-1
    # f(x) = sin(x)^4 + sin(x)^3 + sin(x)^2 + sin(x)^1 + sin(x)^0
    # f(x) = sin(x^3)
    # f(x) = sin(sin(x^2))
    # f(x) = 2^x
    # f(x) = 2x^2 - x - 6
    # f(x) = x^(1.0/2.0)
    # f(x) = sqrt(x)
    # f(x) = Fn0(x, 1.1, 1, 100)
    # f(x) = Fn0(x, 0.6, 1, 100)
    # f(x) = 1 / x
    # f1(x) = x * sin(1 / x)
    # f2(x) = x
    # f3(x) = -x
    # g(x) = -1
    # f(x) = x / (1 - x)
    
    function f(x)
        Result = BigFloat(0)
        #如果范围为4:63，会产生负值。和精度无关。
        for i in 4:62
            n = 2^i
            Result += n * x^n / (1 + x^n)
        end

        return Result

        # return 16 * x^16 / (1 + x^16)
        #     + 32 * x^32 / (1 + x^32) 
        #     + 64 * x^64 / (1 + x^64)
        #     + 128 * x^128 / (1 + x^128)
        #     + 256 * x^256 / (1 + x^256)
        #     + 512 * x^512 / (1 + x^512)
        #     + 1024 * x^1024 / (1 + x^1024)
        #     + 512 * x^512 / (1 + x^512)
        #     + 512 * x^512 / (1 + x^512)
        #     + 512 * x^512 / (1 + x^512)
        #     + 512 * x^512 / (1 + x^512)
        #     + 512 * x^512 / (1 + x^512)
        #     + 512 * x^512 / (1 + x^512)
    end
    g(x) = 16 * x^16 / (1 - x^16)

    a = -10
    b = 10
    
    # plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")
    # plot_inst0 = plot(f1, a, b, label = "", xlabel = "x", ylabel = "f(x)", title = "f(x)")
    # plot!(plot_inst0, f2, a, b)
    # plot!(plot_inst0, f3, a, b)
    # plot!([-1, 10], line = (:gray, 2), label = "")    # TODO(zz)
    # plot!(plot_inst0, g, a, b, label = "g(x)")
    plot_inst0 = plot(g, a, b, label = "g(x)", xlabel = "x", ylabel = "g(x)", title = "functions")

    display(plot_inst0)
    readline()
end

UnitTest()
println("done!")
