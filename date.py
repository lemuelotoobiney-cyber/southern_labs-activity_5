# Author: Lemuel Waye Otoo-Biney
"""
This pythn script checks and calculates if a year is a Leap year 
and returns the day of the week of the month, day and year
"""
def is_leap_year(year):
    """
    This function calculates if the year is a Leap year and return a boolean
    True or False because Leap years occur every 4 years or roughly 400 years
    :param year: The year that will be checked if it is a leap year
    :return: The boolean if the year is a leap year
    """
    if year % 4 == 0:      # A Leap year is divisble by 4
        return True

    elif year % 100 == 0:    # A Leap year does not occur every 100 years
        return False

    elif year % 400 == 0:  # A Leap year is divisble by 400
        return True

    else:                   # A Leap year is divisble by 4
        return False



def get_day_of_the_week(month, day, year):
    """
    This function gets the day of the week by calculating if the date matches the date
    :param month: This is the Month 
    :param date: This is the day of the date
    :param year: This is the year of the date
    :return: The weekday / weekend of the month, day and year
    """
    # Step 1 Take last two digits and show how many 12s fit in the two digits
    last_two_digits = year % 100 # This returns the last 2 digits of the year 
    twelves_in_digits = last_two_digits // 12 # This determines how many 12s fit in it
    
    # Step 2 remainder of the two digits subtracted (twelves in two digits times 12)  
    remainder_value = last_two_digits - twelves_in_digits * 12

    # Step 3 Shows how many 4s fot into the remainder
    fours_in_remainder = remainder_value // 4

    # Add Month Code
    if month == 1: # january
        month_value = 1

    elif month == 2: # Febuary
        month_value = 4
    
    elif month == 3: # March
        month_value = 4

    elif month == 4: # April
        month_value = 0
    
    elif month == 5: # May
        month_value = 2
    
    elif month == 6: # June
        month_value = 5
    
    elif month == 7: # July
        month_value = 0

    elif month == 8: # August
        month_value = 3

    elif month == 9: # Septmeber
        month_value = 6

    elif month == 10: # October
        month_value = 1

    elif month == 11: # November
        month_value = 4

    elif month == 12: # December
        month_value = 6
    
    # Step 6: Add all the above numbers
    sum_of_numbers = twelves_in_digits + remainder_value + fours_in_remainder + day + month_value

    # Specific to leap years daates that have the month January and Febuary
    if is_leap_year(year):
        if month == 1:
            sum_of_numbers = sum_of_numbers + 6
        elif month == 2:
            sum_of_numbers = sum_of_numbers + 6

    # Specific to years ranges dates from 1600 to 2100
    if 1600 <= year and year < 1700:
        sum_of_numbers = sum_of_numbers + 6
        
    elif 1700 <= year and year < 1800:
        sum_of_numbers = sum_of_numbers + 4

    elif 1800 <= year and year < 1900:
        sum_of_numbers = sum_of_numbers + 2

    elif 2000 <= year and year < 2100:
        sum_of_numbers = sum_of_numbers + 6

    elif 2100 <= year and year < 2200:
        sum_of_numbers = sum_of_numbers + 4

    # Step 6 mod total by 7 
    weekday = sum_of_numbers % 7

    # These check if values of day of the week codes matches the date
    if weekday == 0:
        return "Saturday"

    elif weekday == 1:
        return "Sunday"

    elif weekday == 2:
        return "Monday"
    
    elif weekday == 3:
        return "Tuesday"
    
    elif weekday == 4:
        return "Wednesday"

    elif weekday == 5:
        return "Thursday"

    elif weekday == 6:
        return "Friday"


def main():
    """
    The main function to Test if the day of the week matches the month, day and year
    """
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


if __name__ == "__main__":
    main()


