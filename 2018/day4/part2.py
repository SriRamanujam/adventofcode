#!/usr/bin/env python3

import re

def match_line(regex, line):
    return [m.groupdict() for m in regex.finditer(line)]


def process_shift(sleep_regex, wake_regex, slp_line, wake_line, schedule):
    matches = match_line(sleep_regex, slp_line)
    if len(matches) != 1:
        print("UNEXPECTED SLEEP LINE: {}".format(slp_line))
        exit(1)

    sleep_time = matches[0]['timestamp']
    slp_hour, slp_minute = [int(x) for x in sleep_time.split(':')]

    matches = match_line(wake_regex, wake_line)
    if len(matches) != 1:
        print("UNEXPECTED WAKE LINE: {}".format(line))
        exit(1)

    wake_time = matches[0]['timestamp']
    wake_hour, wake_minute = [int(x) for x in wake_time.split(':')]

    if slp_hour != 0 and wake_hour != 0:
        return
    if slp_hour != 0 and wake_hour == 0:
        slp_minute = 0
    if slp_hour == 0 and wake_hour != 0:
        print("UNEXPECTED LINE COMBO: {} and {}".format(slp_line, wake_line))
        exit(1)

    # we have normalized our data, time to put it into the thing
    for i in range(slp_minute, wake_minute):
        schedule[i] += 1


def process_schedules(schedules):
    max_times = 0
    time_of_max = -1
    guard_num = ""

    for k, v in schedules.items():
        for idx, num in enumerate(v):
            if num > max_times:
                max_times = num
                time_of_max = idx
                guard_num = k

    print("Guard {} spent minute {} asleep more than any other guard or minute - {} times!".format(guard_num, time_of_max, max_times))


if __name__ == "__main__":
    # sort the input chronologically
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    lines.sort()

    # compile regexes for performance

    # pulls out two groups 'timestamp' and 'guard_num' indicating the timestamp
    # and guard number starting their shift respectively
    shift_start_regex = re.compile('\[[0-9]{4}-[0-9]{2}-[0-9]{2} (?P<timestamp>[0-9]{2}:[0-9]{2})\] Guard #(?P<guard_num>[0-9]+)')
    falls_asleep_regex = re.compile('\[[0-9]{4}-[0-9]{2}-[0-9]{2} (?P<timestamp>[0-9]{2}:[0-9]{2})\] falls asleep')
    wakes_up_regex = re.compile('\[[0-9]{4}-[0-9]{2}-[0-9]{2} (?P<timestamp>[0-9]{2}:[0-9]{2})\] wakes up')

    sleep_schedules = {}


    lines = iter(lines)
    line = next(lines) # seed the iterator
    while True:
        match = [m.groupdict() for m in shift_start_regex.finditer(line)]

        if len(match) != 1:
            print("INVALID LINE: {}".format(line))
            exit(1)

        schedule = sleep_schedules.setdefault(match[0]['guard_num'], [0] * 60)
        print("Processing shift:\t{}".format(line))
        while True:
            try:
                line = next(lines)
            except StopIteration:
                process_schedules(sleep_schedules)
                exit(0)

            if "begins shift" in line:
                print("Done processing shift")
                break
            else:
                slp_line = line
                wake_line = next(lines)
                process_shift(falls_asleep_regex, wakes_up_regex, slp_line, wake_line, schedule)
