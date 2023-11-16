def ubs(arr):
    n = len(arr[0])
    for one_count in range(n+1):
        if one_count == 0:
            continue
        for pos in range(n+1-one_count):
            # pos elotti 0 + onecount 1 + pos utani 0
            curstr = pos * "0" + one_count * "1" + (n - (pos + one_count)) * "0"
            if curstr not in arr:
                return curstr
print(ubs(["1111","0100"]))