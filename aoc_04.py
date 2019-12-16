bDouble = False
bGreater = True
iPre = 0
iCounter = 0


for i in range(265275,781584):
    tmp = str(i)
    for ch in tmp:
        digit = int(ch)
        if digit < iPre:
            bGreater = False
        if digit == iPre:
            bDouble = True
        iPre = digit
    if ((bDouble == True) and (bGreater == True)):
        iCounter += 1
    iPre = 0
    bGreater = True
    bDouble = False

print(iCounter)