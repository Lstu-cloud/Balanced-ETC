import csv
result = []
linecount = 0

import os

from scapy.all import *

from scapy.all import *
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
import csv
import pathlib

filepath = r'C:\Processing_classification\Processing_classification\Processing_classification\split_output'


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

            def write_csv_from_list(l: list, file_name: str):
                with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    for row in l:
                        writer.writerow(row)
                csvfile.close()

            def cut_packet(pkt):
                data = raw(pkt)
                if len(pkt) < 100:
                    pad_len = 100 - len(pkt)
                    pad = Padding()
                    pad.load = '\x00' * pad_len
                    pkt = pkt / pad
                if len(pkt) > 100:
                    return Raw(data[:100])
                return pkt

            def process(path: str, is_output_pcap=False) -> list:
                ret = []
                pkts = rdpcap(path)
                i = 0
                for pkt in pkts:
                    # 只保留pair
                    # target_pair = None
                    # if UDP in pkt:
                    #     target_pair = UDP
                    # if TCP in pkt:
                    #     target_pair = TCP
                    # raw_data = pkt[target_pair].payload
                    # pkt = IP(raw(raw_data))
                    # print(pkt.summary())


                    if Ether in pkt:
                        pkt[Ether].src = '00:00:00:00:00:00'
                        pkt[Ether].dst = '00:00:00:00:00:00'
                    if IP in pkt:
                        pkt[IP].src = '0.0.0.0'
                        pkt[IP].dst = '0.0.0.0'

                    if UDP in pkt:
                        layer_after = pkt[UDP].payload.copy()
                        pad = Padding()
                        pad.load = '\x00' * 12
                        layer_before = pkt.copy()
                        layer_before[UDP].remove_payload()
                        pkt = layer_before / raw(pad) / layer_after

                    pkt = cut_packet(pkt)
                    raw_pkt = hexstr(pkt)
                    # raw_pkt = pkt.show(dump=True)
                    one_line_list = raw_pkt[:300].split(" ")[:-1]
                    ret.append(one_line_list)

                    # pathlib.Path(f'output/{filename}').mkdir(parents=True, exist_ok=True)
                    # if is_output_pcap:
                    #     wrpcap(f'output/{filename}/packet_{i}.pcap', [pkt])
                    # i = i + 1

                # print(ret)
                return ret

            def read_pkt(filename: str):
                pkts = rdpcap(filename)
                print(pkts)

            # read_pkt("output/packet_1.pcap")
            filename = fp
            # filename = "vpn_aim_chat1a.pcap"
            write_csv_from_list(process(filename, is_output_pcap=True), f"{filename}.csv")

read(filepath, 0)



