second = 60
minute = 60
hours = 24
days_week = 7
calculation_day = second * minute * hours
calculation_month= second * minute * hours*days_week
text_day = f"{calculation_day} seconds are in a day"
print(text_day)
text_week = f"{calculation_month} seconds are in a week"
print(text_week)