def add_time(start, duration, day=None):
    # Parse the start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_hour = start_hour % 12 + 12 if meridian == 'PM' else start_hour % 12

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the end time
    end_minute = (start_minute + duration_minute) % 60
    end_carry = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + end_carry) % 24
    end_meridian = 'PM' if end_hour >= 12 else 'AM'
    end_hour = end_hour % 12
    end_hour = 12 if end_hour == 0 else end_hour

    # Calculate the number of days later
    days_later = (start_hour + duration_hour + end_carry) // 24

    # Calculate the day of the week of the end time, if specified
    if day is not None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day = days.index(day.title())
        end_day = (start_day + days_later) % 7
        day_string = ', ' + days[end_day]
    else:
        day_string = ''

    # Generate the output string
    if days_later == 0:
        result = f"{end_hour:02d}:{end_minute:02d} {end_meridian}{day_string}"
    elif days_later == 1:
        result = f"{end_hour:02d}:{end_minute:02d} {end_meridian} (next day){day_string}"
    else:
        result = f"{end_hour:02d}:{end_minute:02d} {end_meridian} ({days_later} days later){day_string}"

    return result
