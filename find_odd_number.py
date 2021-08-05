def oddnum(num):
    odd_num = []

    for i in range(num):
        if i%2 == 1:
            odd_num.append(i)

    return odd_num

print("Odd numbers: ",oddnum(10))