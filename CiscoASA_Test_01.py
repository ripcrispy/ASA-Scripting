import time
from netmiko import ConnectHandler

print("Connecting to device...\n")

device = ConnectHandler(
    device_type='cisco_asa', 
    ip='A.B.C.D',
    username='nope', 
    password='nope'
    )

print("Gathering ACL policies...\n")
output = device.send_command("sh run access-list")

currentDate = time.strftime('%d-%b-%Y_%H-%M')
fileName = "logging-" + currentDate + ".txt"
print("Saving to file: " + fileName + "...\n")
f = open(fileName, 'w')
print(output, file=f)

device.disconnect()
print("Complete, disconnected from device...\n")