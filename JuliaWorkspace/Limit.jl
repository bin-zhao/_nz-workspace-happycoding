#
# Limit.jl
#

setprecision(96)

bUsePlot = false

function truncate_decimal_deprecated(num::BigFloat, n::Int)
    factor = BigFloat(10^n)
    return floor(num * factor) / factor
end

function truncate_decimal(num::BigFloat, n::Int)
    str_num = string(num)
    if occursin(".", str_num)
        int_part, dec_part = split(str_num, ".")
        return parse(BigFloat, "$int_part.$(dec_part[1:n])")
    else
        return num  # 如果没有小数部分，直接返回
    end
end

function MainEntry()
    sqrt2 = sqrt(BigFloat(2))
    println(sqrt2)
    println(parse(BigFloat, string(sqrt2)[1:3]))
    # println(string(sqrt2)[1:4])
    # println(string(sqrt2)[1:5])
    println((sqrt2 - trunc(sqrt2)))

    # println(round(sqrt2, RoundDown, 1))
    # println(round(sqrt2, RoundDown, 2))
    # println(round(sqrt2, RoundDown, 3))

    cur = sqrt2
    for i = 50:-1:1
        next = nextfloat(cur)
        println(next - cur)
        cur = next
        # next = truncate_decimal(sqrt2, i)
        # println(next)
        # println(cur -  next)
        # cur = next
    end
end

MainEntry()
if bUsePlot
    readline()
end
println("done!")
