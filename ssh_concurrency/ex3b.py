"""
This Python script evaluates the total time taken to execute "show version" on 4 network devices:
- 1 Cisco IOS device
- 2 Arista EOS devices
- 1 Juniper SRX device

It uses Netmiko & the "ThreadPoolExecutor" in Concurrent Futures
"""

from concurrent.futures import ThreadPoolExecutor, as_completed # no longer importing wait timer
from datetime import datetime
from my_devices import device_list
from my_functions import ssh_command2 as ssh_conn


def main():
    command = "show version"
    start_time = datetime.now()
    max_threads = 4
   
    pool = ThreadPoolExecutor(max_threads)
 
    future_list = []
    for device in device_list:
        future = pool.submit(ssh_conn, device, command)
        future_list.append(future)

    # Process as completed, whichever result is the fastest
    for future in as_completed(future_list):
        print("#" * 30)
        print("Result: " + future.result())
        end_time = datetime.now()
        print(f"\nExecution time for result: {end_time - start_time}")

    end_time = datetime.now()
    print(f"\nTotal execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()
