import logging


class Logger:


    def __init__(self, name, log_level="ERROR") -> None:
        self.logger=logging.getLogger(name)
        level_setter = self.levels.get(log_level)
        
        if level_setter:
            level_setter()
        
        formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file_handler=logging.FileHandler('test.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
    def print(self, *args, **kwargs):
        self.get_logger().info(*args, **kwargs)

    def get_logger(self):
        return self.logger
    
    @property
    def levels(self):
        return  {
        "ERROR": self.logger.setLevel(logging.ERROR),
        "DEBUG": self.logger.setLevel(logging.DEBUG)
    }