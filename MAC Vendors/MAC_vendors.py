#Autor: Paweł Czyszczoń
#email: 290425@uwr.edu.pl

import requests
from time import sleep
from collections import defaultdict 

ENDPOINT_TEMPLATE = 'https://api.macvendors.com/{}'
summary_dict = defaultdict(int)

mac_list = open("lista_mac.txt", "r")

answer_file = open("vendors_list.txt", "a")
answer_file.write("#Autor: Paweł Czyszczoń\n#email: 290425@uwr.edu.pl\n\n1. LIST\n")

for MAC in mac_list:
    request = requests.get(ENDPOINT_TEMPLATE.format(MAC.strip()))
    answer_file.write("{} - {}\n".format(MAC.strip(), request.text))
    answer_file.flush()
    summary_dict[request.text] += 1
    sleep(1)

mac_list.close()

answer_file.write("\n2. SUMMARY \n\n")
for vendor, number in summary_dict.items():
    answer_file.write('{}: {}\n'.format(vendor, number))
    answer_file.flush()

answer_file.close()
