def read_excel(filename, index, cloumn):
#��������xlrdģ���open��������Excel�ļ�
xls = xlrd.open_workbook(filename)
#����Ҫѡ��ı��
sheet = xls.sheet_by_index(index)
#��ӡѡ����������
print(sheet.nrows)
#��ӡѡ����������
print(sheet.ncols)
#����һ���յ��б�data
data = []
#������forѭ������Excel�еĵ�һ�е�����Ȼ�󽫱������뵽�б�data��
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i)[0])
        print(sheet.row_values(i)[0])
    #�����б�data
    return data	
