# write a function that given an amount, and a list of coin denominations, 
# computes the number of ways to make an amount of money with coins
# of the available denominations

# what if the denominations can't add up to the exact amount? like only have 2's and 11 is the amount?


amount = 4
denominations = [1, 2, 3, 4]
number_of_denominations = 0
remainder = 0

def make_change(amount):

	# make a function that will work for any denomination
	# for each denomination, we can use it once, twice or as many
	# times as it takes to reach ot overshoot the amount with the coins of that denomination alone

	for i in denominations:

		# if the ammount can evenly be divided by a single denomination, then calculate # of denominations needed
		if amount % i == 0:
			number_of_denominations = amount / i
			print "you need", number_of_denominations, "of", i

		if amount % i != 0:
			number_of_denominations = amount / i
			remainder = amount % i
			print "you need", number_of_denominations, "of", i, "and you get a remainder of", remainder


make_change(amount)

			# # if the amount can
			# if amount / denomination == 0:
			# 	print denomination

			# # might not need this one, jsut the greater than 0 below
			# if amount / denomination != 0:
				
			# 	# divide amount by denomination (for a postive # result)
			# 	if amount / denomination > 0:

				# breakdown = amount / denomination

			# return breakdown
			
			# if there is leftoved in the amount, 
			# try other denominations until the amoutn either == it or can be divided by it
