try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
# except Exception as e:
#     print("Exception Occured")
    # print(e)      # if anyone one to see what is the problem is occuring 

except ValueError as e:
    print("Please enter a valid value")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")

print("Thanks for using this code")
