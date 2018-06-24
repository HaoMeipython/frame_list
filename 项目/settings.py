# coding=utf-8
import logging

DEFAULT_LOG_LEVEL = logging.DEBUG    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = '日志.log'    # 默认日志文件名称

# SPIDERS = [
#     "spider.baidu.BaiduSpider",
#     "spider.douban.DoubanSpider"
# ]
#
# PIPELINES = [
#     'pipelines.BaiduPipeline',
#     'pipelines.DoubanPipeline'
# ]
#
# SPIDER_MIDDLEWARES = []
# DOWNLOADER_MIDDLEWARES = []