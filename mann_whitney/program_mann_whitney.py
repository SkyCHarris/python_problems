# Mann-Whitney U Function for Zhang MD Research

import openpyxl
import scipy


def get_column(sheet, column_name):

    data_column = []
    wb = openpyxl.load_workbook("mann_whitney/the_new_datafile.xlsx")
    sheet_num = wb.worksheets[sheet - 1]

    for row in sheet_num:

        # Convert alpha to index
        index = 0
        for char in column_name:
            index = index * 26 + (ord(char.upper()) - ord('A'))
        
        # Get cell data for specified column
        data = row[index].value
        data_column.append(data)
    data_column.pop(0)
    return data_column


# Mann-Whitney U Function

# columnF = scipy.stats.mannwhitneyu(get_column(1, "F"), get_column(2, "F"))
columnAL = scipy.stats.mannwhitneyu(get_column(1, "AL"), get_column(2, "AL"))
columnAP = scipy.stats.mannwhitneyu(get_column(1, "AP"), get_column(2, "AP"))
columnBD = scipy.stats.mannwhitneyu(get_column(1, "BD"), get_column(2, "BD"))
columnBI = scipy.stats.mannwhitneyu(get_column(1, "BI"), get_column(1, "BI"))

# print(f"Column F Mann-Whitney U test results: {columnF}")
print(f"Column AL Mann-Whitney U test results: {columnAL}")
print(f"Column AP Mann-Whitney U test results: {columnAP}")
print(f"Column BD Mann-Whitney U test results: {columnBD}")
print(f"Column BI Mann-Whitney U test results: {columnBI}")
