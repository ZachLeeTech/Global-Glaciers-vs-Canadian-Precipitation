"""
The processing_data module is responsible for processing the data
Project Name: The Relationship Between
Global Glacier Mass Changes and Precipitation in Canada
Programmer name: Zachary Lee
Date Submitted: 14/12/2020

Copyright and Usage information
===============================
This file is Copyright (c) 2020 Zachary Lee
"""
from typing import List, Dict
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def average_precipitation(city_data: List[Dict[int, float]]) \
        -> Dict[int, float]:
    """Average the precipitation of all the cities and return a dict of year to
    average precipitation.

    Preconditions:
        - len(city_data) > 1
        - len(city_data[0]) > 0

    >>> city_data = [{1970: 823.95, 1971: 788.58, 1972: 829.52, 1973: 812.75, 1974: 841.25}, {1970: 730.29,\
    1971: 777.6, 1972: 772.79, 1973: 781.89, 1974: 759.15}]
    >>> average_precipitation(city_data)
    {1970: 777.12, 1971: 783.09, 1972: 801.155, 1973: 797.3199999999999, 1974: 800.2}
    """
    average_precipitations_so_far = {}
    for year in city_data[0]:
        current_sum = [city_data[city].get(year) for city in range(0, len(city_data))]
        average = sum(current_sum) / len(city_data)
        average_precipitations_so_far[year] = average

    return average_precipitations_so_far


def display_graph(glacial_data: Dict[int, float],
                  average_precipitation_data: Dict[int, float]) -> None:
    """Using plotly, create a graph of global glacial mass change in
    gigatonnes/year vs. time in years and a graph of average
    precipitation in Canada vs. time in years.

    Preconditions:
        - len(glacial_data) > 0
        - len(average_precipitation_data) > 0
    """
    years = list(average_precipitation_data.keys())
    precipitation = [average_precipitation_data.get(year) for year in years]
    mass_change = [glacial_data.get(year) for year in years]

    fig = make_subplots(rows=2, cols=1, subplot_titles=("Global Glacial Mass Change",
                                                        "Canadian Average Precipitation"))

    fig.add_trace(go.Scatter(x=years, y=mass_change), row=1, col=1)
    fig.add_trace(go.Scatter(x=years, y=precipitation), row=2, col=1)

    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)

    fig.update_yaxes(title_text="Glacial Mass Change(Gt/year)", row=1, col=1)
    fig.update_yaxes(title_text="Average Precipitation(mm)", row=2, col=1)

    title = f'Global Glacial Mass Change vs. Canadian Average Precipitation ' \
            f'from {years[0]} to {max(years)}'
    fig.update_layout(title_text=title, showlegend=False)

    fig.show()


def display_table(glacial_data: Dict[int, float],
                  average_precipitation_data: Dict[int, float]) -> None:
    """Using plotly, create a table showing the global glacial mass change
    in gigatonnes/year and the average precipitation in Canada
    over the years in the inputs.

    Preconditions:
        - len(glacial_data) > 0
        - len(average_precipitation_data) > 0
    """
    years = list(average_precipitation_data.keys())
    precipitation = [average_precipitation_data.get(year) for year in years]
    mass_change = [glacial_data.get(year) for year in years]

    fig = go.Figure(data=[go.Table(header=dict(values=['Year',
                                                       'Glacial Mass Change(Gt/year)',
                                                       'Average Precipitation in Canada(mm)']),
                                   cells=dict(values=[years, mass_change, precipitation]))
                          ])
    title = f'Global Glacial Mass Change vs. Canadian Average Precipitation ' \
            f'from {years[0]} to {max(years)}'
    fig.update_layout(title_text=title)

    fig.show()


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config={
        'allowed-io': ['read_city_data', 'read_all_cities', 'read_glacial_data'],
        'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
                          'plotly.graph_objects', 'plotly.subplots'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    doctest.testmod()
