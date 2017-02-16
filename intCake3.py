# Given a list_of_ints, 
# find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

# find max, pop, add popped to a new list_of_ints
# add those ints bam!

# lst = [11,9,4,7,13, 21, 55, 17]
# returns [55, 21, 17]
		# 93

# lst = [0, 9, 7]
# returns append three highest [9, 7]
	# None
# if there are only 3 numbers in the list I need an if statement 
# to add them before going through the loop
# if len(lst) == 3 then return three items added

# lst = [2, 2, 2]  
# 		same issue as above
# returns None

lst = [-1, 9, 8, -11]
# append three highest [9, 8]
# returns None

# lst = [-1, -9, -8, -11]
# returns
# append three highest [-1, -8]
# None

# lst = [-1, -9, -8, -11, -2]
# append three highest [-1, -2, -8]
# [-1, -2, -8]
# -11


def find_highest_product(lst):
	# list for the three highest numbers
	three_highest = []

	# product of three highest numbers
	product = None

	if len(lst) <= 3:
		product_of_three_highest = reduce(lambda x, y: x+y, lst)
		three_highest.append(product_of_three_highest)
		print "lst under 3"
		return product_of_three_highest
# THIS DOESN'T WORK BECAUSE WHEN THE LIST IS LESS THAN 3 (SINCE WE ARE REMOVING THE MAX NUMBERS, IT THEN HITS THE FIRST IF STATEMENT)
# HENCE GOING TO USE A WHILE LOOP
# JUST CHECKING THIS IS TO REMEMBER :)
	else:	
		for num in lst:				
			highest_num = max(lst)
			print "max", highest_num
			three_highest.append(highest_num)
			print "append three highest", three_highest
			lst.remove(highest_num)

			if len(three_highest) == 3:
				# multiply the remaining items in the list
				product_of_three_highest = reduce(lambda x, y: x+y, three_highest)

				print three_highest
				print product_of_three_highest

print find_highest_product(lst)



# 		lst.remove(product_of_three)
		
# 		for num in lst:
# 			two = max(lst)
# 			lst.remove(two)
# 			for num in lst:
# 				three = max(lst)
# 				lst.remove(three)

# # >>> lst = [3,7,2,9,11]
# # >>> for num in lst:
# 		add_top_three = 0
# # ...     one = max(lst)
# # ...     lst.remove(one)
# 		add_top_three += one
# # ...     print one
# ...     print lst
# ... 
# 11
# [3, 7, 2, 9]
# 9
# [3, 7, 2]
# 7
# [3, 2]
# >>> 
