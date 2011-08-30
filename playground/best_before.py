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
        raise Exception('Invalid day maybe %s%s%s' % (input_year, input_month, input_day))

def main(input_date = None):
    """
    >>> main('1999/1/1')
    '1999-01-01'
    >>> main('1999/123/1')
    'Invalid date'
    >>> main('1999/13/1')
    'Invalid date'
    >>> main('000/1/1')
    '2000-01-01'
    >>> main('00/1/1')
    '2000-01-01'
    >>> main('0/1/1')
    '2000-01-01'
    >>> main('

    """
    if not input_date:
        number_list = get_label()
    else:
        number_list = get_label(input_date)

    try:
        date_1 = date_parser(number_list[0], number_list[1], number_list[2])
    except Exception:
        date_1 = None

    if date_1:
        return date_1.strftime("%Y-%m-%d")
    else:
        return 'Invalid date'

if __name__ == "__main__":
    import doctest
    main()
