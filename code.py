# cook your dish here
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        if curr_start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, curr_end))
        else:
            merged.append(current)
    return merged

n = int(input().strip())
data = []
while len(data) < n:
    line = input().strip()
    if not line:
        continue
    data.append(tuple(map(int, line.split())))

for start, end in merge_intervals(data):
    print(start, end)
    