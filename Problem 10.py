from numba import jit


@jit
def Solver(targetTotal):
    TotalVal = 5
    Number = 4

    while Number < targetTotal:
        Divider = 2
        while ((Number % Divider) != 0) and (Divider < Number):
            if Divider == Number - 1:
                print(Number)
                TotalVal = TotalVal + Number
            Divider = Divider + 1
        Number = Number + 1
    print(TotalVal)


print(Solver(2000000))
# Finished, Ans = 142913828922. Took 20 minutes
