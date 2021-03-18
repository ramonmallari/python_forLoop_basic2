#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "Big"
    return list

print(biggie_size([-1,3,5,-5]))

#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(list):
    total = 0
    for x in range(len(list)):
        if list[x] > 0:
            total += 1
    list.pop(len(list)-1)
    list.append(total)
    return list
print(count_positives([1,6,-4,-2,-7,-2]))

#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(list):
    total = 0
    for x in range(len(list)):
        total = total + list[x]
    return total
    
print(sum_total([1,2,3,4]))

#4 Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def average(list):
    total = 0
    for x in range(len(list)):
        total = total + list[x]
    return total/len(list)
         
print(average([1,2,3,4]))

#5 Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(list):
    return len(list)

print(length([37,2,1,-9]))
print(length([]))

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def minimum(list):
    min = list[0]
    for x in range(len(list)):
        if list[x] < min:
            min = list[x]
    return min

print(minimum([37,2,1,-9]))

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def maximum(list):
    max = list[0]
    for x in range(len(list)):
        if list[x] > max:
            max = list[x]
        return max
        
print(maximum([37,2,1,-9]))

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    sum = sum_total(list)
    avg = average(list)
    min = minimum(list)
    max = maximum(list)
    total_length = length(list)
    analysis = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': total_length
    }
    return analysis

print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    list_len = len(list)
    for x in range(int(len(list)/2)):
        temp = list[list_len-1-x]
        list[list_len-1-x] = list[x]
        list[x] = temp
    return list

print(reverse_list([2,6,5,7,8,9]))