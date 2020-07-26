import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


cisco3 = {
    "host": "<device FQDN>",
    "device_type": "cisco_ios",
    "username": username,
    "password": password
}

arista1 = {
    "host": "<device FQDN>",
    "device_type": "arista_eos",
    "username": username,
    "password": password,
    "global_delay_factor": 4
}

arista2 = {
    "host": "<device FQDN>",
    "device_type": "arista_eos",
    "username": username,
    "password": password,
    "global_delay_factor": 4
}

srx2 = {
    "host": "<device FQDN>",
    "device_type": "juniper_junos",
    "username": username,
    "password": password,
}    


device_list = [cisco3, arista1, arista2, srx2]

