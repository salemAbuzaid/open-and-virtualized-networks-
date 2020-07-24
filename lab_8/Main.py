from random import shuffle
from Network import Network
import numpy as np
import json
from Connection import Connection
from random import shuffle
import matplotlib.pyplot as plt

network = Network('nodes.json') # creates nodes and line objects
network.connect() #connects the net by setting the line successive attribute with the node object at the end of the line
node_labels = list(network.nodes.keys())
connections = []
for i in range(100):
    shuffle(node_labels)
    connection = Connection(node_labels[0], node_labels[-1]) # creates connection object between random node pair
    connections.append(connection) # list of connection objects

streamed_connections = network.stream(connections, best='snr', transceiver= 'flex-rate')
snrs = [connection.snr for connection in streamed_connections]
rbs = [connection.calculate_capacity for connection in streamed_connections]
plt.hist(snrs, bins=10)
plt.title('SNR Distribution')
plt.show()
plt. hist (rbs , bins =10)
plt. title ('Bitrate Distribution [ Gbps ]')
plt. show ()
network.draw()
print("Total Capacity : {:.2 f} Tbps",format(np.sum(rbs)*1e-3))
print("Avg Capacity : {:.2 f} Gbps",format(np.mean(rbs)))


