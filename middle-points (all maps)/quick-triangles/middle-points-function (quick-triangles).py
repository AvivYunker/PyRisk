quick_1 = [(100,100),(250,250),(400,100),(100,100)]
quick_2 = [(100,400),(250,250),(100,100),(100,400)]
quick_3 = [(400,100),(250,250),(400,400),(400,100)]
quick_4 = [(400,400),(250,250),(100,400),(400,400)]

arr_quick = [quick_1,quick_2,quick_3,quick_4]

for cnt1 in range(0, len(arr_quick), 1):
    x = int(0)
    y = int(0)
    for cnt2 in range(0, len(arr_quick[cnt1]), 1):
        x = int(x + arr_quick[cnt1][cnt2][0])
        y = int(y + arr_quick[cnt1][cnt2][1])
    x = int(x / 4)
    y = int(y / 4)
    print("(" + str(x) + "," + str(y) + ")")