#!/usr/bin/env python3
""" Module containing script that reads stdin line by line and
    computes metrics:
"""
import sys

TOTAL_COUNTS = {'total': 0, '200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
TOTAL_FILE_SIZE = 0


def print_metrics(counts, file_size):
    """
    Prints the metrics for a given set of counts and file size
    """
    print("File size: {}".format(file_size))
    for code, count in counts.items():
        print("{}: {}".format(code, count))


def process_line(line):
    """
    Processes a single log line and updates the counts and file size
    """
    global TOTAL_FILE_SIZE
    global TOTAL_COUNTS

    # Parse the line
    fields = line.split()
    if len(fields) < 7:
        print("Invalid line format: {}".format(line.strip()))
        return

    try:
        status_code = fields[-2]
        file_size = fields[-1]
        TOTAL_FILE_SIZE += int(file_size)
        TOTAL_COUNTS['total'] += 1
        if status_code in TOTAL_COUNTS:
            TOTAL_COUNTS[status_code] += 1
    except ValueError:
        print("Invalid line format: {}".format(line.strip()))
        return

    # Print the metrics every 10 lines
    if TOTAL_COUNTS['total'] % 10 == 0:
        print_metrics(TOTAL_COUNTS, TOTAL_FILE_SIZE)


# Process each line from stdin
for line in sys.stdin:
    process_line(line)

# Print the final metrics
print_metrics(TOTAL_COUNTS, TOTAL_FILE_SIZE)
