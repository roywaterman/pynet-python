import requests # this is the default way of interfacing to REST APIs in Python (needs to be installed with pip (pip install requests)
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning # make SSL certificate warning go away (device has unsigned certificate)

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    # Working no auth
    url = "<redacted>"
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    response = requests.get(url, headers=http_headers, verify=False) # verify=False - don't worry about SSL certificate not being validated
    print("#" * 20)    
    pprint(f"response.status_code: {response.status_code}")
    print("#" * 20)
    pprint(f"response.text: {response.text}")
    print("#" * 20)
    pprint(f"response.json(): {response.json()}")
    print("#" * 20)
    pprint(f"response.headers: {response.headers}")

