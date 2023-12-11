from scipy.stats import mannwhitneyu
import openpyxl


#  Convert user input to excel format

def excel_column_to_index(column):
    index = 0
    for char in column:
        index = index * 26 + (ord(char.upper()) - ord('A')) + 1
    return index

#TODO: ^ Nest inside of get column function?

# Get sheet
def get_column(sheet, columnindex):
    data_column = []
    wb = openpyxl.load_workbook("mann_whitney//datafile.xlsx")
    sheet_num = wb.worksheets[sheet - 1]

# Get column
    for row in sheet_num:
        data = row[columnindex].value
        data_column.append(data)
    return data_column
