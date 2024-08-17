import sys # Any exceptions that is basically getting controlled this sys library will automatically have the information
from src.logger import logging

def error_message_detail(error, error_detail:sys): # push my error message
    _,_,exc_tb=error_detail.exc_info() # which file and which line exception occured
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error=error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
