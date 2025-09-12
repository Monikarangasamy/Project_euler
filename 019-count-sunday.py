def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def count_sunday():
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (is_leap_year):
        day = 366 % 7
    else:
        day = 365 % 7
    
    day_of_week = day +1 
    count = 0

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0: 
                count += 1
        
            days = days_in_month[month]
            if month == 1 and is_leap_year(year):
                days = 29
            day_of_week = (day_of_week + days) % 7

    return count
    
print(count_sunday())

