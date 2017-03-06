# write a function that given an amount, and a list of coin denominations, 
# computes the number of ways to make an amount of money with coins
# of the available denominations

# what if the denominations can't add up to the exact amount? like only have 2's and 11 is the amount?


amount = 4
denominations = [1,2,3]

def make_change(amount):

	# make a function that will work for any denomination
	# for each denomination, we can use it once, twice or as many
	# times as it takes to reach ot overshoot the amount with the coins of that denomination alone
	for denomination in denominations:

		for i in amount
			breakdown = amount / denomination

			return breakdown
			
			# if there is leftoved in the amount, 
			# try other denominations until the amoutn either == it or can be divided by it
