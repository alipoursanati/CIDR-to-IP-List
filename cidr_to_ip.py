#By Ali Rajabpour-Sanati
import os
import ipaddress

def cidr_to_ips(cidr):
    ips = []
    for ip in ipaddress.IPv4Network(cidr):
        ips.append(str(ip))
    return ips

def save_to_file(ips, filepath):
    with open(filepath, 'a') as f:
        for ip in ips:
            f.write(ip + '\n')

def read_cidr_file(cidr_file):
    with open(cidr_file) as file:
        cidrs = file.read().splitlines()
    return cidrs

cidr_file = 'cidrs.txt'
cidrs = read_cidr_file(cidr_file)

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, 'results.txt')

for cidr in cidrs:
    ips = cidr_to_ips(cidr)
    save_to_file(ips, filepath)

print(f'IP addresses from {cidrs} saved to {filepath}')
