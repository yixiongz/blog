from django.test import TestCase

# Create your tests here.


iplist = ["114.114.114.114"]
commit = "ip pool dhcp-vlan"

for i in range(2,10):
    print(commit+str(i))
    for ip in iplist:
        print("undo dns-list",ip)
    print("dns-list","219.141.136.10")
    print("dns-list","114.114.114.114")
