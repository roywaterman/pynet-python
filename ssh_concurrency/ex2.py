"""
This Python script evaluates the total time taken to execute "show version" on 4 network devices:
- 1 Cisco IOS device
- 2 Arista EOS devices
- 1 Juniper SRX device

It uses Netmiko & the SSH concurrency option 'threads' (considered legacy; processes is preferred)
Without using SSH concurrency the approx time taken is 60 secs
SSH concurrency reduces this time to under 25 secs
"""

import threading
from datetime import datetime
from my_devices import device_list
from my_functions import ssh_command


def main():
    command = "show version"
    start_time = datetime.now()

    for device in device_list:
        my_thread = threading.Thread(target=ssh_command, args=(device, command))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    end_time = datetime.now()
    print(f"\nTotal execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()
