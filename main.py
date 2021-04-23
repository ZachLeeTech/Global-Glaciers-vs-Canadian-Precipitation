"""
The main file of the project
Project Name: The Relationship Between
Global Glacier Mass Changes and Precipitation in Canada
Programmer name: Zachary Lee
Date Submitted: 14/12/2020

Copyright and Usage information
===============================
This file is Copyright (c) 2020 Zachary Lee.
"""

if __name__ == '__main__':
    import reading_data
    import processing_data

    file_paths = {'datasets/Baker Lake, NU.csv', 'datasets/Charlottetown, PEI.csv',
                  'datasets/Coral Harbour, NU.csv', 'datasets/Dawson, YT.csv',
                  'datasets/Edmonton, AB.csv', 'datasets/Fredericton, NB.csv',
                  'datasets/Halifax, NS.csv', 'datasets/Inuvik, NT.csv',
                  'datasets/Iqaluit, NU.csv', 'datasets/Kugluktuk, NU.csv',
                  'datasets/Mayo, YT.csv', 'datasets/Norman Wells, NT.csv',
                  'datasets/Quebec City, QC.csv', 'datasets/Regina, SK.csv',
                  'datasets/St. Johns, NL.csv', 'datasets/Toronto, ON.csv',
                  'datasets/Victoria, BC.csv', 'datasets/Whitehorse, YT.csv',
                  'datasets/Winnepeg, MB.csv', 'datasets/Yellowknife, NT.csv'}

    glacial_data_filepath = 'datasets/Zemp_etal_results_global.csv'

    city_data = reading_data.read_all_cities(file_paths, 1962, 2005)
    averaged_data = processing_data.average_precipitation(city_data)
    glacial_data = reading_data.read_glacial_data(glacial_data_filepath, 1962, 2005)

    processing_data.display_graph(glacial_data, averaged_data)
    processing_data.display_table(glacial_data, averaged_data)
