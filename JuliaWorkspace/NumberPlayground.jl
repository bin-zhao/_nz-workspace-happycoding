#
# NumberPlayground.jl
#

include("Utils.jl")

using .Utils
# using DifferentialEquations
using Primes
using Printf

setprecision(2000)

function main()
    # x = BigFloat(100000000000000000000)   # 20
    x = BigFloat(1000000)
    y = x / (x - 3)
    # println(y)

    # println(sqrt(BigFloat(2)))
    # println(3^7)
    # println(2187^(1/7.0))
    # println(1/BigFloat(7))

    f0 = function (x)
        return 1/BigFloat(x)
    end
    f1(x) = 1/BigFloat(x)
    # println(sum(f0, (1,1000)))
    # println(sum(map(f1, 1:10000000000)))

    #21.30048150234794401668510184890834696612707273359888038310175008962476724562403540575933460750325408971499662630659877139709744856811392152833864288067588054528617172358110923419278286440781855539621524270597351888387956619568427517288078473536934102890096194671362259252812948254211847884592419717088264327201506883966947978568442835837197717266565537583692727586116694808179211144742128653975054932550200679387093141304859377853368650144673622972554661001037665285827167632226455931529433767976195705731202966221836763265283223717591060483182446999434628700785939282179094742368559601922130594195360658
    #21.30026583694641
    result = 0
    # for i in 1:1000000000  # 9
    #     result += 1 / BigFloat(i)
    # end
    result = log(1000000000) + 0.577
    # println(result)

    temp = BigFloat(0)

    # for i in 1000000:-1:3
    #     temp = 1 / (i + temp)
    # end
    
    # for i in 1:100000
    #     sign = 1
    #     if i % 2 == 0
    #         sign = -1
    #     end
    #     temp += sign * 1 / i
    # end

    # temp = integral

    # println(temp)

    if false
        primes = Set()
        for i in 1:100000
            factors = factor(i)
            primes = union(primes, keys(factors))
        end

        result = []
        append!(result, primes)
        sort!(result)
        # println(result)
        WriteOutList(result, "Primes.log", "\n")
    end

    if false
        result = []
        for i in 1:10000
            # @printf "%d, %s\n" i sqrt(BigFloat(i))
            # println(i, sqrt(BigFloat(i)))
            push!(result, sqrt(BigFloat(i)))
        end
        WriteOutList(result, "Sqrt.log", "\n")
    end

    if false
        result = 0
        last_result = 0
        for i in 1:100000000
            result += 1 / BigFloat(i)
            if i % 100000 == 0
                @printf "result = %f\n" (result - last_result)
                last_result = result
            end
        end
        @printf "result = %f\n" result
    end

    if true
        println(sqrt(BigFloat(7)))
    end

end

main()
println("done!")
