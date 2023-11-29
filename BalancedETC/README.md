Balanced ETC

We introduce a novel approach for encrypted Internet traffic classification and application identification by transforming basic flow data into grayscale image, and then using balanced supervised contrastive learning to identify the traffic class (browsing, chat, video, etc.) and the application in use. Our approach can classify traffic with high accuracy, both for a specific application, or a traffic class, even for VPN and Tor traffic. Our method can improve the classification accuracy of network traffic classification on unbalanced dataset.

Approach

1.Our approach uses the first 25 packets of each network flow.
2.Transform the packet size and packet arrival time interval of the first 25 packets of each network flow into 5×10 pixel grayscale image.Transform the first 100 bytes of each packet's Ethernet header, IP header, and TCP/UDP header into 10×10 pixel grayscale image. The images are stitched together to produce a 10×15 pixel grayscale image.
3.Classification using balanced supervised contrast learning.

Dataset

We use labeled datasets of packet capture (pcap) files from the Uni. of New Brunswick (UNB): "ISCX VPN-nonVPN traffic dataset" (ISCX-VPN) and "ISCX Tor-nonTor dataset" (ISCX-Tor).

Run the files as follow:

1.Processing

2.Classify
