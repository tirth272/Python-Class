def ans(x, y, z):
    if x == y or y == z or x==z:
        ans = 0
    else:
        ans = x + y + z
    return ans
print(ans(9, 1, 1))

