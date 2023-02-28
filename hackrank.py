def fizzBuzz():
    # Write your code here

    # bu = "FizzBuzz"
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzBuzz()

# if __name__ == '__main__':
#     n = int(input().strip())

#     fizzBuzz(n)
# print(fizzBuzz(n))
