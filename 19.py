def fun(list):
    length = []
    for n in list:
        length.append((len(n), n))
    length.sort()
    return length[-1][0], length[-1][1]
result = fun(["PHP", "Exercises", "Backend"])
print("\nLongest word is: ",result[1])
print("Length of the longest word is: ",result[0])
