from random import choice

def coin_toss():
    states = {1: "Heads", 0:"Tails"}
    one_or_zero = choice([0, 1])
    result = states[one_or_zero]
    print(result)

coin_toss()
