# Mann-Whitney U Function for Zhang MD Research

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
        data_column.append(data)
        cleaned_data = [x for x in data_column if isinstance(x, (int, float))]  # Filter for int/float type data
    return cleaned_data

#TODO: Can clean up into dictionary?
#* Variables for column lists
column1AK_PTH = get_column(1, "AK")
column2AK_PTH = get_column(2, "AK")
column1AL_Ca = get_column(1, "AL")
column2AL_Ca = get_column(2, "AL")
column1AM_Phos = get_column(1, "AM")
column2AM_Phos = get_column(2, "AM")
column1AN_VitD = get_column(1, "AN")
column2AN_VitD = get_column(2, "AN")
column1AO_PTHatTx = get_column(1, "AO")
column2AO_PTHatTx = get_column(2, "AO")
column1AP_CaatTx = get_column(1, "AP")
column2AP_CaatTx = get_column(2, "AP")
column1AQ_PhosatTx = get_column(1, "AQ")
column2AQ_PhosatTx = get_column(2, "AQ")
# column1BE_TUG_PF_New = get_column(1, "BE")
# column2BE_TUG_PF_New = get_column(2, "BE")
# column1BL_MOCAP_PF_New = get_column(1, "BL")
# column2BL_MOCAP_PF_New = get_column(2, "BL")
# column1BO_Age2 = get_column(1, "BO")
# column2BO_Age2 = get_column(2, "BO")




#* Print column values
#* A Columns
print(f" column1AK_PTH values: {column1AK_PTH}")
print(f" column2AK_PTH values: {column2AK_PTH}")
print(f" column1AL_Ca values: {column1AL_Ca}")
print(f" column2AL_Ca values: {column2AL_Ca}")
print(f" column1AM_Phos values: {column1AM_Phos}")
print(f" column2AM_Phos values: {column2AM_Phos}")
print(f" column1AN_VitD values: {column1AN_VitD}")
print(f" column2AN_VitD values: {column2AN_VitD}")
print(f" column1AO_PTHatTx values: {column1AO_PTHatTx}")
print(f" column2AO_PTHatTx values: {column2AO_PTHatTx}")
print(f" column1AP_CaatTx values: {column1AP_CaatTx}")
print(f" column2AP_CaatTx values: {column2AP_CaatTx}")
print(f" column1AQ_PhosatTx values: {column1AQ_PhosatTx}")
print(f" column2AQ_PhosatTx values: {column2AQ_PhosatTx}")
#* B Columns
# print(f"column1BE_TUG_PF_New values: {column1BE_TUG_PF_New}")
# print(f"column2BE_TUG_PF_New values: {column2BE_TUG_PF_New}")
# print(f"column1BL_MOCAP_PF_New values: {column1BL_MOCAP_PF_New}")
# print(f"column2BL_MOCAP_PF_New values: {column2BL_MOCAP_PF_New}")
# print(f"column1BO_Age2 values: {column1BO_Age2}")
# print(f"column2BO_Age2 values: {column2BO_Age2}")



#* Mann Whitney U Test
#* A Columns
mannwhit_AK_PTH = scipy.stats.mannwhitneyu(column1AK_PTH, column2AK_PTH)
print(f"Column AK PTH Mann Whitney U test restuls: {mannwhit_AK_PTH}")
mannwhit_AL_Ca = scipy.stats.mannwhitneyu(column1AL_Ca, column2AL_Ca)
print(f"Column AL Ca Mann Whitney U test restuls: {mannwhit_AL_Ca}")
mannwhit_AM_Phos = scipy.stats.mannwhitneyu(column1AM_Phos, column2AM_Phos)
print(f"Column AM Phos Mann Whitney U test restuls: {mannwhit_AM_Phos}")
mannwhit_AN_VitD = scipy.stats.mannwhitneyu(column1AN_VitD, column2AN_VitD)
print(f"Column AN VitD Mann Whitney U test restuls: {mannwhit_AN_VitD}")
mannwhit_AO_PTHatTx = scipy.stats.mannwhitneyu(column1AO_PTHatTx, column2AO_PTHatTx)
print(f"Column AO PTHatTx Mann Whitney U test restuls: {mannwhit_AO_PTHatTx}")
mannwhit_AP_CaatTx = scipy.stats.mannwhitneyu(column1AP_CaatTx, column2AP_CaatTx)
print(f"Column AP CaatTx Mann Whitney U test restuls: {mannwhit_AP_CaatTx}")
mannwhit_AQ_PhosatTx = scipy.stats.mannwhitneyu(column1AQ_PhosatTx, column2AQ_PhosatTx)
print(f"Column AQ PhosatTx Mann Whitney U test restuls: {mannwhit_AQ_PhosatTx}")
#* B Columns
# mannwhit_BE_TUGPF_New = scipy.stats.mannwhitneyu(column1BE_TUG_PF_New, column2BE_TUG_PF_New)
# print(f"Column AQ PhosatTx Mann Whitney U test restuls: {mannwhit_BE_TUGPF_New}")

#TODO: Update print strings


# columnAK_PTH = scipy.stats.mannwhitneyu(get_column(1, "AK"), get_column(2, "AK"))



# # columnF = scipy.stats.mannwhitneyu(get_column(1, "F"), get_column(2, "F"))
# columnAL = scipy.stats.mannwhitneyu(get_column(1, "AL"), get_column(2, "AL"))
# columnAP = scipy.stats.mannwhitneyu(get_column(1, "AP"), get_column(2, "AP"))
# # columnBD = scipy.stats.mannwhitneyu(get_column(1, "BD"), get_column(2, "BD"))
# columnBI = scipy.stats.mannwhitneyu(get_column(1, "BI"), get_column(1, "BI"))

# # print(f"Column F Mann-Whitney U test results: {columnF}")
# print(f"Column AL Mann-Whitney U test results: {columnAL}")
# print(f"Column AP Mann-Whitney U test results: {columnAP}")
# # print(f"Column BD Mann-Whitney U test results: {columnBD}")
# print(f"Column BI Mann-Whitney U test results: {columnBI}")


