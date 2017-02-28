# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.
# To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time) 
# These integers represent the number of 30-minute blocks past 9:00am.

# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges

# we could tell that the meetings overlapped because
# 	end_time of the first meeting was after the start_time of the second meeting 
# 	our ideas of first and second are important here - this only works 
# 	after we ensure that we treat the meeting that starts earlier as the first one...

meeting_times = [(1,3), (2,4)]

def merge_ranges(meeting_times):
	# get the start times - but they're not attached to 
	start_times = [start[0] for start in meetings]
	end_times = [end[1] for end in meetings]

	# assign the first meeting 
	first = min(start_times) 


	for meeting in meeting_times:
		if end_time of first == start time of second
			then merge meetings 
		
		if second ends before the first meeting ends [(1,5), (2,3)]
			then merge the meetings

		compare each tuple and earliest start_time = first
		and other is second

		# if the end_time of first >= start_time of the second
		# 	merge the two meetings into one time range


		# 	the resulting time range's start time = 
		# 	the first meeting's start_time and its end_time 
		# 	is the later of the two meeitngs end times
		else:
			leave them separate


# could we make the first and seconds into sets
firsts {1, 2, 3, 4}
seconds {2, 5, 6, 7}

and then do set math?
firsts & seconds = intersection {2, 3, 4}
 and the outliers mean, the start and ends?
