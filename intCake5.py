# write a function that given an amount, and a list of coin denominations, 
# computes the number of ways to make an amount of money with coins
# of the available denominations

# what if the denominations can't add up to the exact amount? like only have 2's and 11 is the amount?


amount = 4
denominations = [1, 2, 3, 4]
number_of_denominations = 0
number_of_other_denominations = 0
remainder = 0

def make_change(amount):

	# make a function that will work for any denomination
	# for each denomination, we can use it once, twice or as many
	# times as it takes to reach ot overshoot the amount with the coins of that denomination alone

	for i in denominations:

		# tried this and it actually works and returns floats, could put a try/except in for non integers?
		# if amount < min(denominations):
		# 	print "cannot calculate as the amount is less than the available denominations"

		# if the ammount can evenly be divided by a single denomination, then calculate # of denominations needed
		if amount % i == 0:
			number_of_denominations = amount / i
			print "you need", number_of_denominations, "of", i

		elif amount % i != 0:
			number_of_denominations = amount / i
			remainder = amount % i
			
			for k in denominations:
				# then we need to find out which denominations the remainder can be divided by
				number_of_other_denominations = remainder / k

				if number_of_other_denominations > 0:
					print "you need", number_of_denominations, "of", i, "and", number_of_other_denominations, "of", k

make_change(amount)

