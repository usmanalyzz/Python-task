# 1. Reverse a string
# Question: Write a function to reverse a given string.
# Input: A single string s.
# Example: reverse_string("hello") should return "olleh”.


# def reverse_string(str):
# 	return str[::-1]

# str = “Hello”
# print(everse_string(str))

# 2. Check if a string is a palindrome
# Question: Write a function to check if a given string is a palindrome.
# Input: A single string s.
# Example: is_palindrome("madam") should return True.

# def is_palindrome(str):
# 	if str == str[::-1]:
# 		return True
# 	else:
# 		return False

# str = “madam"
# print(is_palindrome(str))

# 3. Count the frequency of each character in a string
# Question: Write a function to count the frequency of each character in a string.
# Input: A single string s.
# Example: char_frequency("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.


# def char_frequency(str):
# 	freq_dict = {}
# 	for char in str:
# 		if char in freq_dict:
# 			freq_dict[char] +=1
# 		else:
# 			freq_dict[char] = 1
# 	return freq_dict

# str = “hello”
# print(char_frequency(str))


# 4. Find the first non-repeating character in a string
# Question: Write a function to find the first non-repeating character in a string.
# Input: A single string s.
# Example: first_non_repeating("swiss") should return 'w’.


# def char_frequency(str):
# 	freq_dict = {}
# 	for char in str:
# 		if char in freq_dict:
# 			freq_dict[char] +=1
# 		else:
# 			freq_dict[char] = 1
# 	return freq_dict

# def first_non_repeating(str):
# 	freq = char_frequency(str)
# 	for char in str:
# 		if freq[char] == 1:
# 	return char

# str = “swiss”
# print(first_non_repeating(str))


# 5. Remove duplicate characters from a string
# Question: Write a function to remove duplicate characters from a string.
# Input: A single string s.
# Example: remove_duplicates("hello") should return "helo”.


# def remove_duplicates(str):
#  	result_str = “ "
# 	for char in str:
# 		if char not in result_str:
# 			result_str+=char
# 	return result_str

# str = “hello"
# print(remove_duplicates(str))



# 6. Find the largest and smallest elements in an array
# Question: Write a function to find the largest and smallest elements in an array.
# Input: A list of integers arr.
# Example: min_max([3, 5, 1, 9]) should return (1, 9).



# def min_max(list):
# 	min = list[0]
# 	max = list[0]

# 	for num in list:
# 		if num < min:
# 	   		 min = num
# 		if num > max:
# 	   		 max = num
# 	return (min, max)

# list = [3, 5, 1, 9]
# print(min_max(list))


# 7. Rotate an array by a given number of positions
# Question: Write a function to rotate an array to the right by a given number of positions.
# Input: A list of integers arr and an integer n (number of positions).
# Example: rotate_array([1, 2, 3, 4, 5], 2) should return [4, 5, 1, 2, 3].

# def rotate_array(list, num):
# 	n=n%len(list)
# 	return list[-n:  ]

#  rotate_array([1, 2, 3, 4, 5], 2)


# 8. Check if a number is prime
# Question: Write a function to check if a number is prime.
# Input: An integer num.
# Example: is_prime(7) should return True.

# def is_Prime(num):
# 	if num<=1:
# 		return False
# 	for n in range(2, num):
# 		if num%2==0:
# 		return false
# 	return True

# num = 7
# print(is_Prime(num))

# 9. Find the factorial of a number
# Question: Write a function to find the factorial of a number.
# Input: An integer num.
# Example: factorial(5) should return 120.


# def factorial(num):
# 	if num<0:
# 	return False
# 	if num==0 and num ==1:
# 	return True
# 	fact = 1
# 	for i in range(1, num+1)
# 		fact*=i
# 	return result


# factorial(5)



# 10. Find pairs in an array that sum up to a specific target
# Question: Write a function to find pairs of numbers in an array that add up to a given target.
# Input: A list of integers arr and an integer target.
# Example: find_pairs([1, 2, 3, 4], 5) should return [(1, 4), (2, 3)].




# def find_pairs(list, target):
#     pairs = [] 

#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):  
#             if list[i] + list[j] == target: 
#                 pairs.append((list[i], list[j])) 

#     return pairs 

# Target = 5
# List = [1, 2, 3, 4, 5]
# print( find_pairs(list, target))