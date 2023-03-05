#!/usr/bin/python3
""" Module containing code that reads stdin line by line and computes metrics
"""
import sys

# Initialize variables for the metrics.
total_size = 0
status_counts = {}

try:
    # Read lines from standard input.
    for i, line in enumerate(sys.stdin, start=1):
        # Parse the fields from the input line.
        parts = line.split()
        ip_address, date, method, path, protocol, status_code, file_size = parts

        # Convert the file size to an integer.
        file_size = int(file_size)

        # Add the file size to the total size.
        total_size += file_size

        # Increment the count for the status code.
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        # Print the metrics every 10 lines.
        if i % 10 == 0:
            print(f"Total file size: File size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

    # Print the final metrics.
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    # Print the final metrics on keyboard interrupt.
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
