# Given a list of ints, find the product of every integer except the the int at that index
# for example [1, 7. 3, 4]
# returns [84, 12, 28, 21]
# by calculating [7*3*4, 1*3*4, 1*7*4, 1*7*3]

# DO NOT use division in your solution

# TESTS
# What if number is 0 or negative?
# are we returning the same list with the items replaced or a new list?
# what if there is only 1 number in the list?
# what if there are only two numbers in the list?
# What if all the numbers in the list are the same?

lst = [1,7,3,4]
products = []

def multiply_the_rest(lst):

	for num in lst:
		# remove the first item in the list with .pop(0)
		# using .pop because we need to add the item back in 
		x = lst.pop(0)
		
		# multiply the remaining items in the list
		y = reduce(lambda x, y: x*y, lst)

		# add the product to a new list
		products.append(y)

		# need to append popped item back on to the list at the end, before you start on the next item
		lst.append(x)

	return products

print multiply_the_rest(lst)


# OTHER WAYS BESIDES LAMBDA TO MULTIPLY ALL INTS IN LIST
# 	for i in range(0, len(lst)):
# 		total *= lst[i]
# 		print total

# or

# 		for num in lst: 
# 			total = total * num
# 		return total
