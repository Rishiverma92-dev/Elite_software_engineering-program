def two_sum(li,target):
    seen = {}
    for i,num in enumerate(li):
        diff = target-num
        if diff in seen:
            return [seen[diff],i]
        seen[num]=i
    return[]
print(two_sum([2,8,10,11],21))
'''Time complexity : O(n)
Space complexity : O(n)'''

# Valid parenthesis
def isValid(char:str):
    mapping = {"}":"{" , ")":"(","]":"["}
    stack=[]
    for ch in char:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1]!=mapping[ch]:
                return False
            stack.pop()
        else:
            return False
    return not stack
print(isValid("()[]"))
'''Time complexity : O(n)
Space complexity : O(n)'''
        
#Best time to buy and sell stock        
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
       if price < min_price:
           min_price = price
       elif price - min_price > max_profit:
           max_profit = price-min_price
    return max_profit

print(maxProfit([12,2,21,22,3,2]))     
'''Time complexity : O(n)
Space complexity : O(n)'''

#Contains duplicates
def duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(duplicates([1,2,3]))
#one liner
def containsDuplicates(numbers):
    return len(numbers)!=len(set(numbers))
print(containsDuplicates([23,4,2,4]))
'''Time complexity : O(n)
Space complexity : O(1)'''

# Move zeroes
def moveZeroes(li):
    result = [x for x in li if x!=0]
    zeroes = [0] * (len(li) - len(result))
    return result+zeroes
print(moveZeroes([12,3,12,3,0,7,0]))
'''Time complexity : O(n)
Space complexity : O(n)'''        