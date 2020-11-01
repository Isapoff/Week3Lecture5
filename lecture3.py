# names = ('nurbek', 'atay', 'ermek', 'nargiza', 'bakyt', 'ermek')
# capitalized_names = []
# for name in names:
#     capitalized_names.append(name.capitalize())

# capitalized_names = [name.capitalize() for name in names]
# print(capitalized_names)

# nums = range(10)
# print('Nums =', nums)
# squared_nums = ['num ' + str(num) for num in nums]
# print(list(nums))
# print('squared_nums=', squared_nums)



# num = range(15)
# new = [item*3 for item in num]                         #sintaksis list comprehension


# users = ['Bakyt', 'Amantay', 'Atabek', 'The Best', 'Syimyk']
# users_that_know_iterator = [user for user in users if user == 'Amantay']
# print(users_that_know_iterator)

# nums = [1,2,3,4,-3,-6,0,-1,4,8,-3]
# positive_nums = [num for num in nums if num >=0]
# print(positive_nums)

# nums = [1,2,3,-4,3,-6,0,-1,4,8,3]
# odd_nums = [num for num in nums if num %2 !=0  and num >0]
# print(odd_nums)

# nums = range(100)
# numss = [num for num in nums if num %3 ==0 and num %5 == 0]           
# print(numss)


# for num in range(1,10):
#     print(end='\n')
#     for num2 in range(1,10):
#         print(num*num2, end='\t')
      

# numss = [num * num2 for num2 in range(1,10) for num in range(1,10)]
# print(numss)

nums = [f'even num {num}' if num % 2 == 0 else f'odd num {num}' for num in range(20)]
print(nums)

