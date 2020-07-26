from my_devices import network_devices
from my_functions import open_napalm_connection, create_checkpoint
from pprint import pprint

if __name__ == "__main__":
    print()
    print("Create NAPALM connections to cisco3 and arista1")
    for device in network_devices:
        conn = open_napalm_connection(device)

    print()
    print("Exercise 4a/b - Create checkpoint file")
    create_checkpoint(conn)

    print()
    print("Exercise 4c/d - Add loopback to checkpoint file/stage new config/compare/discard/compare")
    conn.load_replace_candidate(filename="nxos1-rw.txt")
    print("Start diff")
    print(conn.compare_config())
    print("End diff")

    print()
    print("Discard config")
    conn.discard_config()
    print("Start diff")
    print(conn.compare_config())
    print("End diff")
