from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup
from pprint import pprint
from datetime import datetime

if __name__ == "__main__":
    print()
    print("Create NAPALM connections to cisco3 and arista1")
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    print()
    for conn in connections:
        print("Stage candidate config for:" + conn.hostname)
        config = conn.hostname + "-loopbacks.conf"
        conn.load_merge_candidate(filename=config)
        
        print("---Pre Change Diff: " + conn.hostname)
        print(conn.compare_config())
        print("---End Pre Change Diff: " + conn.hostname)
        
        print("Commit the pending changes")
        conn.commit_config()
        
        print("---Post Change Diff: " + conn.hostname)
        print(conn.compare_config())
        print("---End Post Change Diff: " + conn.hostname)
        print("\n\n")

