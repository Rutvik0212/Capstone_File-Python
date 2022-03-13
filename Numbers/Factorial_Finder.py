
def factorial(num):
    ans = 1
    if num == 0:
        print(f'Factorial is 1')
    for i in range(1,num+1):
        ans = ans * i
    print(f'Factorial is {ans}')

def fact_rec(num):
    if num == 0 or num == 1:
        return 1
    return num * fact_rec(num - 1)

num = int(input("Enter the Number you want to calculate factorial: "))
factorial(num)