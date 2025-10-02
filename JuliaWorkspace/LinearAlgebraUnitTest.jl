#
# LinearAlgebra.jl
#

include("ExceptionHandler.jl")

using .ExceptionHandler
using LinearAlgebra
using Plots


setprecision(96)

bUsePlot = false

function HelloWorld()
    println("############ HelloWorld ############")

    A = [
        1 2 3;
        4 1 6;
        7 8 1
    ]

    I_3 = [
        1 0 0;
        0 1 0;
        0 0 1
    ]

    println("\n## display")
    display(A)
    display(I_3)

    #TODO(zz)
    println("\n## tr")
    println(tr(A))

    println("\n## det")
    println(det(A))
    println(det(I))

    println("\n## inv")
    display(inv(A))
    display(inv(I))

    A = [
        -4.0 -17.0;
        2.0 2.0
    ]

    #TODO(zz)
    println("\n## eigen")
    display(A)
    display(eigvals(A))
    display(eigvecs(A))

    A = [
        1.5 2.0 -4.0;
        3.0 -1.0 -6.0;
        -10.0 2.3 4.0
    ]

    B = [
        1.5 2.0 -4.0;
        2.0 -1.0 -3.0;
        -4.0 -3.0 5.0
    ]

    #TODO(zz)
    println("\n## factorize")
    display(A)
    display(B)
    display(factorize(A))
    display(factorize(B))

    B = [
        1.5 2 -4;
        2 -1 -3;
        -4 -3 5
    ]

    X = [
        1;
        2;
        3
    ]

    #TODO(zz)
    println("\n## symmetric")
    display(B)
    sB = Symmetric(B)
    display(sB)
    display(X)
    display(sB \ X)

    A = [
        1 2 3;
        4 5 6;
        7 8 10;
    ]

    b = [
        6;
        15;
        24
    ]

    b1 = [
        6;
        15;
        25;
    ]

    println("\n## resolve")
    display(det(A))
    try
        display(A \ b)
        display(A * (A \ b))
        display(A \ b1)
        display(A * (A \ b1))
    catch ex
        println(ex.msg)
    end

    B = [
        1.5 2 -4;
        2 -1 -3;
        -4 -3 5
    ]

    b = [
        0;
        0;
        0
    ]

    # https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#Elementary-operations
    # https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#Matrix-factorizations
    println("\n## special matrices")
    try
        display(B)
        display(Symmetric(B))
        display(Hermitian(B))
        display(UpperTriangular(B))
        display(UnitUpperTriangular(B))
        display(LowerTriangular(B))
        display(UnitLowerTriangular(B))
        display(UpperHessenberg(B))
        display(Tridiagonal(B))
        display(SymTridiagonal(B))
        # display(Bidiagonal(B))  # TODO(zz)
        display(Diagonal(B))
        # display(UniformScaling(B))  # TODO(zz)
    catch ex
        PrintException(ex)
    end

    println("\n## uniform scaling")
    U = UniformScaling(2)

    a = [
        1 2;
        3 4
    ]

    b = [
        1 2 3;
        4 5 6
    ]
    
    display(U)
    display(a + U)
    display(a * U)
    display([a U])
    display(b)
    try
        display(b - U)
    catch ex
        PrintException(ex)
    end

    # https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#man-linalg-factorizations
    println("\n## factorizations")
    # TODO(zz) here.
end

function Basic()
    println("############ Basic ############")
    
    A = [
        1.5 2.0 -4.0;
        3.0 -1.0 -6.0;
        -10.0 2.3 4.0
    ]

    B = [
        1.5 2.0 -4.0;
        2.0 -1.0 -3.0;
        -4.0 -3.0 5.0
    ]

    x = [
        1;
        2;
        3
    ]

    b = [
        0;
        1;
        0
    ]

    println("\n## basic")
    display(A)
    display(B)
    display(det(A))
    display(det(B))
    display(A + B)
    display(A - B)
    display(A * 2)
    display(2 * A)
    display(A * B)
    display(B * A)
    display(A * x)
    display(B * x)
    display(A \ b)
    display(B \ b)
    display(inv(A))
    display(inv(B))
end

function MainEntry()
    HelloWorld()
    # Basic()
end

MainEntry()
if bUsePlot
    readline()
end
println("done!")
