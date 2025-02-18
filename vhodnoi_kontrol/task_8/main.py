seconds = int(input())

days = seconds // 86400
seconds = seconds % 86400
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(days,':',hours,':',minutes,':',seconds)