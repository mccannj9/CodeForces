#! /usr/bin/env python

# http://codeforces.com/problemset/problem/816/A
# Problem name ::: A. Karen and Morning
# Submission Number: 28023241 (Accepted)

# A little irked that this problem wants you to return 0 if 
# original input time is already a palindrome, it should return
# the next time palindrome, because you can't sleep 0 mins


def compute_time_string_from_mins(mins):

    hrs = (mins // 60) % 24
    mins = mins % 60

    str_time = "%02d:%02d" % (hrs, mins)

    return str_time


def extract_total_mins_from_time_string_24h(time_string):

    time_string = time_string.split(":")

    hrs = int(time_string[0]) % 24
    mins = int(time_string[1])

    total_mins = hrs*60 + mins

    return total_mins


def compute_next_time_palidrome(time_input):

    time_input = time_input.rstrip()
    eingeschlafen = extract_total_mins_from_time_string_24h(time_input)
    total_mins = eingeschlafen

    while True:
        if time_input == time_input[::-1]:
            return total_mins - eingeschlafen

        total_mins += 1
        time_input = compute_time_string_from_mins(total_mins)


def main():

    import sys

    for line in sys.stdin:
        print(compute_next_time_palidrome(line))

if __name__ == '__main__':
    main()