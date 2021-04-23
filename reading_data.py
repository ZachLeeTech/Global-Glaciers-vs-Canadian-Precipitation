"""
The reading_data module is responsible for reading the files
Project Name: The Relationship Between
Global Glacier Mass Changes and Precipitation in Canada
Programmer name: Zachary Lee
Date Submitted: 14/12/2020

Copyright and Usage information
===============================
This file is Copyright (c) 2020 Zachary Lee
"""
from typing import Set, List, Dict
import csv


def read_all_cities(filenames: Set[str], start_year: int, end_year: int) \
        -> List[Dict[int, float]]:
    """Read all the precipitation data sets for each city
    represented by the paths in filenames and return a dict of
    year to precipitation.

    Preconditions:
        - len(filenames) > 0
        - all(filename != '' for filename in filenames)
        - start_year >= 1962
        - end_year <= 2005
        - start_year < end_year

    >>> read_all_cities({'datasets/Toronto, ON.csv', 'datasets/Victoria, BC.csv'}, 1970, 1972)
    [{1970: 730.29, 1971: 777.6, 1972: 772.79}, {1970: 823.95, 1971: 788.58, 1972: 829.52}]
    """
    city_data = []
    for filename in filenames:
        city_data.append(read_city_data(filename, start_year, end_year))

    return city_data


def read_glacial_data(filename: str, start_year: int, end_year: int) \
        -> Dict[int, float]:
    """Read the glacial data from a file and return a dict of year to
    glacial mass change in gigatonnes/year.

    Preconditions:
        - filename != ''
        - start_year >= 1962
        - end_year <= 2005
        - start_year < end_year

    >>> read_glacial_data('datasets/Zemp_etal_results_global.csv', 1962, 1966)
    {1962: -218.0, 1963: -44.0, 1964: 71.0, 1965: -21.0, 1966: -97.0}
    """
    with open(filename) as file:
        reader = csv.reader(file)

        for _ in range(0, 20):
            next(reader)

        data_so_far = {}
        for row in reader:
            if start_year <= int(row[0]) <= end_year:
                year = int(row[0])
                change = float(row[2])
                data_so_far[year] = change

    return data_so_far


def read_city_data(filename: str, start_year: int, end_year: int) \
        -> Dict[int, float]:
    """Read the precipitation data from a file and return
    a dict of year to precipitation.

    Preconditions:
        - filename != ''
        - start_year >= 1962
        - end_year <= 2005
        - start_year < end_year

    >>> read_city_data('datasets/Toronto, ON.csv', 1970, 1974)
    {1970: 730.29, 1971: 777.6, 1972: 772.79, 1973: 781.89, 1974: 759.15}
    """
    with open(filename) as file:
        reader = csv.reader(file)

        next(reader)

        data_so_far = {}
        for row in reader:
            year = int(row[0].split('-')[0])
            if start_year <= year <= end_year:
                rainfall = float(row[1])
                data_so_far[year] = rainfall

    return data_so_far


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config={
        'allowed-io': ['read_city_data', 'read_all_cities', 'read_glacial_data'],
        'extra-imports': ['python_ta.contracts', 'csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    doctest.testmod()
