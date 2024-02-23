""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    with open(logfile, 'r') as log_file:
        events = log_file.read()
    logs = events.splitlines()
    shutdowm_events_ = list()
    for ev in logs:
        if 'Shutdown initiated' in ev :
            shutdowm_events_.append(ev)
    return shutdowm_events_

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
