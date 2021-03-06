#!/usr/bin/env python
import openpyxl as px


def main():
    """program entry point"""
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.get_sheet_by_name('US Presidents')

    print_first_and_last_names(ws)


def print_first_and_last_names(ws):
    """Print first and last names of all presidents"""
    pres_range = ws['B2':'J46']  # cell range
    for row in pres_range:  # row object
        # print(row[1].value, row[0].value)
        print(row[0].value, row[1].value, row[-1].value)

if __name__ == '__main__':
    main()
