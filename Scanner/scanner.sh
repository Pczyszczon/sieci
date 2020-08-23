#!/bin/bash
#Autor: Paweł Czyszczoń
#email: 290425@uwr.edu.pl

# ip1=($(seq -f "156.17.88.%g" 1 254))
# for ip in ${!ip1[@]};
# do  
#     echo ${ip1[$ip]}
#     # nmap -p 80 ${ip1[$ip]} | grep '80/open' | awk '{print $3 $2 $5}';
#     nc -z -v ${ip1[$ip]} 80
# done

nmap -p80 -oG - 156.17.88.0/24 | grep '80/open'
