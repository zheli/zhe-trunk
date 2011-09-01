import sys
import datetime

def get_label(input_date = None):
    """Get input

    >>> get_label('1/2/3')
    ['1', '2', '3']

    """
    while True:
        if not input_date:
            input_date = raw_input("Give me a date: ")
        numbers = input_date.split('/', 2)
        if len(numbers) == 3:
            break
        else:
            print("Input should be like 1/7/89")

    return numbers

def date_parser(input_year, input_month, input_day):
    """
    >>> import datetime
    >>> date_parser('2011', '1', '1')
    datetime.date(2011, 1, 1)
    >>> date_parser('2011', '123', '1')
    Traceback (most recent call last):
    Exception: 123 is invalid for month
    >>> date_parser('2011', '13', '1')
    Traceback (most recent call last):
    Exception: 13 is invalid for month
    >>> date_parser('2011', '9', '31')
    Traceback (most recent call last):
    Exception: Invalid day in date 2011/9/31
"""

    if len(input_year)==4:
        year = int(input_year)
    else:
        year = int(input_year) + 2000
    if len(input_month)>2 or int(input_month) > 12:
        raise Exception('%s is invalid for month' % input_month)
    else:
        month = int(input_month)
    day = int(input_day)
    try:
        return datetime.date(year, month, day)
    except:
        raise Exception('Invalid day in date %s/%s/%s' % (input_year, input_month, input_day))

def main(input_date = None):
    """
    >>> main('2011/1/1')
    '2011-01-01'
    >>> main('2011/123/1')
    '2011/123/1 is invalid'
    >>> main('2011/13/1')
    '2011/13/1 is invalid'
    >>> main('000/1/1')
    '2000-01-01'
    >>> main('00/1/1')
    '2000-01-01'
    >>> main('0/1/1')
    '2000-01-01'
    >>> main('99/1/1')
    '2099-01-01'
    >>> main('5/1/2')
    '2001-02-05'

    """
    dates = []
    earliest_date = None
    if not input_date:
        number_list = get_label()
    else:
        number_list = get_label(input_date)

    try:
        dates.append(date_parser(number_list[0], number_list[1], number_list[2]))
    except Exception:
        pass

    try:
        dates.append(date_parser(number_list[1], number_list[2], number_list[0]))
    except Exception:
        pass

    try:
        dates.append(date_parser(number_list[2], number_list[0], number_list[1]))
    except Exception:
        pass

    try:
        dates.append(date_parser(number_list[2], number_list[1], number_list[0]))
    except Exception:
        pass

    if dates:
        earliest_date = dates[0]
        for date in dates:
            if date<earliest_date:
                earliest_date = date

    if earliest_date:
        return earliest_date.strftime("%Y-%m-%d")
    else:
        return '%s is invalid' % input_date

if __name__ == "__main__":
    import doctest
    main()
