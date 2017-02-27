# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.
# To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time) 
# These integers represent the number of 30-minute blocks past 9:00am.

# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges


meeting_times = [(1,3), (2,4)]

def merge_ranges(meeting_times):
	we could tell that the meetings overlapped because
	end_time of the first meeting was after the start_time of the second meeting 
	our ideas of first and second are important here - this only works 
	after we ensure that we treat the meeting that starts earlier as the first one...

	assign the first meeting 
	1. the end_time of the First meeting and the start time of the second meeting are equal [(1,2), (2,3)]
	2. the second meeting ends befor ethe first meeting ends [(1,5), (2,3)]

	for each tuple in list:
		compare each tuple and earliest start_time = first
		and other is second

		if the end time of the first >= the start time of the second
			merger two meeting sinto one time range
			the resulting time range's start time is the first meeting's start and 
			its end time is the later of the two meeitngs end times
		else:
			leave them separate
