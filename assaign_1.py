
# create different variables for data types

# integer : int = 123
# decimal : float = 2.345
# string : str = 'this is string'
# boolean : bool = True

# perform basic opearations 


# num1 :int = 90
# num2 :int = 30
# # addition 
# sum = num1 + num2
# print(f'sum of numbers :',sum)  # 120

# # substraction
# sub = num1 - num2
# print(f'difference of numbers :',sub)

# #multiplacation
# mult = num1*num2
# print(f'multiplacation of numbers :',mult)

# # division 
# div = num1 / num2
# print(f'division :',div)

#type conversions
# convert int to float
# var :int = 30
# print(float(var))

# # convert  float to int
# var :float = 2.5
# print(int(var))

# # convert string number to a int
# var :str= '32'
# print(int(var))

# # convert bool to a string
# var :bool= True
# print(str(var))
#============================
# # control statements
# age :int = int(input('enter number : '))

# if age < 18 :
#   print('not eligible')
# else :
#   print("aplly for vote")
#==================================  
# # even or odd
# number :int= int(input('enter number : '))

# if (number % 2 == 0)  :
#   print('even')
  
# else : 
#   print('false')
  
#====================================
# year : int = int(input('enter year'))

# if year % 4 == 0 :
#   print('leap year')
  
# else :
#   print('not a leap year')
  
#======================================  not completed 
num1 : int = int(input('enter nbr: '))
num2 : int = int(input('enter another nbr: '))


operation = input('select : additon/substraction/multiplicaton/division : ')

if operation == 'addition' :
    print(num1 + num2)
elif operation == 'substraction' :
    print(num1 - num2)
elif operation == 'multiplication' :
    print(num1 * num2)
elif operation == 'division ':
    print(num1 / num2)
#===========================================
# while loop

# counter= 1
# while counter <= 10 :
#   print(counter,end=',')
#   counter+=1
  
  
#============================
# num : int = int(input('enter number : '))

# a = 1
# fact = 1 # not be zero
# while a< (num+1) :
#     fact *= a
#     a+=1
#     print(fact)

# for loop
# num : int = int(input('enter number : '))
# fact = 1    
# for i in range (1,num+1) :
#     fact *= i
#     print(fact)
#=========================================
# multiplication table :
# num : int = int(input('enter number: '))

# for i in range (1,11) :
#     mul = num * i
#     print(f'{num }X{i} = {mul} ' )

#=============================
# even or odd

# list_1 = [12,323,'34',45,656,67775]

# list_even = []
# list_odd = []
# for i in list_1 : 
#     each_nbr = int(i)
#     if each_nbr % 2 == 0 :
#         print(f'{each_nbr }is even')
#         list_even.append(each_nbr)
#     else : 
#         print(f'{each_nbr }is odd number')
#         list_odd.append(each_nbr)
# print(list_even)
# print(list_odd)  