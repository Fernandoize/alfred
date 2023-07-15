import os
import signal
import sys

def main():
    process_id = int(sys.argv[1])

    print("Killing process with ID: {}".format(process_id))
    # Kill the process using the process ID
    os.kill(process_id, signal.SIGKILL)

if __name__ == '__main__':
    main()