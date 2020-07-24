import pandas as pd
import itertools as it
from Network import Network
import numpy as np
import json
from Connection import Connection
from random import shuffle
import matplotlib.pyplot as plt

def create_traffic_matrix (nodes , rate ):
    s = pd. Series ( data =[0.0] * len( nodes ) , index = nodes )
    df = pd. DataFrame (float ( rate ) , index =s.index , columns =s.index , dtype =s. dtype )
    np. fill_diagonal (df. values , s)
    return df

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

def main ():
    network = Network ('nodes.json') # creates nodes and line objects
    network . connect ()
    network . draw ()
    node_labels = list ( network . nodes . keys ())
    T = create_traffic_matrix ( node_labels , 600)
    t = T. values
    connections = []
    node_pairs = list ( filter ( lambda x: x[0] != x[1] ,\
        list (it. product ( node_labels , node_labels ))))
    shuffle ( node_pairs )
    for node_pair in node_pairs :
        connection = Connection ( node_pair [0] , node_pair [ -1] , \
        float (T.loc[ node_pair [0] , node_pair [ -1]]))
        connections . append ( connection ) # list of connection objects
    streamed_connections = network . stream \
    ( connections , 'snr', 'flex-rate' )
    #print('streamed connections ',streamed_connections)
    snrs = []
    [ snrs . extend ( connection .snr) for connection in streamed_connections ]
    rbl = []
    #print(connection.lightpaths)
    for connection in streamed_connections :
        for lightpath in connection . lightpaths :
            rbl . append ( lightpath . bitrate )
            print("\nlp bitrate", rbl)
    print(rbl)
    # for calculating and plotting bitrate#
    rbs = [connection.calculate_capacity() \
           for connection in streamed_connections]
    plt.hist(rbs, bins=10)
    plt.title('BitrateDistribution[Gbps]')
    plt.show()

    # Plot
    plt. hist (snrs , bins =10)
    plt. title ('SNR Distribution [dB]')
    plt. show ()
    rbc = [ connection . calculate_capacity () for connection in streamed_connections ]
    plt. hist (rbc , bins =10)
    plt. title ('Connection Capacity Distribution [ Gbps ]')
    plt. show ()
    plt. hist (rbl , bins =10)
    plt. title ('Lightpaths Capacity Distribution [ Gbps ]')
    plt. show ()

    s = pd.Series(data=[0.0] * len(node_labels), index=node_labels)
    df = pd.DataFrame(0.0, index=s.index, columns=s.index, dtype=s.dtype)
    print(df)
    for connection in streamed_connections:
        df.loc[connection.input_node, \
               connection.output_node] = connection.bitrate
    print(df)
    plot3Dbars(t)
    plot3Dbars(df.values)
    print('Avg SNR: {:.2f} dB '.format(np.mean (list(filter(lambda x: x != 0, snrs)))))
    print('Total Capacity Connections: {:.2f} Tbps '.format(np.sum(rbc) * 1e-3))
    print('Total Capacity Lightpaths: {:.2f} Tbps '.format(np.sum(rbl) * 1e-3))
    print('Avg Capacity: {:.2f} Gbps '.format(np.mean(rbc)))

if __name__ == "__main__":
    main()