import pyperclip
import datetime

def main():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("result: {}".format(current_time))
    pyperclip.copy(current_time)



if __name__ == '__main__':
    main()