arr = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temp = int(tokens[1])
            arr[day] = temp
        except:
            print ("ignore the rows without int value")
            continue

    print(arr)

    # What was the temperature on Jan 9
    print("Temp on Jan 9:", arr['Jan 9'])

    # What was the temperature on Jan 4
    print("Temp on Jan 4:", arr['Jan 4'])

