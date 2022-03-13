def Change_return(price, money):
    return_amount = money - price
    print(f'Return amount {return_amount}')
    change_list = []
    for rs in we_have:
        if rs <= return_amount:
            change = return_amount // rs
            change_list.append((rs,'*',change))
            return_amount = return_amount - (change * rs)
    print(*change_list, sep= '\n')
    
        
price = int(input("Enter the price of object : "))
money = int(input("Enter the Money given : "))
we_have = [100,10,50, 5, 2, 1]

Change_return(price, money)