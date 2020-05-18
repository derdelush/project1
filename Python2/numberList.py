count = []
countValue = 1
countMax = 50

while countValue <= countMax:
    count.append(countValue)
    countValue += 1
print(count, '\n')

countMax = 60
while countValue <= 60:
    count.append(countValue)
    countValue +=1
print(count, '\n')

multiples2 = []
for i in count:
    if i%2 == 0:
        multiples2.append(i)
print(multiples2, '\n')

multiples3 = []
for i in count:
    if i%3 == 0:
        multiples3.append(i)
print(multiples3)
