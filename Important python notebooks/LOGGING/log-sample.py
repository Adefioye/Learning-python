# Getting acquainted with the basics of logging
import logging 
import employee 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("Time: %(asctime)s, Name of logger: %(name)s, Logging level: %(levelname)s, message: %(message)s")
file_handler = logging.FileHandler("sample.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# If we wanna make errors and messages appear on the console, we use the stream handler
# It is important to note that usually, stream handler prints out only the "message" content without
# considering the format provided to the file handler. If we wanrt the same format, we should add the
# formatter to the stream handler.
stream_handler = logging.StreamHandler()
# We then add it to the logger
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)

def add(x, y):
    "Add function"
    return x + y 

def subtract(x, y):
    "Subtract function"
    return x - y

def multiply(x, y):
    "Multiply function"
    return x * y 

def divide(x, y):
    "Divide function"
    try:
        result = x / y 
    except ZeroDivisionError:
        logger.exception("Tried dividing by zero")
    else:
        return result

# There are 5 logging levels. The default being "WARNING". In order to use other logging levels, we would
# have to explicitly set it under the basicConfig function.

# The below code is used to print out messages usin the DEBUG level while outputing the logs to
# logfile.txt

# logging.basicConfig(filename="sample.log", level=logging.DEBUG, 
#                   format="Time: %(asctime)s, Name of logger: %(name)s, Logging level: %(levelname)s, message: %(message)s")

num_1 = 20
num_2 = 5

add_result = add(num_1, num_2)
logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logger.debug("Subtract: {} - {} = {}".format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1, num_2)
logger.debug("Multiply: {} * {} = {}".format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
logger.debug("Divide: {} / {} = {}".format(num_1, num_2, divide_result))
