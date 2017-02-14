
stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 1]

def get_max_profit(stock_prices_yesterday):

    max_profit = 0

# go through each price in the list where the index equals the time of the price

# using enumerate here. You can enumerate a list to get tuples by using
# list(enumerate(stock_prices_yesterday) which give you tuples:
# [(0, 10), (1, 7), (2, 5), (3, 8), (4, 11), (5, 9), (6, 1)]

    # so enumerate here loops over the list for the earlier_time and earlier_price
    # earlier_time = index
    # earlier_price = list item
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):
        # print earlier_time, earlier_price 

        # and go through all the LATER prices
        # then we want to look at the the prices and times that follow
        # since we have to buy first and sell after, we need to compare 
        # the earlier times to the later times to find the biggest difference(profit)

        # so for each price in the later prices after the outer loop, 
        for later_price in stock_prices_yesterday[earlier_time + 1:]:
            # print "later", later_price, stock_prices_yesterday[earlier_time+1:]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price
            # print "pp", potential_profit

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)
            print "mp", max_profit

    print max_profit


get_max_profit(stock_prices_yesterday)

# What if all the prices are the same?
assert (get_max_profit([10, 10, 10, 10, 10]) == 0, "all values the same, no profit")

# What if they only go down?
assert (get_max_profit([10, 1, 1, 0]) == -1, "all values lower, negative profit")

# What if there is a greater difference earlier in the day? 
assert (get_max_profit([3, 10, 2, 7]) == 7, "greater profit earlier")

# # What if there is a greater difference later in the day? 
# assert (get_max_profit([3, 10, 1, 9] == 8, "greater profit later")
# # why am I getting a syntax error on the line after??

# SyntaxError: invalid syntax
# Kellys-MacBook-Pro-2:Desktop kellyhoffer$ python intCake1a.py 
#   File "intCake1a.py", line 55