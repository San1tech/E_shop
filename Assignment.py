#  #Leap year
years=[2002,2003,2004,2005,2006]
for year in years:
    if year % 4 == 0:
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")
#
# # odd or even
#
# val=[2,3,4,5,7,10,12]
# for num in val:
#     if num % 2 == 0:
#         print(num,"is even number")
#     else:
#         print(num,"odd number")
#
#  # sum from 1 to 100 number
# num=range(1,101)
# sum=0
# for val in num:
#     sum=sum+val
#     print(sum)

# prime number program

# num=(int(input("Enter a number:")))
# if num > 1:
#     for i in range(2, num):
#         if(num % i) == 0:
#             print(num,"is not a prime number")
#             break
#     else:
#             print(num,"is a prime number")
# else:
#     print(num,"is  not a prime number")

# #Armstrong number program
# number =int(input("Enter a number:"))
# str_num = str(number)
# digits = len(str(number))
# add_sum = 0
# for item in str_num:
#     num_val=int(item)
#     add_sum = add_sum +pow(num_val,digits)
# if add_sum == number:
#     print(number,"is an Armstrong Number")
# else:
#     print(number,"is not a Armstrong Number")
