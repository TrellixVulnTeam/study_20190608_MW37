# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/1  15:21
# 文件名称   ：bilibili_video.py
# 开发工具   ：PyCharm

import requests  # 网络请求模块
import time      # 时间模块
import random    # 随机模块
import os        # 操作系统模块
import re        # 正则表达式

# 哔哩哔哩小视频json地址
json_url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={page}1&tag=今日热门&platform=pc'
class Crawl():
    def __init__(self):
        # 创建头部信息
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

    def get_jsonurl(self,json_url):
        response = requests.get(json_url, headers=self.headers)
        # 判断请求是否成功
        if response.status_code == 200:
            return response.json()  # 返回json信息
        else:
            print('获取json信息的请求没有成功！')

    def download_video(self,video_url,titlename):
        size = 0     # 记录叠加每次写入大小的变量
        # 下载视频的网络请求
        response = requests.get(video_url, headers=self.headers, stream=True)
        content_size = int(response.headers['content-length'])  # 视频内容的总大小
        chunk_size = 1024  # 单次请求最大值
        if not os.path.exists('video'):  # 如果video目录不存在时
            os.mkdir('video')             # 创建该目录
        if response.status_code == 200:   # 判断请求是否成功
            if os.path.exists('video'):
                print('视频文件大小：%0.2fMB' % (content_size / chunk_size / 1024))  # 换算单位，并打印文件大小
                with open('video/'+titlename+'.mp4', 'wb')as f:                     # 将视频写入指定位置
                    for data in response.iter_content(chunk_size=chunk_size):       # 循环写入，实现一段一段的写
                        f.write(data)                                                # 写入视频文件
                        f.flush()                                                    # 刷新缓存
                        size += len(data)                                            # 叠加每次写入的大小
                        # 打印下载进度
                        print('\r 文件下载进度:%d%%(%d/%d)'%
                              (float(size / content_size * 100),size,content_size), end=" ")
        else:
            print('视频下载失败！')

if __name__ == '__main__':
    c = Crawl()
    ranking = 0                                           # 排名变量
    for page in range(0,10):
        json = c.get_jsonurl(json_url.format(page=page))  # 获取返回的json数据
        infos=json['data']['items']                       # 信息集
        for info in infos:                               # 遍历信息
            ranking+=1                                    # 叠加排名
            print('\n正在下载排名第',ranking,'的视频')
            title = info['item']['description']        # 视频标题
            # 只保留标题中英文、数字与汉字，其它符号会影响写入文件
            comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
            title = comp.sub('',title )                # 将不符合条件的符号替换为空
            video_url = info['item']['video_playurl']  # 视频地址
            c.download_video(video_url,title)          # 下载视频,视频标题作为视频的名字
        time.sleep(random.randint(3,6))                     # 随机产生获取json请求的间隔时间
