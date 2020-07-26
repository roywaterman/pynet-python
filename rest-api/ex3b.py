iiport os
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

    for device in response["results"]:
        location = device["site"]["name"]
        vendor = device["device_type"]["manufacturer"]["name"]
        status = device["status"]["label"]
        print()
        print("-" * 20)
        print(device["display_name"])
        print("-" * 20)
        print(f"Location: {location}")
        print(f"Vendor: {vendor}")
        print(f"Status: {status}")
        print("-" * 20)
        print()
