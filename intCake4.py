
# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges
# from operator import itemgetter

meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# meeting_times = [(1,3), (2,4)]

def merge_ranges(meeting_times):

	# sorted() will put them in order
	ordered_meeting_times = sorted(meeting_times)

	# identify the first meeting
	# first = ordered_meeting_times[0]
	# [(start_time, end_time)]
	# merge meetings where start_time and end_time don't have an upper bound
	# upper_bound = ordered_meeting_times[0][0]

	busy_times = []

	# for (start_time, end_time) in ordered_meeting_times:
	for i in range((len(ordered_meeting_times)) -1):
	# for meeting in ordered_meeting_times:
		start_time = ordered_meeting_times[i][0]
		end_time = ordered_meeting_times[i][1]

		if end_time < ordered_meeting_times[i+1][0]:
			busy_times.append((start_time, end_time))

					# start_time of next meeting 
		if end_time >= ordered_meeting_times[i+1][0]: 
			busy_times.append((start_time, ordered_meeting_times[i+1][1]))
		
		# works except for 4, 8 whcih fits inside 3, 8 which was created before
		# because i'm not comparing to the busy times list, just the ordered_meeting_times list
		
		
		print busy_times

merge_ranges(meeting_times)

	# for i in range(len(ordered_meeting_times)):
	# 	# print ordered[i], ordered[i + 1]
	# 	# ordered_meeting_times[i] is the item (1, 3) then (2, 4)
	# 	# if ordered_meeting_times[i] == ordered_meeting_times[i +1]
	# 		# do nothing
	# 	if ordered_meeting_times[i][1] >= [i+1][0]
	# 		# merge
	# 		busy_times.append((ordered_meeting_times[i][0], ordered_meeting_times[i]+1[1])

# 		if first == meeting:
# 			busy_times.append(meeting)

# # 		if end_time of first >= start time of next
# 		# then that meeting is within the bounds of the first and can be merged into it
# 		if first[1] >= meeting[0]:
# # 			then merge meetings into one time range [(0, 5), (1,3), (2,4)] (we totally lose (1,3) here)
# 			busy_times.append((first[0], meeting[1]))

# 		# if end time of first < start time of next, 

#  		# if first[1] < meeting[0]:
# 			# busy_times.append((meeting)
# 			# # print busy_times

# 		else:
# 			# leave them separate
# 			busy_times.append(meeting)

# 		print busy_times

# merge_ranges(meeting_times)


# 	same as if first[1] >= second[0]:
# 		if second ends before the first meeting ends[(0, 5), (1,3), (2,4)]
		# if second[1] <= first[1]:
		# 	busy_times.append((first[0], first[1]))
		# 	print busy_times

	# 	the resulting time range's start time = 
	# 	the first meeting's start_time and its end_time 
	# 	is the later of the two meeitngs end times



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
