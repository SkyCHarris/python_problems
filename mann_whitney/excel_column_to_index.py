import openpyxl


def excel_column_to_index(sheet, column_name):
    column_index = 0
    for char in column_name:
        column_index = column_index * 26 + (ord(char.upper()) - ord('A')) + 1

    return column_index

def get_column_index(file_path, sheet_name, column_name):
    workbook = openpyxl.load_workbook(file_path)

    sheet = workbook[sheet_name]
    index = excel_column_to_index(sheet, column_name)
    return index

file_path = 'mann_whitney/the_new_datafile.xlsx'
sheet_name = 'Sheet1'
column_name = 'A'

column_index = get_column_index(file_path, sheet_name, column_name)
print(f"The index value for column {column_name} in sheet {sheet_name} is: {column_index}")