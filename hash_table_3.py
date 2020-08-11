arr = {}

with open("poem.txt","r") as f:
    for line in f:
        print(line)
        tokens = line.split(' ')
        print(tokens)

        for word in tokens:
            word = word.replace('\n', '')
            print(word)
            if word not in arr:
                arr[word] = 1
            else:
                arr[word] += 1

    print(arr)