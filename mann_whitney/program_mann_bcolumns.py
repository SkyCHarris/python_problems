import openpyxl
import scipy

def get_column(sheet, column_name):

    data_column = []
    wb = openpyxl.load_workbook("mann_whitney/newest.xlsx", data_only=True)
    sheet_num = wb.worksheets[sheet - 1]

    for row in sheet_num:

        # Convert alpha to index
        index = 0
        for char in column_name:
            index = index * 26 + (ord(char.upper()) - ord('A') + 1)
        
        # Get cell data for specified column
        data = row[index-1].value   # The -1 grabs us the correct column
        if data == 'P':
            data_column.append(1)
        elif data == 'F':
            data_column.append(0)
        else:
            data_column.append(data)
        cleaned_data = [x for x in data_column if isinstance(x, (int, float))]  # Filter for int/float type data
    return cleaned_data

# Variables holding column data
column1BD_TUG_PF_New = get_column(1, "BD")
column2BD_TUG_PF_New = get_column(2, "BD")
column1BK_MOCAP_PF_New = get_column(1, "BK")
column2BK_MOCAP_PF_New = get_column(2, "BK")
column1BO_Age2 = get_column(1, "BO")
column2BO_Age2 = get_column(2, "BO")

# Driver test for column data lists
print(f"column1BD_TUG_PF_New values: {column1BD_TUG_PF_New}")
print(f"column2BD_TUG_PF_New values: {column2BD_TUG_PF_New}")
print(f"column1BK_MOCAP_PF_New values: {column1BK_MOCAP_PF_New}")
print(f"column2BK_MOCAP_PF_New values: {column2BK_MOCAP_PF_New}")
print(f"column1BO_Age2 values: {column1BO_Age2}")
print(f"column2BO_Age2 values: {column2BO_Age2}")

# Mann-Whitney U test
mannwhit_BD_TUGPF_New = scipy.stats.mannwhitneyu(column1BD_TUG_PF_New, column2BD_TUG_PF_New)
print(f"Column BD TUGPF New Mann Whitney U test restuls: {mannwhit_BD_TUGPF_New}")
mannwhit_BK_Mocap_PF_New = scipy.stats.mannwhitneyu(column1BK_MOCAP_PF_New, column2BK_MOCAP_PF_New)
print(f"Column BK MOCAP PF New Mann Whitney U test restuls: {mannwhit_BK_Mocap_PF_New}")
mannwhit_BO_Age2 = scipy.stats.mannwhitneyu(column1BO_Age2, column2BO_Age2)
print(f"Column BO Age2 Mann Whitney U test restuls: {mannwhit_BO_Age2}")