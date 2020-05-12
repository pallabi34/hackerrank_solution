number = input()
min_price =  int(number[:1])
for i in range(1, len(number)):
        new_price = int(number[:i]+number[i+1: ])
        print(min(new_price))
