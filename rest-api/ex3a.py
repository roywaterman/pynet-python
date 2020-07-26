import os
import requests
from pprint import pprint


from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]
    url = "<redacted>"
    http_headers = {"accept": "application/json; version=2.4;"}
    if token:
        http_headers["authorization"] = f"Token {token}"

    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    # reponse["results"] is a list of dictionary elements
    # we can obtain the hostname of each device by referencing the "display_name" key
    for device in response["results"]: 
        print(device["display_name"])


