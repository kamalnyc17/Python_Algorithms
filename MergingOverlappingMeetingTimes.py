# our calendar contains the start and end time for each meeting with 30 minutes duration.
# this program will traverse the list and combine the overlapping meeetings
import os
meeting_schedule_for_today = [(1, 2), (2, 5), (5, 6), (3, 7)]


def merge_overlapping_range(scheduled_meetings):

    # Sorting the schedule by start time
    sorted_meetings = sorted(scheduled_meetings)

    # Initialize merged_meetings with the very first meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append(
                (current_meeting_start, current_meeting_end))

    return merged_meetings


# clear screen & print result
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Result: {merge_overlapping_range(meeting_schedule_for_today)}")
