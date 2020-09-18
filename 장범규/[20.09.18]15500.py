n = int(input())
rod1 = list(map(int, input().split()))
rod2 = []
rod3 = []

chk = n
mv = 0
result = []
while True :
    if (len(rod3) == n) :
        result.insert(0,mv)
        break

    if (chk in rod1) :
        while (len(rod1) != 0) :
            tmp = rod1.pop()
            if (tmp == chk) :
                result.append("1 3")
                mv += 1
                rod3.append(tmp)
                chk -= 1
                break
            else :
                result.append("1 2")
                mv += 1
                rod2.append(tmp)
    elif (chk in rod2) :
        while (len(rod2) != 0) :
            tmp = rod2.pop()
            if (tmp == chk) :
                result.append("2 3")
                mv += 1
                rod3.append(tmp)
                chk -= 1
                break
            else :
                result.append("2 1")
                mv += 1
                rod1.append(tmp)

for i in result :
    print(i)