try:
    i = int(input("Enter a number: "))
    c = 1/i

except Exception as e:
    print(e)
else:
    print("We are successful")      #if try run without any hassle it will execute otherwise it will not