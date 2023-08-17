#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num=10
    while num>0:
        print(num)
        num-=1
    print("Happy New Year!")
happy_new_year()        

def square_integers(int_list):
    # code goes here!
    square_list=[]
    for num in int_list:
        square=num*num
        square_list.append(square)
    print(square_list)
    return square_list    
square_integers([1, 2, 3, 4, 5])    

def fizzbuzz():
    # code goes here!
    nums=range(1,101)
    for num in nums:
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)            
fizzbuzz()