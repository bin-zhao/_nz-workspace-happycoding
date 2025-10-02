#
# draw_240705.jl
#

using Plots
using QuadGK
using LaTeXStrings

function fn_draw0()
    f(x) = x^2 + 3x + 2

    a = 0
    b = 2
    
    plot_inst0 = plot(f, a, b, label = "f(x) = x^2 + 3x + 2", xlabel = "x", ylabel = "f(x)", title = "Graphical representation of an integral")
    
    # plot!([a, a], [0, f(a)], line = (:gray, 2), label = "")     # Min
    # plot!([b, b], [0, f(b)], line = (:gray, 2), label = "")     # Max
    # plot!([a, b], [0, 0], line = (:black, 1), label = "")       # x-Axis
    
    # plot!([a, b], [f(a), f(b)], line = (:blue, 2), label = "Integral Curve")
    # plot!([a, b], [f(a), f(b)], line = (:blue, 2), label = "")
    
    display(plot_inst0)
end

function fn_draw1()
    f(x) = x^2 + 3x + 2

    a = 0
    b = 2

    result, error = quadgk(x -> x^2 + 3x + 2, a, b)

    println("The integral of f(x) from $a to $b is approximately $result with an error of $error")
end

function fn_draw2()
    n = 100000

    x = rand(n)
    y = rand(n)

    # alpha = 0.01,
    scatter(x, y, alpha = 0.01, color = RGBA(0.0, 1.0, 0.0, 1.0), markerstrokewidth = 0, label = "", xlabel = "x", ylabel = "y", title = "Random Points")

    # for i in 1:5    
    # end

    gui()
end

# function fn_vector_field(X, Y)
#     U = sin.(X) .* cos.(Y)
#     V = cos.(X) .* sin.(Y)

#     return U, V
# end

# function meshgrid(x, y)
#     X = repmat(x, length(y))
#     Y = repmat(y', length(x))

#     return X, Y
# end

# function fn_draw3()
#     x = -10:0.5:10
#     y = -10:0.5:10

#     X, Y = meshgrid(x, y)

#     U, V = fn_vector_field(X, Y)

#     quiver(X, Y, quiver = (U, V), scale = 1, title = "Vector Field")

#     gu()
# end

#TODO(zz) With error.
function fn_draw4()
    # 定义向量场函数
    function vector_field(x, y)
        u = -y
        v = x
        return u, v
    end

    # 定义网格范围和步长
    x_min, x_max, y_min, y_max = -2.0, 2.0, -2.0, 2.0
    step = 0.2

    # 生成网格点
    x = x_min:step:x_max
    y = y_min:step:y_max

    println(typeof(x), typeof(x[0]))

    # 初始化向量场的 U 和 V 分量
    u = zeros(length(x), length(y))
    v = zeros(length(x), length(y))

    println(u)

    # 计算向量场的 U 和 V 分量
    for i in eachindex(x)
        for j in eachindex(y)
            u[i, j], v[i, j] = vector_field(x[i], y[j])
        end
    end

    # 创建向量场图
    quiver(x, y, quiver=(u, v), legend=false, xlabel=L"x", ylabel=L"y", title="Vector Field", aspect_ratio=:equal)

    # 显示图像
    plot!()
end

fn_draw0()
# fn_draw1()
# fn_draw2()
# fn_draw3()
# fn_draw4()

readline()
print("done!")
