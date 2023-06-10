name = "Protoy"
worktype = "Software Engineer"
company = "Google"

# a = f"This is {name}"
a = "This is {0} and his company is {1} and he work as {2}".format(name,company, worktype) #Whatever value we want first we have to type index no
# a = "This is {} and his company is {} and he work as {}".format( worktype, name, company) #it will accordingly come whatever I have written first
print(a)