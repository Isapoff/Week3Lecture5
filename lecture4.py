# list comprehensin
# nums = [x for x in range(1,11)]             
# print(nums)

# nums = []
# for x in range (1,11):
#     nums.append(x)
# print(nums)

# nums = list(range(1,11))
# print(nums)

# numbers = [-1, 9,34, -43, 0, 9]
# nums = [x //3 if x % 3 == 0 else 0 for x in numbers if x > 0]
# print(nums)

      
                            #dict comprehension

# some_dict = {'a': 1, 'b': 2, 'c': 2, 'd':3}   
# some_dict['f'] = 4
# new_dict = {}  
# print(some_dict.items())                                          
# for key, value in some_dict.items():
#     new_dict[value] = key
# print(new_dict)
    
    # print(key)
    # print(value)

# some_dict = {'a': 1, 'b': 2, 'c': 2, 'd':3}
# dict_ = {value * 2: key if value  == 1 else key for key, 
#         value in some_dict.items() if value % 2}
# print(dict_)



                     #set comprehension

# some_set = {'aijana', 'larisa', 'bakyt', 'anton'}
# new_set = {name.capitalize() for name in some_set if name.startswith('a')}    #startswith metod stroki
# print(new_set)                                  # if name.startwith[0] == a



# d = {'a': 1, 'b': 2, 'c': 3}                         # mnojestvennoe prisvaevanie
# for x,y in d.items():
#     print(x)

# my_dict = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# new_dict = {key: val for key, val in my_dict.items() if val %5 == 0 or val % 3 == 0}
 
# print(new_dict)



# list_ = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# [1,2,3,4,5,6,7,8,9]
# new_list = []
# for item in list_:                                 #vlojeny cikl
#     for i in item:
#         new_list.append(i)

# print(new_list)


# num1 = 6
# num2 = input('Enter number: ')
# res = 0

# try:
#     res = num1 / num2
# except TypeError:
#     res = num1 / int(num2)

# print(res)



# flag = True
# while flag:
#     num1 = 6
#     num2 = input('Enter number: ')
#     res = 0
#     try:
#         num2 = int(num2)
#     except ValueError:
#         print('neccorectnye dannye')
#         continue                               # continue zavershaet iteraciu no ne zavershaet cikl
#     try:
#         res = num1 / num2                     
#         print(res)
#         break                                  # break ostanavlivaet cikl
#     except ZeroDivisionError:
#          print('na nol delit nelzya!')           # iteraciya eto povtornoe deistvie
#          continue
   

num1 = 6
num2 = 0
try:                                             #except srabotaet pri luboi oshibke
    res = num1 / num2                         
    print(res)
except ZeroDivisionError:
    raise Exception('na nol delit nelzya')      # s pomosh'y raise mojno vizvat' oshibku
    # print('na nol delit nelzya!')
else:
    print('oshibok ne bylo')                    #else srabotaet esli srabotaet try
finally:
    print('srabotau v lubom sluchae')           #finally srabotaet v lubom sluchae





