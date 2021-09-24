iw dev
sudo iw phy phy1 interface add mon0 type monitor
sudo iw dev wlan1 del
sudo ifconfig mon0 up
sudo iw dev mon0 set channel 1


# Steps 

# #: to be replaced by a number
# Command: "iw dev"
# Description: "Identify new added USB interface, should show 2 interfaces (old one and new one)"



# Command: "sudo iw phy phy# interface add mon0 type monitor"
# Description: "Add new monitor interface, replace phy1 with new interface phy number, it's either 0 or 1"

# Comamnd: "sudo iw dev wlan# del"
# Description: "Delete the wlan interface on phy#, replace # with actual number"

# Comamnd: "sudo ifconfig mon0 up"
# Description: "start the interface"

# Comamnd: "sudo iw dev mon0 set freq 2437"
# "sudo iw dev mon0 set channel 1"

# Description: "set to a frequency or channel"


# Comamnd: "sudo tcpdump -i mon0 -n -w wireless.pcap"
# Description: "Verify if it's successful"



