import openpyxl
import scipy
import pandas as pd
import re

# Load Excel file

xls = pd.ExcelFile('mann_whitney/dialysis_1.xlsx')
df1 = pd.read_excel(xls, 'GROUP 1 SUCCESSFUL')
df2 = pd.read_excel(xls, 'GROUP 2 DIALYSIS')

column_name_B = 'PTH'
column_name_C = 'Ca'
column_name_D = 'Phos'
column_name_E = 'VitD'
column_name_F = 'PTH at Tx'
column_name_G = 'Ca at Tx'
column_name_H = 'Phos at Tx'
column_name_I = 'TUG P/F'
column_name_J = 'MOCA P/F'


pth_B1_dialysis = pd.to_numeric(df1[column_name_B], errors='coerce').dropna().tolist()
pth_B2_dialysis = pd.to_numeric(df2[column_name_B], errors='coerce').dropna().tolist()
ca_C1_dialysis = pd.to_numeric(df1[column_name_C], errors='coerce').dropna().tolist()
ca_C2_dialysis = pd.to_numeric(df2[column_name_C], errors='coerce').dropna().tolist()
phos_D2_dialysis = pd.to_numeric(df1[column_name_D], errors='coerce').dropna().tolist()
phos_D1_dialysis = pd.to_numeric(df2[column_name_D], errors='coerce').dropna().tolist()
vitd_E1_dialysis = pd.to_numeric(df1[column_name_C], errors='coerce').dropna().tolist()
vitd_E2_dialysis = pd.to_numeric(df2[column_name_C], errors='coerce').dropna().tolist()
pthattx_F1_dialysis = pd.to_numeric(df1[column_name_F], errors='coerce').dropna().tolist()
pthattx_F2_dialysis = pd.to_numeric(df2[column_name_F], errors='coerce').dropna().tolist()
caattx_G1_dialysis = pd.to_numeric(df1[column_name_G], errors='coerce').dropna().tolist()
caattx_G2_dialysis = pd.to_numeric(df2[column_name_G], errors='coerce').dropna().tolist()
phosattx_H1_dialysis = pd.to_numeric(df1[column_name_H], errors='coerce').dropna().tolist()
phosattx_H2_dialysis = pd.to_numeric(df2[column_name_H], errors='coerce').dropna().tolist()
tug_pf_I1 = pd.to_numeric(df1[column_name_I], errors='coerce').dropna().tolist()
tug_pf_I2 = pd.to_numeric(df2[column_name_I], errors='coerce').dropna().tolist()
moca_pf_J1 = pd.to_numeric(df1[column_name_J], errors='coerce').dropna().tolist()
moca_pf_J2 = pd.to_numeric(df2[column_name_J], errors='coerce').dropna().tolist()



# print(tug_pf_I1)
# print(tug_pf_I2)
# # print(moca_pf_J1)
# # print(moca_pf_J2)

print(f"PTH (Dialysis): {scipy.stats.mannwhitneyu(pth_B1_dialysis, pth_B2_dialysis)}")
print(f"CA (Dialysis): {scipy.stats.mannwhitneyu(ca_C1_dialysis, ca_C2_dialysis)}")
print(f"Phos (Dialysis): {scipy.stats.mannwhitneyu(phos_D2_dialysis, phos_D1_dialysis)}")
print(f"VitD (Dialysis): {scipy.stats.mannwhitneyu(vitd_E1_dialysis, vitd_E2_dialysis)}")
print(f"PTH at Tx (Dialysis): {scipy.stats.mannwhitneyu(pthattx_F1_dialysis, pthattx_F2_dialysis)}")
print(f"Ca at Tx (Dialysis): {scipy.stats.mannwhitneyu(caattx_G1_dialysis, caattx_G2_dialysis)}")
print(f"Phos at Tx (Dialysis): {scipy.stats.mannwhitneyu(phosattx_H1_dialysis, phosattx_H2_dialysis)}")
print(f"TUG P/F (Dialysis): {scipy.stats.mannwhitneyu(tug_pf_I1, tug_pf_I2)}")
print(f"MOCA P/F (Dialysis): {scipy.stats.mannwhitneyu(moca_pf_J1, moca_pf_J2)}")




