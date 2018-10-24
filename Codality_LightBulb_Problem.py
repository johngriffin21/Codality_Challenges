A = [2,1,3,5,4]
y = []
for x in range(1,len(A)+1):
    y.append(["Off","Dull"])

tracker = 0
all_on = 0
for val in A:
    if val > 1:
        y[val-1] = ["On","Dull"]
    if val == 1:
        y[0] = ["On","Shine"]

    for i in range(len(A) - 2, 0, -1):
        if y[i][0] == "On" and y[i-1][0] == "On":
            y[i] = ["On","Shine"]

    tracker += 1
    counter = 0
    print(tracker,counter)
    for z in range(0,len(y)-1):
        if y[z] == ["On", "Shine"]:
            counter += 1
    if tracker == counter:
        all_on += 1
        print(all_on)
    print(tracker,counter)

print(all_on + 1)