from netmiko import ConnectHandler


def ssh_command(device, command):
    """Execute show version command using Netmiko."""
    print()
    print("### START OF COMMAND OUTPUT ###")
    remote_conn = ConnectHandler(**device)
    output = remote_conn.send_command(command)
    remote_conn.disconnect()
    print(output)
    print("### END OF COMMAND OUTPUT ###")
    print()

def ssh_command2(device, command):
    """Execute show version command using Netmiko."""
    remote_conn = ConnectHandler(**device)
    output = remote_conn.send_command(command)
    remote_conn.disconnect()
    return output
