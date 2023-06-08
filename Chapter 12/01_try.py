while True:
    print("Press q to quit")  # Display a message for the user to quit
    a = input("Enter a number\n")  # Prompt the user to enter a number
    
    if a == 'q':  # Check if the user entered 'q' to quit
        break
    
    try:
        a = int(a)  # Convert the input to an integer
        if a > 6:
            print("You entered a number greater than 6.")  # Display a message if the number is greater than 6
    except Exception as e:
        print("Invalid input: Please enter a valid integer") # Display an error message if the input cannot be converted to an integer
    
print('Thanks for playing this game!')  # Display a final message when the program ends


# while True:
#     print("Press q to quit")
#     a = input("Enter a number\n")
#     if a == 'q':
#         break
#     try:
#         a = int(a)
#         if a > 6:
#             print("You entered a number greater than 6.")
#     except ValueError:
#         print("Invalid input: Please enter a valid integer.")
# print('Thanks for playing this game!')
