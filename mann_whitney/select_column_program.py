from scipy.stats import mannwhitneyu
import openpyxl


# Get sheet
def get_column(sheet, columnindex):
    data_column = []
    wb = openpyxl.load_workbook("mann_whitney//datafile.xlsx")
    sheet_num = wb.worksheets[sheet - 1]    # -1 to match the number, not index

# Get column
    for row in sheet_num:   # Loop through each row of data
        data = row[columnindex].value   # Get cell data
        data_column.append(data)    # Append cell data to data_column list
    return data_column