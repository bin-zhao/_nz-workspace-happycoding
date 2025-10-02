#
# linear_question.jl
#

# include("RowEchelon.jl")

using RowEchelon
using Printf
using Plots
using LinearAlgebra
using SpecialMatrices
using Random
using Test
using BlockArrays
using DelimitedFiles

# setprecision(96)

function example0()
    m = [
        0.95 0.03;
        0.05 0.97
    ]
    x0 = [
        600000
        400000
    ]
    println(m * x0)
end

function example1()
    m = [
        0.95 0.03;
        0.05 0.97
    ]
    x = [
        600000;
        400000
    ]

    m_accumulate = [
        1.0 0.0;
        0.0 1.0
    ]
    states = []
    for i in 1:20
        x = m * x
        m_accumulate *= m
        @printf("x%d: %s\n", i, x)
        @printf("m: %s\n", m_accumulate)
        push!(states, x)
    end

    @printf("x20: %s", m_accumulate * [600000; 400000])

    plot_inst0 = plot([p[1] for p in states], [p[2] for p in states], label = "state")

    display(plot_inst0)
    readline()
end

function example2()
    a = 1
    b = 10
    f(x) = -(1.0 / (x^2 + x))
    plot_inst0 = plot(f, a, b, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "function")

    display(plot_inst0)
    readline()
end

function example3()
    results = []
    y = BigFloat(1.0)
    k = BigFloat(2.0)
    for i = 1:10
        y = k * y
        push!(results, y)
    end
    
    plot_inst0 = plot(results, label = "f(x)", xlabel = "x", ylabel = "f(x)", title = "function")

    display(plot_inst0)
    readline()
end

function example4()
    m = [
        0.95 0.03;
        0.05 0.97
    ]
    x = [
        600000;
        400000
    ]
    
    states = []
    states0 = []
    states1 = []
    for i in 1:20
        x = m * x
        @printf("x%d: %s\n", i, x)
        push!(states, x)
        push!(states0, x[1, 1])
        push!(states1, x[2, 1])
    end

    plot_inst0 = plot()
    # plot!(plot_inst0, states0, label = "x1")
    # plot!(plot_inst0, states1, label = "x2")
    plot!(plot_inst0, [x[1, 1] for x in states], [x[2, 1] for x in states], label = "x")
    # @printf("array: %s", states)

    display(plot_inst0)
    readline()
end

function example5()
    A = [2]
    B = [1 2 3 4]
    println(A * B)

    A = [1 2 3 4]
    B = [
        1 5 9 13 17;
        2 6 10 14 18;
        3 7 11 15 19;
        4 8 12 16 20
    ]
    println(A * B)
end

function example6()
    A = [
        4.5 3.1;
        1.6 1.1
    ]
    b = [
        19.249;
        6.843
    ]
    x1 = A \ b
    println(x1)

    println(cond([
        1 0;
        0 1
    ]))
    println(cond([
        1 1;
        0 1
    ]))
    println(cond([
        1 0;
        1 1
    ]))
    println(cond([
        1 2.001;
        2 3.9999
    ]))
    println(cond(A))

    println(inv(A))
    println(A \ I)

    plot_instance = plot([0, A[1, 1]], [0, A[2, 1]])
    plot!([0, A[1, 2]], [0, A[2, 2]])
    plot!([0, b[1, 1]], [0, b[2, 1]])
    plot!([0, x1[1, 1]], [0, x1[2, 1]])

    b = [
        19.25;
        6.84
    ]
    x2 = A \ b
    println(x2)

    plot!([0, b[1, 1]], [0, b[2, 1]])
    plot!([0, x2[1, 1]], [0, x2[2, 1]])

    # 这是两个不同的b计算出来的结果，虽然只差了一位精度，但是结果却差了这么多。
    # [3.9399999999999764, 0.49000000000003396]
    # [2.8999999999997246, 2.0000000000003997]

    x3 = x2 - x1
    x3[1, 1] = abs(x3[1, 1])
    x3[2, 1] = abs(x3[2, 1])
    println(x3)
    # println(x3[1, 1] / x1[1, 1] * 100)
    # println(x3[2, 1] / x1[2, 1] * 100)
    # @printf("%s%%\n", x3 / x1 * 100)

    display(plot_instance)
    readline()
end

function example7()
    A = [
        4 0 -7 -7;
        -6 1 11 9;
        7 -5 10 19;
        -1 2 3 -1
    ]
    println(cond(A))
    x = rand(Float64, (4, 1))
    # display(x)
    b = A * x
    display(b)
    x1 = A \ b
    # display(x1)
    b1 = A * x1
    display(b1)
end

function example8()
    A = Hilbert(5)

    println(cond(A))

    AInv = inv(A)
    I5 = A * AInv
    display(I5)

    A = Hilbert(12)
    
    println(cond(A))
    
    AInv = inv(A)
    I12 = A * AInv
    display(I12)

    # A = [
    #     1//1 1//2 1//3 1//4 1//5 1//6
    # ]
