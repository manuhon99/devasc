from netmiko import ConnectHandler
import desafioWebex
import os

from dotenv import load_dotenv, find_dotenv

# Load and get environment variables
load_dotenv(find_dotenv())
room_id = os.environ.get("ROOM_ID")


cisco1 = {
        "device_type": "cisco_ios",
        "host": "ios-xe-mgmt.cisco.com",
        "port": 8181,
        "username": "developer",
        "password": "C1sco12345",
    }   

command = "show interfaces"

def get_interfaces():
    with ConnectHandler(**cisco1) as net_connect:
        # Use TextFSM to retrieve structured data
        output = net_connect.send_command(command, use_textfsm=True)
   
    message = []
    for equip in output:
        interface = equip['interface']
        status = equip['link_status']
        text = f'A interface {interface} está em estado operacional {status}. \n'
        if equip:
            message.append(text)
    #POST message on webex room
    desafioWebex.post_message(room_id, message)         

def main():
    get_interfaces()

if __name__ == "__main__":
    main()
