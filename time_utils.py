import time
import pyperclip
import datetime
import sys



def timestamp_to_str(timestamp_ms):
    # Convert timestamp to datetime object
    dt = datetime.datetime.fromtimestamp(timestamp_ms / 1000)
    # Convert datetime object to string
    dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return dt_str

def datetime_to_timestamp(dt_str):
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # Convert datetime object to timestamp in milliseconds
    timestamp = int(time.mktime(dt.timetuple()) * 1000)
    return timestamp

if __name__ == '__main__':
    # Get the clipboard content
    # clipboard_content = pyperclip.paste()
    arg = " ".join(sys.argv[1:])

    contain_space = " " in arg

    if contain_space:
        # Convert datetime string to timestamp
        timestamp = str(datetime_to_timestamp(arg))
        # Copy the timestamp to clipboard
        pyperclip.copy(timestamp)
        print("result: " + timestamp + "\n")
    else:
        # Convert timestamp to datetime string
        dt_str = timestamp_to_str(int(arg))
        # Copy the datetime string to clipboard
        pyperclip.copy(dt_str)
        print("result: " + dt_str + "\n")