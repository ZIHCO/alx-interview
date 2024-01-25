#!/usr/bin/python3
"""log parsing"""
import re
import sys


try:
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\]'
                         r' "GET /projects/260 HTTP/1.1" (\d+) (\d+)')
    metric_dict = {
                   '200': 0,
                   '301': 0,
                   '400': 0,
                   '401': 0,
                   '403': 0,
                   '404': 0,
                   '405': 0,
                   '500': 0
                  }
    count = 0
    total_size = 0
    for line in sys.stdin:
        count += 1
        if bool(pattern.match(line)):
            list_line = line.split()
            status_code = list_line[-2]
            file_size = list_line[-1]
            total_size += int(file_size)
            metric_dict[status_code] += 1
            if count % 10 == 0:
                print(f"File size: {total_size}")
                for key in sorted(metric_dict.keys()):
                    if metric_dict[key] > 0:
                        print(f"{key}: {metric_dict[key]}")
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key in sorted(metric_dict.keys()):
        if metric_dict[key] > 0:
            print(f"{key}: {metric_dict[key]}")
    raise
