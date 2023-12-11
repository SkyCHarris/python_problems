
# import openpyxl module
import openpyxl
 
# Give the location of the file
path = "mann_whitney/datafile.xlsx"
 
# To open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path)
 
# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active
 
cell_obj = sheet_obj.cell(row=1, column=1)
 
print(cell_obj.value)