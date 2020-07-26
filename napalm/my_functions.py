from napalm import get_network_driver
from datetime import datetime

def open_napalm_connection(device):
    """Function to open napalm connection and return connection object"""
    # Copy dictionary to ensure original object is not modified
    device = device.copy()
    # Pop "platform" as this is an invalid kwarg to napalm
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn


def create_backup(conn):
    """Function thats takes a napalam connection object as argument and prints out running config"""
    # Get current datetime string in a format to be added to the backup config file
    # dd/mm/YY H:M:S
    now = datetime.utcnow() # get currrent datetime in UTC (datetime.now() gives US timezone)
    dt_string = now.strftime("%d%m%Y_%H%M%S") 

    # conn.get_config() returns a Python dictionary with running and startup as keys; we are just interested in running config
    backup = conn.get_config()
    running_config = backup['running']
    filename = conn.hostname + "." + dt_string + ".txt"

    with open(filename, "w") as f:
        f.write(running_config)

def create_checkpoint(conn):
    checkpoint = conn._get_checkpoint_file()
    filename = "{}-checkpoint.txt".format(conn.hostname)
   
    with open(filename, "w") as f:
        f.write(checkpoint) 
