# Firewall rules - exemple de laboratoire

/ip firewall filter
add chain=input action=accept connection-state=established,related comment="Allow established connections"
add chain=input action=drop connection-state=invalid comment="Drop invalid connections"
add chain=input action=accept protocol=icmp comment="Allow ICMP for testing"
add chain=input action=drop protocol=tcp dst-port=23 comment="Block Telnet access"
