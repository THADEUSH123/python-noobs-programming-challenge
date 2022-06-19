"""Simple script for manual scheduling that does not use basic libs."""

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"]

"""Regular year: days in months."""
mon_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

"""Leap year: days in months."""
leap_mon_len = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def generate_calendar(year):
    """Return a mapping of days in months for a 10 year block near year."""
    calendar = {}
    base_leap_year = year - ((year - 2015) % 4)
    print("Near {}: Years leap in {}, {}, and {}.".format(year,
                                                          base_leap_year,
                                                          base_leap_year+4,
                                                          base_leap_year+8))
    return calendar


class Date():
    """Simple date."""

    def __init__(self, date):
        """Initialize a date."""
        self.day, self.month, self.year = [int(x) for x in date.split("/")]

    def add_days(self, num_of_days):
        """Add 1 to 28 days to an arbitrary date.

        Logic as implemented does not allow adding more
        than 28ish days at a time. Logic could be improved.
        """
        max_days_this_month = mon_len[self.month-1]
        self.day += num_of_days
        if self.day > max_days_this_month:
            self.day -= max_days_this_month
            self.month += 1
            if self.month > 12:
                self.month -= 12
                self.year += 1

    def subtract_days(self, num_of_days):
        """Subtract 1 to 28 days to an arbitrary date.

        Logic as implemented does not allow subtracting more
        than 28ish days  at a time. Logic could be improved.
        """
        days_last_month = mon_len[self.month]
        min_days_this_month = 1
        self.day -= num_of_days
        if self.day < min_days_this_month:
            self.day = days_last_month
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1

    def __str__(self):
        """Return the Date in a string format similar to input."""
        return ("{:02d}/".format(self.day) +
                "{:02d}/".format(self.month) +
                "{:04d}".format(self.year))


def date_to_weekday(date):
    """Take a date as a string and calculate what weekday it will fall on."""
    base_date = "01/01/2015"  # Thursday / weekday_index = 4
    weekday_index = 4
    d = Date(date)
    if d.year >= 2015:
        while not base_date == str(d):
            weekday_index += 1
            d.subtract_days(1)
    else:  # self.year < 2015
        while not base_date == str(d):
            d.add_days(1)
            weekday_index -= 1

    return weekdays[weekday_index % 7]


def create_offset_days(starting_index, other_index):
    """Buid an offset list to track days from a starting point of 0."""
    def calc_offset(starting_index_val, other_index_val):
        """Ruturn a new index based off of the starting index at zero."""
        if other_index_val - starting_index_val < 0:
            return other_index_val - starting_index_val + 7
        else:
            return other_index_val - starting_index_val

    return sorted([calc_offset(starting_index, i) for i in other_index])


def recurringTask(firstDate, k, daysOfTheWeek, n):
    """Test function."""
    firstDate_weekday_index = weekdays.index(date_to_weekday(firstDate))
    other_weekday_index = [weekdays.index(d) for d in daysOfTheWeek]

    offset_list = create_offset_days(firstDate_weekday_index,
                                     other_weekday_index)

    print("Schedule will occur on offset of {} day(s) every {} week(s) from"
          " {}, which is a {}).".format(offset_list, k, firstDate,
                                        weekdays[firstDate_weekday_index]))

    dates = []

    for weeks_from_now in range(0, k*15/len(daysOfTheWeek)+1, k):
        days_to_start_of_week = 7 * weeks_from_now
        for day_offset in offset_list:
            d = Date(firstDate)
            d.add_days(day_offset+days_to_start_of_week)
            dates.append(str(d))

    return dates[0: n]

t = recurringTask("31/12/2014", 1, ["Wednesday", "Thursday"], 10)

print(t)

generate_calendar(2015)
