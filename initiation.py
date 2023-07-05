import os
import sys

host_name = sys.argv[1]
ip = sys.argv[2]
os.system(f'echo "{host_name}" > /etc/hostname')
strx = "127.0.0.1 localhost \n" \
       f"127.0.1.1 {host_name} \n" \
       "::1     ip6-localhost ip6-loopback \n" \
       "fe00::0 ip6-localnet \n" \
       "ff00::0 ip6-mcastprefix \n" \
       "ff02::1 ip6-allnodes \n" \
       "ff02::2 ip6-allrouters \n"
os.system(f'echo "{strx}" > /etc/hosts ')
import yaml

file = open("netplan.yaml", 'r')
netplan = yaml.safe_load(file)
netplan['network']['ethernets']['ens3']['addresses'] = [f'{ip}/24']
netplan_file_name = os.popen("ls /etc/netplan/").read().replace("\n","")
file = open(f"/etc/netplan/{netplan_file_name}", "w")
yaml.dump(netplan, file)
file.close()
os.system("netplan try")
os.system("netplan apply")
