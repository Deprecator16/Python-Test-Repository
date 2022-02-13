def createCostFunction(cost, shipping):
    def costFunc(count):
        return cost * count + shipping * 2

    return costFunc

func1 = createCostFunction(7, 10.5)
func2 = createCostFunction(19, 23)

print( func1(3) )
print( func2(7) )

















