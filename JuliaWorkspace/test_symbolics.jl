#
# test_symbolics.jl
#

# using SymPy
using Symbolics
using LinearAlgebra
using Latexify

function Test2x2()
    @variables m11, m12, m21, m22

    A = [
        m11 m12;
        m21 m22
    ]

    det_A = det(A)

    A_T = A'

    println("Matrix A: ", A)
    println("Determinant of A: ", det_A)
    println("Transpose of A: ", A_T)

    display(A)
    display(det_A)
    display(A_T)

    F = lu(A)
    display(F.L)
    display(F.U)
    display(F.p)

    display(A \ zeros(size(A)[2]))
    display(inv(A))
    display(A[:, 1])

    @variables b1, b2
    b = [
        b1;
        b2
    ]
    display(A \ b)
    display(A * inv(A))

    println(latexify(A \ b))

end

function Test3x3()
    # Base.@var m11
    # Base.@var m12

    @variables m11, m12, m13, m21, m22, m23, m31, m32, m33

    # A = SymMatrix([m11, m12], [m21, m22])
    A = [
        m11 m12 m13;
        m21 m22 m23;
        m31 m32 m33
    ]

    det_A = det(A)

    A_T = A'

    println("Matrix A: ", A)
    println("Determinant of A: ", det_A)
    println("Transpose of A: ", A_T)

    display(A)
    display(det_A)
    display(A_T)

    F = lu(A)
    display(F.L)
    display(F.U)
    display(F.p)

    display(A \ zeros(size(A)[2]))
    display(inv(A))
    display(A[:, 1])

    @variables b1, b2, b3
    b = [
        b1;
        b2;
        b3
    ]
    display(A \ b)

    println(latexify(A \ b))

    # TODO(zz) Rank Factorization, QR Factorization, Singular Value Decomposition, Spectral Factorization
end

function Example0()
    @variables R1, R2

    A1 = [
        1 -R1;
        0 1
    ]
    A2 = [
        1 0;
        -1/R2 1
    ]

    display(A2 * A1)

    A = [
        1 -8;
        -0.5 5
    ]

    F = lu(A)
    display(F.L)
    display(F.U)

    println(latexify(F.L))

    @variables x, y
    @variables A[1:2, 1:2]

    # TODO(zz) 没找到solve矩阵方程的方法。但是可以列方程组。

    A = [
        x   (x*y);
        (x+y)   y
    ]
    B = [
        1 2;
        3 4
    ]
    println(size(A))
    println(size(B))
    # eq = inv(A) * B
    # eq = A .~ B
    # solution = Symbolics.solve_for(eq, X)
    # println(solution)
    # println(eq)
    # solution = Symbolics.solve_for(eq, [x, y])

    eq1 = x ~ 1
    eq2 = (x * y) ~ 2
    eq3 = (x + y) ~ 3
    eq4 = y ~ 4
    eqs = [eq1, eq2, eq3, eq4]
    solution = solve_system_eq(eqs, [x, y])
    println(solution)

    # 很诱人，但不够成熟。
    if false
        A = [
            1 -R1;
            -1/R2 1+R1/R2
        ]
        B = [
            1 -8;
            -0.5 5
        ]
        eq = A .~ B
        # println(eq)
        println(latexify(eq))
        # eq1 = build_function(eq, [A, B])
        # display(eq1)
        # println(latexify(eq1))

        # solution = Symbolics.solve_for(eq, [R1, R2])
        # println(solution)
        eq1 = -R1 ~ -8
        eq2 = (-1/R2) ~ -0.5
        eq3 = (1+R1/R2) ~ 5
        equations = [eq1, eq2, eq3]
        solution = solve_system_eq(equations, [R1, R2])
        println(solution)
    end
end

function main()
    # Test2x2()
    # Test3x3()

    Example0()
end

main()
println("done!")
