import xlrd

xls = xlrd.open_workbook_xls('./grls2021-12-11-1.xls')
table = xls.sheet_by_name('Действующий')
print("Worksheet name(s): {0}".format(xls.sheet_names()))




def select_all_from_sheet(excel_sheet):
    tuples = []
    length = excel_sheet.nrows
    indexes = list(range(length))[12:]
    for index in indexes:
        row = (excel_sheet.row_values(index))
        tuples.append((row[9], row[10],))
    return tuples 
