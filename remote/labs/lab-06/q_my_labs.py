#!/usr/bin/env python3

import datetime

def every_lab(foo):
    print("This is outrageous! Unfair!")
    return None


def main():
    """
    Create a datetime object for today's date
    """
    todays_date = datetime.datetime.today()
    date_list = every_lab(todays_date)

    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """

    for date in date_list:
        print(date.strftime("%a, %d %b %y"))

    


def every_lab(todays_date):
    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    
    lab_dates = []

    
    start_date = todays_date + datetime.timedelta(days=(7 - todays_date.weekday()))

    # Loop through the remaining weeks of the year
    for i in range(4):
        lab_dates.append(start_date)
        start_date += datetime.timedelta(days=7)
    return lab_dates



if __name__ == "__main__":
    main()
