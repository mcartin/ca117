#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"


class Schedule(object):

    def __init__(self):
        self.meetings = {}

    def add(self, m):
        self.meetings[m.hour] = m

    def __str__(self):
        output = []
        output.append("Schedule")
        output.append("--------")
        for k, v in sorted(self.meetings.items()):
            output.append(f'{v}')
        output.append(f"Meetings today: {len(self.meetings)}")
        return "\n".join(output)
