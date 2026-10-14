
# Configuration du VLAN invite
/interface vlan add name=vlan-guest vlan-id=20 interface=ether2
/ip address add address=192.168.20.1/24 interface=vlan-guest
