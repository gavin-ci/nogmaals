dayNight = ["am", "pm"]
time = 0
timeEnd = 12

for i in dayNight:
    while time < timeEnd:
        print(time, i)
        time += 1
    timeEnd += 12