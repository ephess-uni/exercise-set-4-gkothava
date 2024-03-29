""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    total_events = get_shutdown_events(logfile)
    shut_events1 = total_events[0]
    shut_events2 = total_events[-1]
    shut_events1_date_a= logstamp_to_datetime(shut_events1.split()[1])
    shut_events2_date_b = logstamp_to_datetime(shut_events2.split()[1])
    return shut_events2_date_b-shut_events1_date_a


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
