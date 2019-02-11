import xlrd
loc = "/home/sarath/Documents/sarath/qb/projects/pradhidwani/license-management/dj_soundLicence/violation/fixtures/initial_data.xlsx"
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
