total_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

time_to_read = total_pages / pages_per_hour
hours_per_day = time_to_read / days_to_read

print(round(hours_per_day))
