def moveZeroes(li):
    result = [x for x in li if x!=0]
    zeroes = [0] * (len(li) - len(result))
    return result+zeroes
print(moveZeroes([12,3,12,3,0,7,0]))