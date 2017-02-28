
# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges
# from operator import itemgetter

meeting_times = [(1,3), (2,4), (0, 5)]

def merge_ranges(meeting_times):

	# sorted() will put them in order
	ordered_meeting_times = sorted(meeting_times)
	print ordered_meeting_times
	
	# identify the first meeting
	first = ordered_meeting_times[0]
	print first

	second = ordered_meeting_times[1]
	print second

	for meeting in ordered_meeting_times:
# 		if end_time of first == start time of second
		if first[1] == second[0]:
# 			then merge meetings 

		
# 		if second ends before the first meeting ends [(1,5), (2,3)]
		if second[1] <= first[1]:
# 			then merge the meetings

# 		compare each tuple and earliest start_time = first
# 		and other is second

# 		# if the end_time of first >= start_time of the second
# 		# 	merge the two meetings into one time range

# 		# 	the resulting time range's start time = 
# 		# 	the first meeting's start_time and its end_time 
# 		# 	is the later of the two meeitngs end times
# 		else:
# 			leave them separate

# merge_ranges(meeting_times)

# the meetings overlapped because end_time of the first is after the start_time of the second 
# our ideas of first and second are important here


# # meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# # could we make the first and seconds into sets
# firsts {1, 2, 3, 4}
# seconds {2, 5, 6, 7}

# and then do set math?
# firsts & seconds = intersection {2, 3, 4}
#  and the outliers mean, the start and ends?


	# # get the start times - but they're not attached to 
	# start_times = [start[0] for start in meetings]
	# end_times = [end[1] for end in meetings]

	# # assign the first meeting based on lowest start time
	# first = min(start_times) 

	# # or sort the tuples by the first item, which is the start time - using itemgetter library? module?
	# sorted(meetings, key=itemgetter(0))
