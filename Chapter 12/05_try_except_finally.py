try:
    i = int(input("Enter a number: "))
    c = 1/i

except Exception as e:
    print(e)
    exit()

finally:
    print("We are successful")  #nothing can stop to run finally #it will run 10000% if anyone quit the program [exit()] 