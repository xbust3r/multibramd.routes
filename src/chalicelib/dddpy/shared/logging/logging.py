import logging

class Logger:
    
    def __init__(self, logger_name):
        self.logger_name = logger_name
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(self.logger_name)
    
    def log(self, level, data):
        log_function = getattr(self.logger, level)
        return log_function(data)
    
    def info(self, data):
        return self.log('info', data)
    
    def debug(self, data):
        return self.log('debug', data)
    
    def warning(self, data):
        return self.log('warning', data)
    
    def error(self, data):
        return self.log('error', data)
    
    def critical(self, data):
        return self.log('critical', data)
