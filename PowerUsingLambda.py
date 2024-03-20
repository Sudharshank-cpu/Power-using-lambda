def povr(a):
   return lambda n:n**a
a=int(input("Enter Number: "))
b=int(input("Enter Times to Multiply: "))
powValue=povr(b)            
print(powValue(a))          #Example to attempt as Anonymous Values in "lambda" function