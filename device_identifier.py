import nmap3
list_of_devices = []

class device_information:
    info_list = []
    def __init__(self, ip1 : str , mac1:str , manufacturer1:str):
        self.info_list = [ip1,mac1,manufacturer1]



nmap = nmap3.NmapHostDiscovery()
results = nmap.nmap_no_portscan("192.168.10.0/24")
number_of_devices = len(results)
print(results)
counter = 0
for item in results:
    if counter < number_of_devices - 1 : 
        dev = device_information(item,results[item]["macaddress"]["addr"],results[item]["macaddress"]["vendor"])
        list_of_devices.append(dev)
    
print(list_of_devices)
