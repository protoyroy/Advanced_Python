name = input('Enter Your Name : ')
marks = int(input("Enter Your Marks: "))
phone = int(input("Enter Your Phone no: "))

template = "The name of the student is {}, his marks is {} and his phone no is {}"
output = template.format(name, marks, phone)
print(output)