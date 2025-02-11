"""This is using open_workbook, because it is only for opening existed excel"""
# !/usr/bin/env python
# encoding=UTF-8

import xlrd
import os


def read_excel_row(file, row, sheet_id):    # read just one row
    book = xlrd.open_workbook(file, 'r')     # open_workbook is for already existed excel file
    sheet = book.sheet_by_index(sheet_id)
    print(sheet.row_values(row))
    return sheet.row_values(row)


def read_excel_rows(file, sheet_id):      # read all rows
    rows = []
    book = xlrd.open_workbook(file, 'r')
    sheet = book.sheet_by_index(sheet_id)
    for row in range(1, sheet.nrows):        # get values in each row, start from row 1
        rows.append(sheet.row_values(row, 0, sheet.ncols))     # row_values(self, rowx, start_colx=0, end_colx=None)
    # print(rows)
    return rows


def read_excel_col(file, col, sheet_id):     # read data in specific column
    book = xlrd.open_workbook(file, 'r')     # open_workbook is for already existed excel file
    sheet = book.sheet_by_index(sheet_id)
    print(sheet.col_values(col))
    return sheet.col_values(col)


def read_excel_cols(file, sheet_id):       # read data in all columns
    cols = []
    book = xlrd.open_workbook(file, 'r')
    sheet = book.sheet_by_index(sheet_id)
    for col in range(0, sheet.ncols):                # get values in each column
        cols.append(sheet.col_values(col, 0, sheet.nrows))      # col_values(self, colx, start_rowx=0, end_rowx=None)
    # print(cols)
    return cols


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_path = root_dir + r'\data\test.xls'   # this is for windows
    file_path = root_dir + '/data/test.xls'    # this is for linux and mac
    # print(file_path)
    # read_excel_row(file_path, 1, 0)
    # read_excel_row(file_path, 0)     # [['', '', '请输入邮箱名'], ['wuya', 'admin', '您输入的邮箱名格式不正确']]
    read_excel_col(file_path, 1, 0)
    read_excel_cols(file_path, 0)
