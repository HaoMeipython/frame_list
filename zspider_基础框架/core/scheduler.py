from six.moves.queue import Queue

class Scheduler():
    '''完成调取器模块的封装'''
    def __init__(self):
        self.queue=Queue()

    def add_request(self,request):
        '''
        实现添加request到队列中
        :param request: 请求对象
        :return: None
        '''
        # url去重
        # self._filter_request(request)
        self.queue.put(request)

    def get_request(self):
        '''
        实现获取队列中的request对象
        :return: 请求对象
        '''
        return self.queue.get()

    def _filter_request(self,request):
        '''
        实现对请求对象的去重
        :param request: 请求对象
        :return: bool
        '''
        pass