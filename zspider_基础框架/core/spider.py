
from zspider.http.request import Request
from zspider.item import Item

class Spider():
    '''完成对spider的封装'''
    start_url = "http://www.baidu.com"  # 爬虫最开启请求的url地址
    def start_request(self):

        '''
        构造start_url地址的请求
        :return: request
        '''
        return Request(self.start_url)

    def parse(self,response):
        '''
        默认处理start_url地址对应的响应
        :param response: response对象
        :return: item或者是request
        '''
        return Item(response.body)