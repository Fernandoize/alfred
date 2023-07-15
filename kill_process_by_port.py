import sys
import os
import signal

def main():
    # Get the port from the command line
    port = sys.argv[1]
    # Get the process ID using the specified port
    pid = os.popen(f"lsof -i :{port} -t").read().strip()

    pids = pid.split("\n")
    print("will kill process with pids:", pids, "and port:", port, "using SIGTERM")
    
    for pid in pids:
        # Kill the process using the process ID
        os.kill(int(pid), signal.SIGTERM)


if __name__ == '__main__':
    main()