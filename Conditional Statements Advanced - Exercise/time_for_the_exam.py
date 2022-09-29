exam_hour =int(input())
exam_minutes =int(input())
arrival_hour =int(input())
arrival_minutes =int(input())

# exam - 9:30 - > 570 min
# arr - 9:40 - > 580 min
exam_time_minutes = (exam_hour * 60) + exam_minutes
arrival_time_minutes = (arrival_hour * 60) + arrival_minutes

diff_min = abs(exam_time_minutes - arrival_time_minutes)

if exam_time_minutes < arrival_time_minutes:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif exam_time_minutes == arrival_time_minutes or diff_min <= 30:
    print("On time")
    if diff_min >= 1:
        print(f"{diff_min} minutes before the start")
else:
    print("Early")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")

