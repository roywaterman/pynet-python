from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup
from pprint import pprint
from datetime import datetime

if __name__ == "__main__":
# Exercise 2a - Create a list of connection objects
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

# Exercise 2b - Pretty print the arp table for each of these devices
    print("\n\n")
    str = "Print ARP table & NTP peers for all devices in connections list"
    print(str)
    print("-" * len(str))
    for conn in connections:
        print()
        print("-" * 6)
        pprint("ARP table of: {}".format(conn.hostname))
        print("-" * 30)
        pprint(conn.get_arp_table())
        print("-" * 6)
        print("\n\n")

# Exercise 2c - Use the get_ntp_peers() method against both of the devices
        try:
            pprint("NTP peers of: {}".format(conn.hostname))
            print("-" * 30)
            pprint(conn.get_ntp_peers())
        except NotImplementedError:
            print("get_ntp_peers is not supported on: {}".format(conn.platform))
            print()
    
# Exercise 2d - Backup running config to separate files (I'm attaching current date & time to the filenames)
        # dd/mm/YY H:M:S
        now = datetime.utcnow()
        dt_string = now.strftime("%d%m%Y_%H%M%S")        
        
        filename = conn.hostname + "." + dt_string + ".txt"
        config = create_backup(conn)
        running_config = config['running']
        
        with open(filename, "w") as f:
            f.write(running_config) 
            f.close()




