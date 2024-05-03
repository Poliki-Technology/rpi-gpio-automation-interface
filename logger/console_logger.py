from logger.i_logger import ILogger
import time

class ConsoleLogger(ILogger):
  def log(self, message: str):
    print(f"{time.strftime('%x %X %Z')}: {message}")
    return
