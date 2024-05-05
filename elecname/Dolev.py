
# %%

import time
from adhoccomputing.GenericModel import GenericModel, Event, EventTypes, GenericMessage, GenericMessageHeader, GenericMessagePayload
from adhoccomputing.Generics import ConnectorTypes
from adhoccomputing.Experimentation.Topology import Topology
from random import randint
import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum
import queue

class State(Enum):
    ACTIVE = 1
    PASSIVE = 2
    LEADER = 3

class DolevKlaweRodehNode:
    def __init__(self, instance_number, ring_size, nodes):
        self.instance_number = instance_number
        self.ring_size = ring_size
        self.id_p = instance_number
        self.state = State.ACTIVE
        self.nodes = nodes
        self.highest_id_seen = self.id_p

    def on_init(self):
        print(f"Node {self.instance_number} initialized with alias {self.id_p}")

    def start_election(self):
        self.send_message(self.highest_id_seen)

    def send_message(self, alias):
        next_node_index = (self.instance_number + 1) % self.ring_size
        next_node = self.nodes[next_node_index]
        print(f"Node {self.instance_number} (ID: {self.id_p}) sending alias to Node {next_node.instance_number}")
        next_node.receive_message(alias, self.instance_number)

    def receive_message(self, alias, sender_id):
        print(f"Node {self.instance_number} (ID: {self.id_p}) received alias {alias} from Node {sender_id}")
        if alias > self.highest_id_seen:
            self.highest_id_seen = alias
            self.state = State.PASSIVE
        if alias == self.id_p and self.highest_id_seen == self.id_p:
            self.state = State.LEADER
            print(f"Node {self.instance_number} is the elected leader.")
        else:
            self.send_message(self.highest_id_seen)

def draw_ring_topology(nodes):
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node.instance_number)
        next_node_index = (node.instance_number + 1) % len(nodes)
        G.add_edge(node.instance_number, next_node_index)
    
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='k', node_size=2000, arrowstyle='-|>', arrowsize=20)
    plt.title("Unidirectional Ring Topology")
    plt.show()

# Number of nodes in the ring
ring_size = 5

# Create all nodes and set them to know each other
nodes = [DolevKlaweRodehNode(i, ring_size, []) for i in range(ring_size)]
for node in nodes:
    node.nodes = nodes

# Initialize all nodes
for node in nodes:
    node.on_init()

# Start the election process for each node, simulating each sending an alias
for node in nodes:
    node.start_election()

# Draw the topology
draw_ring_topology(nodes)

# After all messages have been processed
for node in nodes:
    if node.state == State.LEADER:
        print(f"Leader is node {node.instance_number} with alias {node.highest_id_seen}")
        break
else:
    print("No leader was elected.")
