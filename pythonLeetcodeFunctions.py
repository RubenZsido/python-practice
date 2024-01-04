from unittest import result


arr = [3,5,7,2]
for i in range(len(arr)-1, -1, -1):
    print(i)
print("\n\n")

print(max(5,2))
print(max(arr))

print("\n\n")

dict = {"key": "value"}
dict[10] = "hahah"

print(dict)

for key, value in dict.items():
    print(key, value)

print("\n\n")

a = "my name is arnold"
str_arr = list(a)
print(str_arr)
str_arr[0], str_arr[1] = str_arr[1], str_arr[0]
print(str_arr)
a = 5
b = 0
a, b = b, a
print(a, b)
result_str = "".join(str_arr)
print(result_str)

cities = ["New York", "London", "Gyor", "New York"]
city_count = {}
for i in cities:
    city_count[i] = city_count.get(i, 0) + 1

print(city_count)