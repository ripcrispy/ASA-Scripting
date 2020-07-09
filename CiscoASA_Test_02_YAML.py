import time
import yaml
import getpass
from netmiko import ConnectHandler

asaUser = input('Username: ')
asaPass = getpass.getpass()
devType = 'cisco_asa'

with open(r'hosts.yaml') as file:
    hostList = yaml.full_load(file)
    hostList = hostList['host_ip']

    for ip_addr in hostList:
        print("Connecting to: " + ip_addr)
        device = ConnectHandler(device_type=devType, ip=ip_addr, username=asaUser, password=asaPass)

        print("Gathering configuration...")
        sendCommand = device.send_command("more system:running-config")

        currentDate = time.strftime('%d-%b-%Y_%H-%M')
        fileName = ip_addr + "_" + currentDate + ".txt"
        print("Saving to file: " + fileName + "\n")
        
        f = open(fileName, 'w')
        print(sendCommand, file=f)
        
        device.disconnect()

print("Backup completed!")