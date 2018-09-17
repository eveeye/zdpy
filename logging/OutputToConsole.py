import logging

"""
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
"""

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
