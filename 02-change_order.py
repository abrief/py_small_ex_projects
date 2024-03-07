/* Chnge order from given list

def swap(data, a, b):
    temp = data[a]
    data[a] = data[b]
    data[b] = temp

data = [6, 5, 4, 3, 2, 1]

for i in range(1, len(data)):
    print(i)
    for j in range(1, len(data)):
        print(i, j)
        if(data[j] < data[j-1]):
            swap(data, j, j-1)

print(data)
