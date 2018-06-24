from .downloader import Downloader
from .pipeline import Pipeline
from .scheduler import Scheduler
from .spider import Spider
from zspider.http.request import Request
from datetime import datetime
from zspider.utils.log import logger
from zspider.middlewares.downloadermiddlewares import Downloadermiddleware
from zspider.middlewares.spidermiddlewares import Spidermiddleware



class Engine():
    def __init__(self):
        self.downloader=Downloader()
        self.pipeline =Pipeline()
        self.scheduler= Scheduler()
        self.spider=Spider()
        self.spidermiddleware=Spidermiddleware()
        self.downloadermiddleware= Downloadermiddleware()

    def start_engine(self):

        '''
        提供引擎启动的入口
        :return:
        '''
        start_time = datetime.now()
        logger.info("爬虫启动：{}".format(start_time))
        self._start_engine()
        end_time = datetime.now()
        logger.info("爬虫结束：{}".format(start_time))
        logger.info("爬虫一共运行：{}秒".format((end_time - start_time).total_seconds()))

        pass

    def _start_engine(self):
        # 1.构造spider中start_urls中的请求
        # 2.传递给调取器进行保存，之后从中取出
        # 3.取出的request对象交给下载的进行下载，返回response
        # 4.response交给爬虫模块进行解析，提取结果
        # 5.如果结果是request对象，重新交给调度器，如果结果是item对象，交给管道处理

        # 1.构造spider中start_urls中的请求
        request=self.spider.start_request()
        # 2.传递给调取器进行保存，之后从中取出
        self.scheduler.add_request(request)


        req=self.scheduler.get_request()
        # 3.取出的request对象交给下载的进行下载，返回response
        response=self.downloader.get_response(req)
        # 4.response交给爬虫模块进行解析，提取结果
        ret=self.spider.parse(response)
        # 5.如果结果是request对象，重新交给调度器，如果结果是item对象，交给管道处理
        if isinstance(ret,Request):
            self.scheduler.add_request(ret)
        else:
            self.pipeline.process_item(ret,self.spider)

