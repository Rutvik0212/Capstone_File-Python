'''Fizz Buzz - Write a program that prints the numbers from 1 to 100.
 But for multiples of three print “Fizz” instead of the number
  and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.'''

def isFizzBuzz(number):

    emt_list = []
    for num in range(1, number):

        if (num % 3 == 0 and num % 5 == 0):
            emt_list.append("FizzBuzz")

        elif (num % 3 == 0):
            emt_list.append("Fizz")
            
        elif (num % 5 == 0):
            emt_list.append("Buzz")

        else:
            emt_list.append(num)
    
    print(emt_list)

# isFizzBuzz(100)
