import heapq

def minMeetingRooms(meetings):
    # Edge case: If there are no meetings, no rooms are required.
    if not meetings:
        return 0

    # Step 1: Sort the meetings by their start times.
    # This allows us to process the meetings in the order they happen.
    # Time complexity of sorting: O(n log n)
    meetings.sort(key=lambda x: x[0])

    # Step 2: Initialize a min-heap to keep track of meeting end times.
    # The heap helps us efficiently find the earliest ending meeting
    # (i.e., the room that becomes free the soonest).
    heap = []  # The heap will store the end times of ongoing meetings.

    # Step 3: Iterate through the sorted meetings one by one.
    for meeting in meetings:
        # If the room that finishes the earliest (smallest end time)
        # is free before the current meeting starts, we can reuse that room.
        # This is checked by comparing the smallest end time (heap[0])
        # with the start time of the current meeting.
        if heap and heap[0] <= meeting[0]:
            # Reuse the room by popping the earliest end time from the heap.
            heapq.heappop(heap)

        # Step 4: Add the current meeting's end time to the heap.
        # Whether we reused a room or need a new one, we add this meeting's
        # end time to the heap since this room is now occupied until that time.
        heapq.heappush(heap, meeting[1])

    # Step 5: The size of the heap gives us the number of rooms needed.
    # This is because each meeting in the heap represents a room in use.
    # At the end of the iteration, the heap size will reflect the peak number
    # of simultaneous meetings, which is the minimum number of rooms required.
    return len(heap)

# Sample Input
meetings = [[1, 4], [1, 5], [5, 6], [6, 10], [7, 9]]

# Expected Output: 2
print(minMeetingRooms(meetings))
