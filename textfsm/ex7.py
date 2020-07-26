from pprint import pprint
import textfsm

template_file = "ex2.template"
template = open(template_file)

with open("ex1_show_int_status.txt") as f:
    raw_text_data = f.read()


# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

key = re_table.header
new_list = []

for row in data:
    new_entry = {key[0]: row[0], key[1]: row[1], key[2]: row[2], key[3]: row[3], key[4]: row[4], key[5]: row[5]}
    new_list.append(new_entry)

print()
pprint(new_list)
print()



