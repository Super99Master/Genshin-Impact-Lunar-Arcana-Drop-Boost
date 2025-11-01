from math import log10
from scipy.optimize import Bounds, minimize

def calculate(pairs):
    def min_fun(probabilities):
        summ = 0
        for pair in pairs:
            p1 = probabilities[int(pair[0]) - 1]
            summ += log10(p1) + log10(probabilities[int(pair[1]) - 1]) - log10(1 - p1)
        return -summ
    
    return minimize(
        min_fun,
        [1 / 22 for _ in range(22)],                            #Uniform probability
        bounds=Bounds(0.000001,1),                  #Log(0) doesn't exist but a probability can be 0
        constraints={"type": "eq", "fun": lambda p: sum(p) - 1} #Sum or probabilities = 100%
    )

def print_result(result):
    print(result.success, result.fun)
    for p in result.x:
        print(str(round(p * 100, 2)).replace(".",","))