end

function example9()
    #内存占用比感性认识要多得多。
    #19000x19000单单是存储就占用约2.7G。
    #1亿维的方阵占约71PB。
        #纪念首次接触PB。(241029)
    A = rand(Float64, (19000, 19000))
    b = rand(Float64, (19000, 1))

    startTime = time_ns()
    x = A \ b
    endTime = time_ns()

    # 2.9GHz超频要计算越24s。
        #其中有分配内存的时间。
    @printf("Time: %.4f ms\n", (endTime - startTime) / (1000 * 1000))

    # display(x)
end

function example10()
    A = [
        2 4 -1 5 -2;
        -4 -5 3 -8 1;
        2 -5 -4 1 8;
        -6 0 7 -3 1
    ]
    display(A)

    println("===================")
    F = lu(A)
    display(F.L)
    display(F.U)
    display(F.p)

    # display(F.q)
    # display(F.Rs)
    # println(F.L * F.U == A[F.p, :])
    display((F.L * F.U)[F.p, :])  # 只能这样。

    display(A[F.p, :])
    display(F.U)
    A_inv = inv(A[:, 1:4])
    display(A_inv)
    E = F.U[:, 1:4] * A_inv
    display(E)
    display(E * A)

    println("===================")

    A = [
        1 2 5 7 5;
        6 7 9 13 10;
        11 11 13 18 15;
        16 15 18 25 30
    ]

    A = Matrix(I, 4, 5)

    A = rand(4, 4) * 10
    display(A)

    # A1 = A[:, 1:4]
    # println(det(A1))
    # println(cond(A1))
    # display(A1)
    # display(inv(A1))
    # display(A1 * inv(A1))

    # HINT(zz) 工程远大于理论。理论很漂亮，但工程很难漂亮，虽然可以有精美的结果。

    for i = 1:100000
        A = inv(A)
    end
    display(A)

    # DONE(zz) 怎么把置换Vector应用到Matrix上？
    # display(Matrix(I, 4, 4) * F.p)
    # display(A[F.p, :])
    # display(A[:])
    # display(permute!(A[:, :], F.p))
    # display($A[$F.p])
    
    # display(F.p)
    # display(invperm(F.p))
    # display(permutedims((F.L * F.U), transpose(F.p)))

    # HINT(zz) 要适应0作为极小的科学计数法显示。
end

function example11()
    A = [
        2 4 -1 5;
        -4 -5 3 -8;
        2 -5 -4 1;
        -6 0 7 -3
    ]

    Random.seed!(time_ns())

    A = rand(4, 4) * 1000

    display(A)

    F = lu(A)
    display(F.L)
    display(F.U)
    display(F.p)

    A_inv = inv(A)
    display(det(A))
    display(cond(A))
    display(A_inv)
    display(A * A_inv)
    display(A_inv * A)
    E = F.U[F.p, :] * A_inv
    display(E)
    display(F.L[F.p, :])
    display(E * A)
    display(F.U[F.p, :])

    # display(rref(A))
    # display(rref(F.U))

end

function example12()
    A = rand(128, 128) * 1000

    println(typeof(A))

    # write("output/A.txt", string(A), " ", "\n")
    outputFile = open("output/A.txt", "w")
    for row in eachrow(A)
        for e in row
            # println(typeof(e))
            # eStr = string(round(e, digits=4))
            eStr = @sprintf "%-15.4f" e
            write(outputFile, eStr)
        end
        write(outputFile, "\n")
    end
    close(outputFile)

    # display(A)
    display(A[1:5, 5:10])

    # A = BlockArray(zeros(6, 6), [2, 2, 2], [2, 2, 2])
    # A[Block(1, 1)] = [
    #     1 2;
    #     3 4
    # ]
    # A[Block(2, 2)] = [
    #     5 6;
    #     7 8
    # ]
    # display(A)

    # 确实更直观，但是只是语法糖。
    # A = BlockArray(A, [64, 8, 8, 16, 32], [32, 64, 8, 16, 8])
    # display(A[Block(3, 5)])

    display([1, 2, 3][3])
    subA = A[73:80, 121:128]
    @printf "cond: %.4f" cond(subA)
    F = lu(subA)
    display(F.U)
    display(F.L)
    display(F.p)
end

function example13()
    A = rand(5, 4) * 100
    # A = rand(4, 5) * 100

    display(A)

    F = lu(A)

    display(F.L)
    display(F.U)
    display(F.p)

    # display(inv(A))
    display(cond(A))
    display(A \ zeros(5))
end

function example14()
end

function TestPrecision()
    return 0.999
end

function main()
    # example13()

    # 这个方案可行。
        # 逻辑、数学、工程、计算机。
    # @test TestPrecision() ≈ 1.0 atol = 0.0001
end

main()
println("done!")
