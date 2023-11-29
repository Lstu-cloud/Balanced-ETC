Balanced ETC

We introduce a novel approach for encrypted Internet traffic classification and application identification by transforming basic flow data into grayscale image, and then using balanced supervised contrastive learning to identify the traffic class (browsing, chat, video, etc.) and the application in use. Our approach can classify traffic with high accuracy, both for a specific application, or a traffic class, even for VPN and Tor traffic. Our method can improve the classification accuracy of network traffic classification on unbalanced dataset.

Approach

1.Our approach uses the first 25 packets of each network flow.
2.Transform the packet size and packet arrival time interval of the first 25 packets of each network flow into 5×10 pixel grayscale image.Transform the first 100 bytes of each packet's Ethernet header, IP header, and TCP/UDP header into 10×10 pixel grayscale image. The images are stitched together to produce 10×15 pixel grayscale image.
3.Classification using balanced supervised contrast learning.

Dataset

We use labeled datasets of packet capture (pcap) files from the Uni. of New Brunswick (UNB): "ISCX VPN-nonVPN traffic dataset" (ISCX-VPN) and "ISCX Tor-nonTor dataset" (ISCX-Tor).

Run the files as follow:

step1.Processing

1.split.py: Network flow splitting.
2.pc.py: Transform pcap to csv.
3.cd.py: Convert base 16 to base 10.
4.firstn.py: The first n packets of each flow are retained. 
5.pincsv.py: csv file splicing.
6.cp.py: Transform csv to picture.
7.combine.py: picture splicing。
8.generic_parser.py: Analyze packet size and packet arrival interval in each network flow. 
The generic_parser.py runtime environment is python2.7.18, and the other files are python3.8.16.

step2.Classify
