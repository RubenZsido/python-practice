def ri(x):
	rx = list(reversed(str(x)))
	rx = "".join(rx)
	if rx[len(rx)-1] == "-":
		rx = "-" + rx[:-1]
	ri = int(rx)
	if ri > pow(2, 31-1) or ri < pow(-2, 31):
		return 0
	return ri

print(ri(-23))
