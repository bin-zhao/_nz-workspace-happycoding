#
# ExceptionHandler.jl
#

module ExceptionHandler

export PrintException

function PrintException(ex, bRichText = true, bStack = true)
    println("\n###################################")
    if bRichText
        Base.showerror(stderr, ex)
    else
        println(sprint(showerror, ex))
    end

    if bStack
        println()
        Base.show_backtrace(stderr, catch_backtrace())
    end
    println("\n###################################\n")
end

end  # ExceptionHandler
