"""
This Python script evaluates the total time taken to execute "show version" on 4 network devices:
- 1 Cisco IOS device
- 2 Arista EOS devices
- 1 Juniper SRX device

It uses Netmiko & the "ProcessPoolExecutor" in Concurrent Futures
"""

from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from my_devices import device_list
from my_functions import ssh_command2 as ssh_conn

def main():
    command = "show ip arp"
    command_junos = "show arp"
    start_time = datetime.now()
    max_procs = 4
 
    # Use context manager to gracefully cleanup the pool
    with ProcessPoolExecutor(max_procs) as pool:

        cmd_list = []
        for device in device_list:
            if "junos" in device["device_type"]:
                cmd_list.append("show arp")
            else:
                cmd_list.append("show ip arp")
                        
        results_generator = pool.map(ssh_conn, device_list, cmd_list)

        for result in results_generator:
            print("#" * 20)
            print(result)
            print("#" * 20)
        end_time = datetime.now()
        print(f"\nTotal execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()
