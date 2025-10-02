#
# TestSymPy.jl
#

# 虽然Julia语法不够友好，但是，不得不说，它对于计算描述来说比Python要好多了。
# Python语法简单，但是，在表示计算和数学符号方面简直差太多了。

# https://docs.juliahub.com/CalculusWithJulia/AZHbv/0.0.5/precalc/polynomial.html

# using SymEngine   #目前和SymPy还有很多冲突。(240909)
using SymPy
using Plots

function UnitTest()
    a, b, c = symbols("a, b, c")
    # @vars a, b, c
    x = symbols("x", real = true)
    # @vars x
    p = -16x^2 + 100
    quad = a*x^2 + b*x + c
    triangle_func = sin(a*(x - b*pi) + c)
    fn0 = quad + quad^2 - quad^3

    p = -16x^2 + 100
    p(x => (x-1)^2)

    y = p(x=>2)

    # @vars a b c E F
    a, b, c, E, F = symbols("a, b, c, E, F")
    p = a*x^2 + b*x + c
    println(p(x => x-E) + F)
    println(expand(p(x => x-E) + F))

    p = -16x^2 + 100
    y = p(2)


    to_show = p
    to_plot = plot(x^5 - x + 1, -3/2, 3/2)
    to_plot = plot(p, -10, 10)

    println(expand((x-1)*(x-2)*(x-3)))

    n = symbols("n")
    println("me?")
    println(expand((n(n + 1)(2n + 1)) / 6))   #expand目前还没能力展开这个。wolfram能，但是，都不能识别这是1^2 + 2^2 + ... + n^2。

    print(to_show)
    print(repr(to_show))
    show(to_show)
    show(repr(to_show))
    
    
    plot_inst = plot(to_plot)
    display(plot_inst)
    readline()
end

UnitTest()
println("done!")
