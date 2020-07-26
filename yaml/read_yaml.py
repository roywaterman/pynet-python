"""
Create a simple program to prompt the user to enter the name of a yaml file
The yaml file in question will be read into Python & printed to stdout
Example of a yaml file:

$ cat dict1.yaml
---
key1: value1
key2: value2
key3: value3
"""

import yaml

filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)
