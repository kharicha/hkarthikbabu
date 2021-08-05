arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            print ("ignore the rows without int value")
            continue

    print(arr)
    # find the max weather temp in first 10 days
    m = max(arr[0:10])
    print(m)

    # find the average temp in first week of jan
    a = sum(arr[0:7]) / len(arr[0:7])
    print(a)
