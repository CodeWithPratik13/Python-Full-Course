# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [2, 3, 4, 23, 21, 54, 6767, 56, 34, 24, 7, 55, 32]

new = list(filter(lambda x: x>9, a))
print(new)