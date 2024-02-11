# calculate area of a rectangle :
# length : float = float(input('enter length :'))
# breadth : float = float(input('enter breadth : '))

# area = length * breadth
# print(area)

#+++++++++++++++++
# greeting  msg
# name : str = input('enter your name: ')
# age :int = int(input('enter your age: '))
# msg = 'Hello '+name+ ', are you '+ str(age ) +' years old ?'

# print(msg)  # or print(f'Hello {name}, are you {age} years old ? ')

#======================
# check even or odd
# num : int = int(input('enter your num: '))
# check = num % 2 == 0 # may i write like this ? or print(num % 2 == 0) ?
# print(check)

#========================
# max , min num in list 
# list1 :list[int]= [23,45,12,78,97,34]
# max_num = max(list1)
# min_num = min(list1)

# print(f'maximum number is {max_num}. minimum number is {min_num}')
 
# can we do without using the max(),min()functions ?
#==========================
# def is_polindrome(word):
#     length = len(word)
    
    
#     for i in range(length) :
#       if (word[i]==word[length-1-i]) :
#         True                                  # some confusion here...
#       else : 
#         return False  # i didn't get the False statement ....
#     return  True 
# word :str = input('enter word: ')
# result = is_polindrome(word)
# print(result)

#===============================
# compound interest 





# ++++++++++++++++++++++++++++++++
# days---->years, months, days
# t_days :int =int(input('enter day : '))

# years = t_days // 365 
# rem_days = t_days - (365*years)
# months = rem_days // 30 
# days = rem_days - (30*months )

# print(f'{t_days} has {years} years, {months} months and {days} days')

#=============================
# sum of integers , which are in list
# list1 : list[int] = [12,34,56,78,90]

# sum = 0
# for num in list1 :
#   sum += num
# print(sum)

#==================================
# input- sentence ,, count number of word

# sentence : str = input('enter sentence: ')
# stripped_sen = sentence.strip().split(' ')

 
# #print(len(stripped_sen))

# count = 0
# for word in stripped_sen :
#       count += 1
# print(count)        # if [ 'qw'.'we',' ','dq'] how to remove spaced string in that list, if user gives extra spaces in middle of the sentence

#==============================
# swapping
# num_1 :int = 20
# num_2 :int = 30

# # swapping a,b = b,a
# num_1 , num_2 = num_2 , num_1


# print(f'num1 is {num_1} and num2 is {num_2}')

#=================================
# sum and avg

# def sum(list1) :
#   l = len(list1)
#   sum = 0
#   for num in list1 :
#     sum += num
#   avg = sum / l
#   return f'sum of list1 is {sum}. and average is {avg}'

# list1 = [12,34,56,78,90]
# result = sum(list1)
# print(result)

#===============================
# number is a prime ?

# num :int = int(input('enter number : '))

# if num <= 0 :
#   print('this is negative nbrs')
# elif num > 1 :
#   if num == 1:
#       print('1 is not a prime nbr')
#   else :
#       fact=0
      
#       for j in range(2,num):
#         if num % j == 0 :
#            fact+=1 
              
#   if fact == 0:
#     print(f'{num} is prime number')       
#   else :
#     print(f'{num} is not a prime number')   

#==================================
# check number is a positive or negative  

# num :float = float(input('enter number'))
# if num > 0:
#   print(f'{num} is a positive number')
# elif num < 0:
#   print(f'{num} is a negative number')
# else :
#   print(f'{num} is zero')
#======================================

# for i in range (1,21) :
#   if i % 2 == 0:
#     print(i) 
#=====================================
# list1 = [12,32,13,65,34]
# # maxi = max(list1)
# # print(maxi)      # or
# list1.sort(reverse = True)
# maxi = list1[0]
# print(maxi)
#======================================
# def fact(num):          # just for practise
#     factors = ' '
#     for i in range(1,num+1) :
#        if num % i == 0:
#          factors +=str( i) + " "
#     return factors
# num :int = int(input('enter number'))
# result = fact(num)
# print(result) 

#-----------------
# def factorial(num) :
#   fact = 1
#   for i in range(1,num+1):
#       fact *= i
#   return fact
# num :int = int(input('enter number'))
# result = factorial(num)
# print(result)
#==============================
list1 = [1,6,3,9,3,5,'a',7,3,23,5,'a']
list_set = set(list1)
for i in list_set :
    counts = list1.count(i)
    print(f'{i} occurences are {counts} in list1')