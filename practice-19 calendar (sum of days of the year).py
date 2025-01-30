#Q19 Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

def dayOfYear(date):
    year, month, day = map(int, date.split('-'))
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False
    if is_leap_year(year):
        days_in_months[1] = 29
    day_number = sum(days_in_months[:month - 1]) + day
    
    return day_number

#test case:
print(dayOfYear("2019-01-09"))  # Output: 9
print(dayOfYear("2019-02-10"))  # Output: 41
