from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_command(device, command):
    """Execute show version command using Netmiko."""
    remote_conn = ConnectHandler(**device)
    output = remote_conn.send_command(command)
    remote_conn.disconnect()
    return output


def main():
    command = "show version"
    start_time = datetime.now()    
    for device in device_list:
        output = ssh_command(device, command)
        print(output)
        print("-" * 20)
        print()    
    end_time = datetime.now()

    print(f"\nTotal execution time: {end_time - start_time}")

if __name__ == "__main__":
    main()
