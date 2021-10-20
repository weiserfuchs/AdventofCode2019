bDouble = False
bGreater = True
iPre = 0
iCounter = 0
iDoubles = 1

for i in range(265275,781584):
    tmp = str(i)
    for ch in tmp:
        digit = int(ch)
        if digit < iPre:
            bGreater = False
        if digit == iPre:
            bDouble = True
            iDoubles +=1
            #print("Double Counter ",iDoubles," i:",i )
        else:
            if iDoubles == 2:
                bDouble = True
                iDoubles = 1
            else:
                bDouble = False
                iDoubles = 1
        iPre = digit
    if ((bDouble == True) and (bGreater == True) and (iDoubles % 2 == 0)):
        #print(i)
        iCounter += 1
    iPre = 0
    bGreater = True
    bDouble = False
    iDoubles = 1


print(iCounter)