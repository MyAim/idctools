from ..SRchemy import *
import threading

snmp = "123321cisco123456"
ip_list = ["10.193.2.11"
]

x =  connect(ip_list,"bob","123",snmp,[])

for i in x:
	print i.device_flag,'----------------',i.sysname


#"10.193.2.12",
#"10.193.2.13",
#"10.193.2.14",
#"10.193.2.15",
#"10.193.2.16",
#"10.193.2.17",
#"10.193.2.18",
#"10.193.2.19",
#"10.193.2.20",
#"10.193.2.21",
#"10.193.2.22",
#"10.193.2.23",
#"10.193.2.24",
#"10.193.2.25",
#"10.193.2.27",
#"10.193.2.28",
#"10.193.2.29",
#"10.193.2.30"


