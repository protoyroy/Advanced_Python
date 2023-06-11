# def func(a):
#     return a + 5
func = lambda a: a +5 
square = lambda x: x*x
sum = lambda a, b, c: a+b+c 
# larger = lambda *args: (any(num>10 for num in args), args)  #if want to print boolean TRue or False
# larger = lambda *args: [num for num in args if num > 10]
larger = lambda num: num > 7

x = 4
l =[45, 3, 21 , 2, 5, 1, 7, 89]
print(func(x)) #print 9
print(square(x)) #print 16
print(sum(x, 3, 4)) #prints 11
# print(larger(x, 5, 7, 9, 12, 14, 15, 17))
print(list(filter(larger, l)))