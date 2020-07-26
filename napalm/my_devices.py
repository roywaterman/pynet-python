import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


cisco3 = {
    "hostname": "<device FQDN>",
    "device_type": "ios",
    "username": username,
    "password": password
}

arista1 = {
    "hostname": "<device FQDN>",
    "device_type": "eos",
    "username": username,
    "password": password
}

nxos1 = {
    "hostname": "<device FQDN>",
    "device_type": "nxos",
    "username": username,
    "password": password,
    "optional_args": {"port": 8443}
}    


network_devices = [nxos1]

