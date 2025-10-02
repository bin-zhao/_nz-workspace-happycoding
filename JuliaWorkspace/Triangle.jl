#
# Triangle.jl
#

using Test

setprecision(96)

function UnitTest()
    println(sin(0))
    println(sin(pi / 2))
    println(cos(0))
    println(BigFloat(cos(pi / 2)))

    @test cos(pi / 2) < 0.0000001
end

UnitTest()
println("done!")
