
import os

if __name__ == '__main__':
    os.system('echo "alias tool_tv=\'python3 time_utils.py\'" >> ~/.zshrc')
    os.system('echo "alias tool_ct=\'python3 current_time.py\'" >> ~/.zshrc')
    os.system('echo "alias tool_my_ip=\'python3 get_ip.py\'" >> ~/.zshrc')
    os.system('echo "alias tool_kpid=\'python3 kill_process_by_pid.py\'" >> ~/.zshrc')
    os.system('echo "alias tool_kport=\'python3 kill_process_by_port.py\'" >> ~/.zshrc')
    os.system('echo "alias tool_format=\'python3 json_format.py\'" >> ~/.zshrc')
    