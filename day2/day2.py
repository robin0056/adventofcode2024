reports = []
with open('input.txt') as text: 
    for line in text: reports.append((line.strip()))

def is_safe(report: list) -> bool:
    return not(violates_trajectory(report) or violates_difference(report))
def violates_trajectory(report: list) -> bool:
    increasing_counter = 0
    decreasing_counter = 0
    for i in range(len(report)-1):
        increasing_counter = increasing_counter + (report[i] < report[i+1])
        decreasing_counter = decreasing_counter + (report[i] > report[i+1])
    only_increasing = increasing_counter+1 == len(report)
    only_decreasing = decreasing_counter+1 == len(report)
    return not(only_increasing or only_decreasing)
def violates_difference(report: list) -> bool:
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) > 3:
            return True
    return False

# task 1
result_1 = 0
for i in reports:
    my_list = [int(num) for num in i.split(' ')]
    result_1 = result_1 + is_safe(my_list)
print(result_1)

#  hardcoding but well...
def safe_after_dampening_report(report: list) -> bool:
    for i in range(len(report)):
        dampened_temporary_list = report.copy()
        dampened_temporary_list.pop(i)
        if is_safe(dampened_temporary_list):
            return True
    return False

# task 2
result_2 = 0
for report in reports:
    report_as_list = [int(num) for num in report.split(' ')]
    #check if safe
    if is_safe(report_as_list):
        result_2 = result_2 + (is_safe(report_as_list))
    else:
        # else if unsafe, try to damp
        result_2 = result_2 + safe_after_dampening_report(report_as_list)
print(result_2)