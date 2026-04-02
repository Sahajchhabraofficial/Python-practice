#wap to create a list of squares of numbers from 1 to 10 using list comprehension
list_numbers=[32,45,67,89,23,12,34]
list_squares=[number*number for number in range(1,len(list_numbers)+1)]
print(list_numbers)
print(list_squares)