Code Documentation 
==================
DolevKlaweRodeh Algorithm
import time
from adhoccomputing.GenericModel import GenericModel, Event, EventTypes, GenericMessage, GenericMessageHeader, GenericMessagePayload
from adhoccomputing.Generics import ConnectorTypes
from adhoccomputing.Experimentation.Topology import Topology
from random import randint
from enum import Enum
import queue

class State(Enum):
    ACTIVE = 1
    PASSIVE = 2
    LEADER = 3

class DolevKlaweRodehNode:
    def __init__(self, name, instance_number, ring_size):
        self.name = name
        self.instance_number = instance_number
        self.ring_size = ring_size
        self.id_p = 0
        self.state = State.ACTIVE
        self.election_round = 1
        self.neighbour_id = None
        self.input_queue = queue.Queue()

    def on_init(self):
        self.id_p = hash(f"{self.name}-{self.instance_number}") % self.ring_size
        print(f"Node {self.name}-{self.instance_number} selected {self.id_p} as their ID for round {self.election_round}")
        self.neighbour_id = (self.instance_number + 1) % self.ring_size

    def handle_event(self, event):
        event_name = event['event']
        if event_name == 'init':
            self.on_init()
        elif event_name == 'start_election':
            self.start_election()
        elif event_name == 'receive_message':  # Added for message reception
            self.receive_message(event['message'])  # Call receive_message with the message

    def start_election(self):
        if self.state == State.ACTIVE:
            message = {
                "source": f"{self.name}-{self.instance_number}",
                "round": self.election_round,
                "id_p": self.id_p
            }
            self.send_peer(message)

    def send_peer(self, message):
        # Assuming a method to send message to peers
        pass

    def receive_message(self, message):
        if self.state != State.LEADER:
            if message["round"] > self.election_round or (message["round"] == self.election_round and message["id_p"] > self.id_p):
                self.state = State.PASSIVE
                self.id_p = " "
                self.election_round += 1
                self.start_election()
            elif message["round"] == self.election_round and message["id_p"] < self.id_p:
                return
            elif message["round"] == self.election_round and message["id_p"] == self.id_p:
                self.state = State.LEADER
                print(f"Node {self.name}-{self.instance_number} is the elected leader.")

# Experiment to elect a leader
def elect_leader():
    # Create nodes
    node1 = DolevKlaweRodehNode("Node", 1, 5)
    node2 = DolevKlaweRodehNode("Node", 2, 5)
    node3 = DolevKlaweRodehNode("Node", 3, 5)
    node4 = DolevKlaweRodehNode("Node", 4, 5)
    node5 = DolevKlaweRodehNode("Node", 5, 5)

    # Simulate events
    events = [
        {"event": "init"},
        {"event": "start_election"},
        {"event": "receive_message", "message": {"round": 1, "id_p": 4}},  # Example message
    ]

    for node in [node1, node2, node3, node4, node5]:
        for event in events:
            node.handle_event(event)


# Execute the experiment
elect_leader()

import networkx as nx
import matplotlib.pyplot as plt

# Create nodes
nodes = [DolevKlaweRodehNode("Node", i, 5) for i in range(1, 6)]

# Define the connections between nodes
edges = [(nodes[i - 1], nodes[i % 5]) for i in range(5)]

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=edges)

# Draw labels
labels = {node: f"{node.name}-{node.instance_number}" for node in nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=12)

plt.title("Graph Representation of Nodes")
plt.show()



Echo Extinction Algorithm

import time
from adhoccomputing.GenericModel import GenericModel, Event, EventTypes, GenericMessage, GenericMessageHeader, GenericMessagePayload
from adhoccomputing.Generics import ConnectorTypes
from adhoccomputing.Experimentation.Topology import Topology
from random import randint
from enum import Enum
import queue

class State(Enum):
    ACTIVE = 1
    PASSIVE = 2
    LEADER = 3

class EchoNode:
    def __init__(self, name, instance_number, ring_size):
        self.name = name
        self.instance_number = instance_number
        self.ring_size = ring_size
        self.id_p = 0
        self.state = State.ACTIVE
        self.election_round = 1
        self.neighbour_id = None
        self.leader = None
        self.input_queue = queue.Queue()

    def on_init(self):
        self.id_p = hash(f"{self.name}-{self.instance_number}") % self.ring_size
        print(f"Node {self.name}-{self.instance_number} selected {self.id_p} as their ID for round {self.election_round}")
        self.neighbour_id = (self.instance_number + 1) % self.ring_size

    def handle_event(self, event):
        event_name = event['event']
        if event_name == 'init':
            self.on_init()
        elif event_name == 'start_election':
            self.start_election()
        elif event_name == 'receive_message':  # Added for message reception
            self.receive_message(event['message'])  # Call receive_message with the message

    def start_election(self):
        if self.state == State.ACTIVE:
            message = {
                "source": f"{self.name}-{self.instance_number}",
                "round": self.election_round,
                "id_p": self.id_p
            }
            self.send_peer(message)

    def send_peer(self, message):
        # Assuming a method to send message to peers
        pass

    def receive_message(self, message):
        if self.state != State.LEADER:
            if message["round"] > self.election_round or (message["round"] == self.election_round and message["id_p"] > self.id_p):
                self.state = State.PASSIVE
                self.id_p = " "
                self.election_round += 1
                self.start_election()
            elif message["round"] == self.election_round and message["id_p"] < self.id_p:
                return
            elif message["round"] == self.election_round and message["id_p"] == self.id_p:
                self.state = State.LEADER
                self.leader = f"{self.name}-{self.instance_number}"

# Function to check and print the leader
def print_leader(nodes):
    for node in nodes:
        if node.state == State.LEADER:
            print("Elected leader:", node.name, node.instance_number)

# Experiment to elect a leader
def elect_leader():
    # Create nodes
    node1 = EchoNode("Node", 1, 5)
    node2 = EchoNode("Node", 2, 5)
    node3 = EchoNode("Node", 3, 5)
    node4 = EchoNode("Node", 4, 5)
    node5 = EchoNode("Node", 5, 5)

    # Simulate events
    events = [
        {"event": "init"},
        {"event": "start_election"},
        {"event": "receive_message", "message": {"round": 1, "id_p": 4}},  # Example message
    ]

    # Handle events for each node
    for node in [node1, node2, node3, node4, node5]:
        for event in events:
            node.handle_event(event)

    # Print the elected leader
    print_leader([node1, node2, node3, node4, node5])

# Execute the experiment
elect_leader()
nodes = ["Node1", "Node2", "Node3", "Node4", "Node5"]

import matplotlib.pyplot as plt
import networkx as nx

# Define the edges (connections between nodes)
edges = [("Node1", "Node2"), ("Node2", "Node3"), ("Node3", "Node4"), ("Node4", "Node5"), ("Node5", "Node1")]

# Create a graph object
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
nx.draw(G, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", pos=nx.spring_layout(G))
plt.title("Graph Representation of Nodes")
plt.show()