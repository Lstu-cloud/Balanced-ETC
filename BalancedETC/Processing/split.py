import csv
result = []
linecount = 0

import os

from scapy.all import *
from scapy.layers.inet import IP, UDP, TCP
from collections import defaultdict

from scapy.plist import PacketList


filepath = r'C:\Processing_classification\Processing_classification\Processing_classification\testpcaps\Torrent'


def read(filepath,n):
    files = os.listdir(filepath)

    for el in files:
        fp = os.path.join(filepath, el)
        if os.path.isdir(fp):
            print("\t" * n, el)
            read(fp, 1 + 1)
        else:
            print("\t" * 1, el)

        with open(fp, "r", encoding='utf8', newline='') as f:
            # total = len(f.readlines())
            reader = csv.reader(f)

            file_path1 = fp
            # file_path2 = r'E:\ProjectFP\ProjectFP\FlowPic-main\TrafficParser\aaa516\1iscx_chat_raw.csv'
            file_path2 ='2' + el

            def _load_pcap(file_name: str) -> PacketList:
                pkts = rdpcap(file_name)
                return pkts

            def _filename_gen(t: tuple):
                proto = "UNKNOWN"
                if t[0] == 6:
                    proto = "TCP"
                if t[0] == 17:
                    proto = "UDP"
                return f"{proto}_{t[1]}_{t[3]}_{t[2]}_{t[4]}"

            def process(packets: PacketList):
                five_tuple_classified = defaultdict(list)
                for pkt in packets:
                    ip_layer = pkt[IP]
                    if TCP in pkt:
                        transmission_layer = pkt[TCP]
                    elif UDP in pkt:
                        transmission_layer = pkt[UDP]
                    else:
                        continue
                    key = (
                    ip_layer.proto, ip_layer.src, ip_layer.dst, transmission_layer.sport, transmission_layer.dport)
                    five_tuple_classified[key].append(pkt)

                for key, value in five_tuple_classified.items():
                    print(key, value)
                    wrpcap(f"split_output/{_filename_gen(key)}.pcap", value)

            # path = "./facebook_audio1a.pcap"
            path = fp
            pkts = _load_pcap(path)
            process(pkts)

read(filepath, 0)



