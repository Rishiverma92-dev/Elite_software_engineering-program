def second_largest(li):
    li.remove(max(li))
    print(max(li))

        
second_largest([12,43,34,44,54,35])