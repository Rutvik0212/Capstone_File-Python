num = int(input("Enter number to check Happy or not: "))
ans = num

def isHappyNumber(num):
    sum = 0 
    while(num > 0):
        rem = num % 10
        sum = sum +pow(rem , 2)
        num = num // 10
    return sum 

while (ans != 1 or ans != 4):
    ans = isHappyNumber(ans)

if (ans == 1):
    print(f'{num} is Happy number')
if (ans == 4):
    print(f'{num} is unHappy number')



