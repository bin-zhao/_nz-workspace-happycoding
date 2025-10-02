#
# UtilsUnitTest.jl
#

include("Utils.jl")

using .Utils
using Plots

setprecision(100000)

function UnitTest()
    Value = sqrt(BigFloat(2.0))
    # Value = BigFloat(2.0)
    # for _ in 1:16
    #     Value = (Value + BigFloat(2.0) / Value) / BigFloat(2.0)
    # end
    ValueStr = string(Value)
    ValueStr = ValueStr[3 : length(ValueStr)]
    Result = SplitStringByLength(ValueStr, 10)
    WriteOutList(Result, "UtilsUnitTest.txt", "\n")
end

UnitTest()
println("done!")
