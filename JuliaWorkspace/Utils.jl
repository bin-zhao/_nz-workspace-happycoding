#
# Utils.jl
#

module Utils

export WriteOutList, DrawFunction, SplitStringByLength

function WriteOutList(List, FileName, Delim = "")
    open(joinpath(["output", FileName]), "w") do OutputFile
        write(OutputFile, join(List, Delim))
    end
end

function DrawFunction(FnToDraw, Range)
    # f(x) = x^2 + 3x + 2

    # a = 0
    # b = 2
    
    # plot_inst0 = plot(f, a, b, label = "f(x) = x^2 + 3x + 2", xlabel = "x", ylabel = "f(x)", title = "Graphical representation of an integral")
end

function SplitStringByLength(Str, SubLen)
    Result = String[]

    StrLen = length(Str)
    # Count = floor(Int32, StrLen / SubLen)
    # for i in 1:Count
    #     push!(Result, Str[(i - 1) * SubLen : i * SubLen - 1])
    # end
    # if isapprox(mod(StrLen, 1), 0)
    #     push!(Result, Str[Count * SubLen])
    # end

    for i in 1:SubLen:StrLen
        EndIndex = min(i + SubLen - 1, StrLen)
        push!(Result, Str[i : EndIndex])
    end

    return Result
end

end  # Utils
