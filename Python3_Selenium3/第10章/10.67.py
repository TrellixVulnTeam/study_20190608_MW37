#coding=utf-8
import  xlrd

# excelֵ��װ�����ؾ���һ���ֵ�
#����������Ҫ�޸���
# demo���ݷ���[{'username': 'tim1', 'passwd': 'TimTest'}, {'username': 'tim2', 'passwd': 'TimTest'}, {'username': 'tim3', 'passwd': 'TimTest'}]

def get_data(filename, sheetnum):
    path = 'testdata.xlsx'
    book_data = xlrd.open_workbook(path)
    book_sheet = book_data.sheet_by_index(1)  # ���ļ����е�һ����
    rows_num = book_sheet.nrows  # ����
    rows0 = book_sheet.row_values(0)  # ��һ�еĸ���������Ϊ�ֵ�ļ�
    rows0_num = len(rows0)  # �������֪���м���
    list = []

    for i in range(1, rows_num):
        rows_data = book_sheet.row_values(i)  # ȡÿһ�е�ֵ��Ϊ�б�
        rows_dir = {}
        for y in range(0, rows0_num):  # ��ÿһ�е�ֵ��ÿһ�ж�Ӧ����
            rows_dir[rows0[y]] = rows_data[y]
        list.append(rows_dir)
    return list


if __name__ == '__main__':
    print(get_data('', 1))
