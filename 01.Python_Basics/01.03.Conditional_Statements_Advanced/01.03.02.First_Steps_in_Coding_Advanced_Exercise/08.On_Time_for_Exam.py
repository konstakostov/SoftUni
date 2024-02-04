exam_hour = int(input())
exam_minutes = int(input())

arrival_hour = int(input())
arrival_minutes = int(input())

# Time in minutes
exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

difference = exam_time - arrival_time

if difference > 30:
    print("Early")
elif difference < 0:
    print("Late")
else:
    print("On time")

result = ""
hours = 0
minutes = abs(difference)

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += str(hours) + ":" +\
              ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
else:
    result += str(minutes) + " minutes"

if difference < 0:
    result += " after the start"
else:
    result += " before the start"

print(result)
