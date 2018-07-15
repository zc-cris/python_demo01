

number = 1
sum = 0
sum1 = 0
while number <= 100:
    if(number % 2 == 0):
        sum += number
    else:
        sum1 += number
    number += 1
print(sum, sum1)