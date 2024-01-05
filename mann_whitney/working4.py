import openpyxl
import scipy
import re
import pandas

def get_column(sheet, column_name):

    data_column = []
    wb = openpyxl.load_workbook("mann_whitney/dialysis_1.xlsx", data_only=True)
    sheet_num = wb.worksheets[sheet - 1]

    # Return list of column data
    for row in sheet_num:
        
        # Convert alpha to index
        index = 0
        for char in column_name:
            index = index * 26 + (ord(char.upper()) - ord('A') + 1)

        # Get cell data for specified column
        data = row[index-1].value   # -1 grabs correct column for some reason, teehee
        data_column.append(data)
        
        for i in str(data):
            if len(i) > 3 and i != 'N/A':
                pattern = re.compile('\d{2}-\d{2}-\d{4}')
                match_str = pattern.search(i)
                return match_str




# pth_b1 = get_column(1, "B")
# pth_b2 = get_column(2, "B")
# ca_c1 = get_column(1, "C")
# ca_c2 = get_column(2, "C")
# phos_d1 = get_column(1, "D")
# phos_d2 = get_column(2, "D")
vitd_e1 = get_column(1, "E")
vitd_e2 = get_column(2, "E")
# pthattx_f1 = get_column(1, "F")
# pthattx_f2 = get_column(2, "F")

# print("Column List Values:")
# print(f"PTH B1 Values (Dialysis): {pth_b1}")
# print(f"PTH B2 Values (Dialysis): {pth_b2}")
# print(f"Ca C1 Values (Dialysis): {ca_c1}")
# print(f"Ca C2 Values (Dialysis): {ca_c2}")
# print(f"Phos D1 Values (Dialysis): {phos_d1}")
# print(f"Phos D2 Values (Dialysis): {phos_d2}")
print(f"VitD E1 Values (Dialysis): {vitd_e1}")
print(f"VitD E2 Values (Dialysis): {vitd_e2}")
# print(f"PTH at Tx F1 Values (Dialysis): {pthattx_f1}")
# print(f"PTH at Tx F2 Values (Dialysis): {pthattx_f2}")

# print("Dialysis Mann-U Test results:")
