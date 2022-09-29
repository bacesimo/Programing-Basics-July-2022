import math
record_seconds = float(input())
distance_meters = float(input())
time_in_seconds_one_meter_swim = float(input())

total_time = distance_meters * time_in_seconds_one_meter_swim
slow_swim_times = math.floor(distance_meters / 15)
slow_swim_sec = slow_swim_times * 12.5
total_time_swim = total_time + slow_swim_sec

if record_seconds > total_time_swim:
    print(f"Yes, he succeeded! The new world record is {total_time_swim:.2f} seconds.")
else:
    result = total_time_swim - record_seconds
    print(f"No, he failed! He was {result:.2f} seconds slower.")
