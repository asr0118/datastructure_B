array = [11, 9, -77, 8]

for i in range(len(array)):
    print(f"{array[i]:3} {id(array[i])}")

print(f"{array[0]:3} {id(array[0])}")
print(f"{array[1]:3} {id(array[1])}")
print(f"{array[2]:3} {id(array[2])}")
print(f"{array[3]:3} {id(array[3])}")

print(array[0]), id(array[0])
print(array[1]), id(array[1])
print(array[2]), id(array[2])
print(array[3]), id(array[3])