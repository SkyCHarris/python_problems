from scipy.stats import mannwhitneyu
import openpyxl


def get_column(sheet, column_name):

    data_column = []
    wb = openpyxl.load_workbook("mann_whitney//datafile.xlsx")
    sheet_num = wb.worksheets[sheet - 1]

    for row in sheet_num:
        index = 0
        for char in column_name:
            index = index * 26 + (ord(char.upper()) - ord('A'))
        data = row[index].value
        data_column.append(data)
    print(data_column)

get_column(1, "F")