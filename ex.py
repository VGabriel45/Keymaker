lst = [0, 1, 2, 3, 4]
n = len(lst)
d = 6
lst = lst[(n + d) % n:] + lst[0:(n + d) % n]
print(lst)
