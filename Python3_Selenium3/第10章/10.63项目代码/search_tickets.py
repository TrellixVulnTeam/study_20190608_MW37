'''
��ҳ����Ϊ�˲��Ի�Ʊ��ѯ��ҳ��Ԫ�صĹ��ܡ�
'''
from functions import date_n,id,css,xpath,js,return_driver,open_base_site,click_blank
import time

'''
�������� search_tickets
������
 from_station: ����վ
 to_station: ����վ
 n�� ��һ�����֣���1��ʾѡ������ĳ�Ʊ��2��ʾѡ�����ĳ�Ʊ��
'''
def search_tickets(from_station,to_station,n):
    #driver =return_driver()
    open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    #from_station = "�Ϻ�"
    from_station = from_station
    #to_station = "����"
    to_station = to_station

    #����Ϊtomorrow����
    tomorrow = date_n(n)

    #����Ϊ��λ�������к͵�����е�ҳ��Ԫ�أ�����������ֵΪ���϶���ֵ��
    id("notice01").send_keys(from_station)
    id("notice08").send_keys(to_station)

    #���´���Ϊ�Ƴ�����ʱ���'readonly'���ԡ�
    js("dateObj")
    time.sleep(2)
    #�������ʱ���Ĭ�����ݡ�
    id("dateObj").clear()
    time.sleep(2)
    #����Ϊ���������������ڡ�
    id("dateObj").send_keys(tomorrow)

    #���²�����Ϊ�˽�����ڿؼ����������������ں��޷���ʧ�����⣬�Ӷ�Ӱ����ԵĽ��С�
    #ԭ����Ϊ�������������ҳ��հ״���

    #ActionChains(driver).move_by_offset(0,0).click().perform()
    click_blank()

    #����Ϊ�������������ť
    id("searchbtn").click()
