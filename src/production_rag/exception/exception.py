class MyException(Exception):
    def __init__(self,message:str, error:Exception):
        traceback = error.__traceback__
        self.orignal_error = error
        if traceback is not None:
            self.filename = traceback.tb_frame.f_code.co_filename
            self.function_name = traceback.tb_frame.f_code.co_name
            self.line_no = traceback.tb_lineno
        else:
            self.filename = "Unknown"
            self.function_name = "Unknown"
            self.line_no = "Unknown"

        error_message = (
            f"Message:{message}\n"
            f"{type(error).__name__}:{error}\n"
            f"File Name:{self.filename}\n"
            f"Function:{self.function_name}\n"
            f"Line Number:{self.line_no}"

        ) 
        super().__init__(error_message)