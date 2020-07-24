import pandas as pd
import itertools as it
from Network import Network
import numpy as np
import json
from Connection import Connection
from random import shuffle
import matplotlib.pyplot as plt

def create_traffic_matrix(nodes , rate , multiplier =1):
    s = pd. Series ( data =[0.0] * len( nodes ) , index = nodes )
    df = pd. DataFrame ( float ( rate * multiplier ) , index =s.index , columns =s.index , dtype =s. dtype )
    np. fill_diagonal (df. values , s)
    return df

'''
def plot3Dbars (t):
    fig = plt. figure ()
    ax = fig. add_subplot (111 , projection ='3d')
    x_data , y_data = np. meshgrid (np. arange (t. shape [1]) ,
    np. arange (t. shape [0]))
    x_data = x_data . flatten ()
    y_data = y_data . flatten ()
    z_data = t. flatten ()
    ax. bar3d ( x_data ,y_data ,np. zeros ( len( z_data )) ,1 , 1 , z_data )
    plt. show ()
'''

def main ():
    NMC = 5
    node_pairs_realizations = []
    stream_conn_list = []
    lines_state_list = []
    for i in range(NMC):
        print('Monte - CarloRealization  # {:d}'. format (i +1))
        network = Network('nodes.json', Nch=10, upgrade_line='AC')
        # creates nodes and line objects
        network.connect()  # connects the net by setting the line
        # successive attribute with the node object at the end of the line
        network.draw ()
        node_labels = list ( network.nodes.keys ())
        T = create_traffic_matrix ( node_labels, 400, multiplier =5)
        t = T.values
        #print (t)
        # it creates pairs of nodes
        node_pairs = list ( filter ( lambda x: x[0] != x[1], list(it.product(node_labels, node_labels))))
        shuffle(node_pairs)  # Create allocation request sequence realization
       # node_pairs_realizations.append(copy.deepcopy(node_pairs))
        connections = []
        for node_pair in node_pairs:
            connection = Connection(node_pair[0], node_pair[-1], float(T.loc[node_pair[0], node_pair[-1]]))

        # creates connection object between random node pair
        connections.append(connection)  # list of connection objects
        streamed_connections = network.stream(connections, best='snr', transceiver ='shannon')
        stream_conn_list.append(streamed_connections)
        lines_state_list.append(network.lines)  # Get lines state

    # Get MC stats
    snr_conns = []
    rbl_conns = []
    rbc_conns = []

    for streamed_conn in stream_conn_list:
        snrs = []
        rbl = []
        [snrs.extend(connection.snr) for connection in streamed_conn]
        for connection in streamed_conn:
            for lightpath in connection.lightpaths:
                rbl.append(lightpath.bitrate)
        rbc = [connection.calculate_capacity() for connection in streamed_conn]
        snr_conns.append(snrs)
        rbl_conns.append(rbl)
        rbc_conns.append(rbc)
    #########
    # Congestion
    lines_labels = list(lines_state_list[0].keys())
    congestions = {label: [] for label in lines_labels}
    for line_state in lines_state_list:
        for line_label, line in line_state.items():
            cong = line.state.count('occupied') / len(line.state)
            congestions[line_label].append(cong)

    avg_congestion = {label: [] for label in lines_labels}
    for line_label, cong in congestions.items():
        avg_congestion[line_label] = np.mean(cong)

    plt.bar(range(len(avg_congestion)), list(avg_congestion.values()), align='center')
    plt.xticks(range(len(avg_congestion)), list(avg_congestion.keys()))
    plt.title('Congestion')
    plt.show()
    ############
    avg_snr_list = []
    avg_rbl_list = []
    traffic_list = []
    [traffic_list.append(np.sum(rbl_list)) for rbl_list in rbl_conns]
    print(traffic_list)
    [avg_rbl_list.append(np.mean(rbl_list)) for rbl_list in rbl_conns]
    [avg_snr_list.append(np.mean(list(filter(lambda x: x != 0, snr_list)))) \
     for snr_list in snr_conns]


    #################
    print('\n')
    print('Line to upgrade: {} '.format(max(avg_congestion, key=avg_congestion.get)))
    print('Avg Total Traffic: {:.2f} Tbps '.format(np.mean(traffic_list) * 1e-3))
    print('Avg Lighpath Bitrate: {:.2f} Gbps '.format(np.mean(avg_rbl_list)))
    print('Avg Lighpath SNR: {:.2f} dB '.format(np.mean(avg_snr_list)))

if __name__ == "__main__":
    main()