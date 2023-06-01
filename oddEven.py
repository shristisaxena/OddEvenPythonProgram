'''
Assignment 2 Day-3(Python Programming Essentials Bootcamp (3 Days)) 

A Python program to count number of odd and even number from the series of the list:

[ 2,3,4,55,56,78,75,69,66,101,100 ]
'''


numbers = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

count_even = 0
count_odd = 0

for num in numbers:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
