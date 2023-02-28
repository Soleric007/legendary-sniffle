# name = input('What is your name? ' )
# year = input('What year were you born in? ' )
# final_year = (2023 - int(year))
# final = str(final_year)
# print ('Hi ' + name + ' you are ' + final + ' years old')
def fizzBuzz(n):
    

    bu = "FizzBuzz"
    for i in range(1,n):
        if i == 3:
            print(bu)
        else:
            print(i)
        # if 0 == i % 15:
        #     print(bu)


    fizzBuzz(n)
