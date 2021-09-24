from scapy.all import *

router_mac="84:d4:7e:f2:33:01"
filename='rssi.txt'

file_object = open('rssi.txt', 'w')
to_write=""
file_object.write(to_write)
file_object.close(  )
missed_count=0


def method_filter_HTTP(pkt):
    global missed_count
    cur_dict={}

    cur_dict['mac_1']  =pkt.addr1
    cur_dict['mac_2']  =pkt.addr2
    cur_dict['rssi'] = pkt.dBm_AntSignal
    # print(cur_dict)



    if cur_dict['mac_1'] == router_mac or cur_dict['mac_2']==router_mac:
        # print(pkt.show())
        file_object = open('rssi.txt', 'a')
        print(cur_dict,"\t Missed:",missed_count)
        try:
            to_write=cur_dict['mac_1']+","+cur_dict['mac_2']+","+str(cur_dict['rssi'])+"\n"
            file_object.write(to_write)
            file_object.close(  )
        except Exception as e:
            print(e,missed_count)
            # print(pkt.show2())
            # ()+1
            missed_count+=1
    return 0

sniff(iface="mon0",prn=method_filter_HTTP,store=0)

