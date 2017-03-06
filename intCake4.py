# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges
# from operator import itemgetter

meeting_times = [(0, 1), (3, 5), (4, 8), (5, 9), (10, 12), (9, 10), (11, 12)]

def merge_ranges(meeting_times):
	ordered_meeting_times = sorted(meeting_times)

	start_ends = zip(*ordered_meeting_times)

	start_times = list(start_ends[0])
	end_times = list(start_ends[1])

	merging = True

	while merging == True:
	
		for i in range(len(ordered_meeting_times)):

			try:
				# if end_times[i] < start_times[i+1]:
				# 	print "got to if"

				if end_times[i] >= start_times[i+1]:
					merging = True
					del start_times[i+1]
					del end_times[i]

				else:
					merging = False

			except IndexError:
				continue

		answer = zip(start_times, end_times)

	print answer

merge_ranges(meeting_times)


################################################################################
# ******faster interview cake answer******

# meeting_times = [(0, 1), (3, 5), (4, 8), (5, 9), (10, 12), (9, 10), (11, 12)]

# # should return [(0, 1), (3, 12)]

# def merge_ranges(meeting_times):
# 	"""determines all busy times based on list of tuples showing busy calendar times"""

# 	ordered_meeting_times = sorted(meeting_times)

# 	# new list for merged meetings, start it with the first in the ordered list
# 	busy_times = [ordered_meeting_times[0]]

# 	# for loop starts after the 0th element
# 	for start_time, end_time in ordered_meeting_times[1:]:
# 		# print "ordered_meeting_times[1:]", ordered_meeting_times[1:]

# 		# the (start, end) equals last thing in merged meetings?
# 		last_merged_meeting_start, last_merged_meeting_end = busy_times[-1]
# 		print "last merged meetings", busy_times[-1]

# # I think busy_times is just a way to hold the current merged tuple while you're going through 
# 		# if the current and last meetings overlap, use the latest end time
# 		# if the current start is less than or equal to last merged meeting end
# 		if (start_time <= last_merged_meeting_end):
# 			# and then we make busy_times[-1] into the last start and the MAX OF THE TWO end times!!!
# 		    busy_times[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, end_time))

# 		# add the current meeting since it doesn't overlap
# 		else:
# 		    busy_times.append((start_time, end_time))

# 	print busy_times

# merge_ranges(meeting_times)


################################################################################################

	# ordered_meeting_times = sorted(meeting_times)
	# # number_to_go_back = len(ordered_meeting_times)
	# # print ordered_meeting_times
	# merging = True

# 	# if no merges then false and it'll stop
# 	while merging == True:
# 		print "cont"
# 		# but the for loop, means it's only going through 7 times?

# 		for i in range(len(ordered_meeting_times)):

# 			if ordered_meeting_times[i] == ():
# 				print "NOTHING"
# 				# go back to the start?
# 				continue

# 			else:
# 				start_time = ordered_meeting_times[i][0]
# 				end_time = ordered_meeting_times[i][1]
# 				# print ordered_meeting_times

# 				try:
# 					# print ordered_meeting_times
# 					# print ordered_meeting_times[i+1]
# 					if end_time >= ordered_meeting_times[i+1][0]:
# 						print "yes"
# 						print end_time, ordered_meeting_times[i+1][0]
# 						ordered_meeting_times[i] = ((start_time, ordered_meeting_times[i+1][1]))
# 						# make the merged extra tuple into and empty tuple and append it to the end of the list to keep the same length
# 						del ordered_meeting_times[i+1]
# 						number_to_go_back -= 1
# 						# AND append to the end of the list - except not using append?
# 						ordered_meeting_times.append(())
						
# 						print ordered_meeting_times

# 						print ordered_meeting_times[i]
# 						# print number_to_go_back

# 					if end_time < ordered_meeting_times[i+1][0]:
# 						print "no"
# 						i = ((start_time, end_time))
				
# 				except: 
# 					# [(0, 1), (3, 12), (11, 12)]
# 					# if i is the last tuple in the list with 2 intesgers...
# 					# can't use last item in the list because they will be () empty tuples
# 					if i == (len(ordered_meeting_times) - number_to_go_back):
# 						print i, "got to this except"

# 						if start_time >= ordered_meeting_times[i-1][1]: 
# 							ordered_meeting_times[i] = ((ordered_meeting_times[i-1][0], end_time))
# 							ordered_meeting_times[i-1] = ()

# 						if end_time < ordered_meeting_times[i-1][0]:
# 							i = ((start_time, end_time))

# 				else:
# 					merging = False
# 					# print ordered_meeting_times

# merge_ranges(meeting_times)


# Currently returns:
# (env) Kellys-MacBook-Pro-2:intCake kellyhoffer$ python intCake4.py
# [(0, 1), (3, 5), (4, 8), (5, 9), (9, 10), (10, 12), (11, 12)]
# [(0, 1), (3, 5), (4, 8), (5, 9), (9, 10), (10, 12), (11, 12)]
# [(0, 1), (3, 8), (5, 9), (9, 10), (10, 12), (11, 12), ()]
# [(0, 1), (3, 8), (5, 9), (9, 10), (10, 12), (11, 12), ()]
# [(0, 1), (3, 8), (5, 10), (10, 12), (11, 12), (), ()]
# [(0, 1), (3, 8), (5, 10), (10, 12), (11, 12), (), ()]
# [(0, 1), (3, 8), (5, 10), (10, 12), (), (), ()]


