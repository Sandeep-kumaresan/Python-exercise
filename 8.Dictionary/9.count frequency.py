List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
freq={}
for i in List1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
