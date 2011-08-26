import sys
import datetime
before_date = datetime.date()

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

def find_year(number_list):
    """Find year in the string list

    >>> find_year(['1','2','2345'])
    '2345'
    >>> find_year(['1','2','0'])
    '2000'

    """
    for number in number_list:
        if int(number) > 31:
            if int(number) < 100:
                return str(int(number)+2000)
            return number
        if 0 == int(number):
            return '2000'
 #       if number > 


def main(input_date = None):
    """This function has no tests
    >>> main('02/4/67')
    '2067'

    """
    if not input_date:
        number_list = get_label()
    else:
        number_list = get_label(input_date)
    year = find_year(number_list)
    return year

if __name__ == "__main__":
    import doctest
    main()
