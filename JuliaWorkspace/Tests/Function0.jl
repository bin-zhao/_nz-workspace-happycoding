#
# Function0.jl
#

# I have a dream
    # 有一天，我可以在代码文件里Attach图片。
    # 代码文件可以支持富文本：可以直接嵌入LaTex。
    # 类似于Jupiter。但是更强大，我可以只提取出代码来，也可以作为笔记使用。

# AI来的太快，让人有一种错觉，AI很容易能做到我们现在想要的，比如自动写代码，自动帮代码查错。

include("../Utils.jl")

using .Utils
using Plots

# 目前这个包下载不了，装不了。
    #如果想display多个窗口，需要使用py版本。
# pyplot()

setprecision(10000)

function Test0()
    function f(x)
        Result = BigFloat(0)
        #如果范围为4:63，会产生负值。和精度无关。
            #TODO(zz) 目前还无法解释为什么。
        for i in 4:62
            n = 2^i
            Result += n * x^n / (1 + x^n)
        end

        return Result

        # return (16.0 * x^16 / (1.0 + x^16)
        #     + 32.0 * x^32 / (1.0 + x^32) 
        #     + 64.0 * x^64 / (1.0 + x^64)
        #     + 128.0 * x^128 / (1.0 + x^128)
        #     + 256.0 * x^256 / (1.0 - x^256))
    end
    g(x) = 16.0 * x^16 / (1.0 - x^16)

    a = -10
    b = 10

    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")
    plot!(plot_inst0, g, a, b, label = "g(x)")
    # plot_inst0 = plot(g, a, b, label = "g(x)", xlabel = "x", ylabel = "g(x)", title = "functions")

    display(plot_inst0)
    readline()
end

function Test1()
    function f(x)
        # Julia里有个很致命的问题。我把公式断成两行，就是不同的公式。换到新行的内容会被自动舍弃。
            #养成习惯，用括号。分行和end也行，但是不算好。
        return (x / (1.0 + x) 
            + 2.0 * x^2 / (1.0 - x^2))
    end
    g(x) = x / (1.0 - x)

    # f(x) = x / (1 + x)
    # g(x) = -2x^2 / (1 - x^2) + x / (1 - x)

    # f(x) = x / (1.0 + x) + 2.0 * x^2 / (1.0 - x^2)
    # g(x) = x / (1.0 - x)

    a = -10
    b = 10
 
    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "functions")
    plot!(plot_inst0, g, a, b, label = "g(x)")
    # plot_inst0 = plot(g, a, b, label = "g(x)", xlabel = "x", ylabel = "g(x)", title = "functions")

    display(plot_inst0)
    readline()
end

function Test2()

    a = -10
    b = 10

    # plot_inst0 = plot(label = "", xlabel = "x", ylabel = "f(x)", title = "functions")

    for i in 0:5
        begin
            n = 2^i
            f(x) = 1 / (1 + x^n)
            # plot!(f, a, b, label = "$n")
            plot_inst0 = plot(f, a, b, label = "", xlabel = "x", ylabel = "f(x)", title = "functions")
            display(plot_inst0)
            gui()
        end
    end
 
    # display(plot_inst0)
    readline()
end

function UnitTest()
    # Test0()
    # Test1()
    Test2()
end

UnitTest()
println("done!")
