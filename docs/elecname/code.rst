Code Documentation 
==================
DolevKlaweRodeh Algorithm
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




Echo Extinction Algorithm

import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from random import randint, choice, shuffle
from threading import Thread, Lock
from time import sleep
from typing import List, Tuple
from enum import Enum


def current_time() -> float:
    return datetime.timestamp(datetime.now())

class Message:
    def __init__(self):
        self.delay = current_time() + randint(0, 2000) / 1000

    def has_arrived(self) -> bool:
        return current_time() >= self.delay

    def __str__(self):
        return "<Message>"

class WaveMessage(Message):
    def __init__(self, highest_id):
        super().__init__()
        self.highest_id = highest_id

    def __str__(self):
        return f"<Wave, Highest ID: {self.highest_id}>"

class State(Enum):
    ACTIVE = 0
    INACTIVE = 1

class MessageManager:
    def __init__(self):
        self.messages = {}
        self.lock = Lock()
        self.active = True  # Initially active

    def send_message(self, from_id: int, to_id: int, msg: Message):
        with self.lock:
            if to_id not in self.messages:
                self.messages[to_id] = []
            self.messages[to_id].append(msg)
            print(f"Message sent from Process {from_id} to Process {to_id}: {msg}")

    def receive_message(self, p_id: int):
        with self.lock:
            if p_id in self.messages and self.messages[p_id]:
                for message in self.messages[p_id]:
                    if message.has_arrived():
                        self.messages[p_id].remove(message)
                        print(f"Message received by Process {p_id}: {message}")
                        return message
            return None

    def check_active(self):
        with self.lock:
            return any(self.messages.values())  # Check if there are any messages in transit

class Process(Thread):
    def __init__(self, process_id: int, neighbors, manager: MessageManager):
        super().__init__()
        self.process_id = process_id
        self.neighbors = neighbors
        self.manager = manager
        self.state = State.INACTIVE
        self.highest_id = process_id
        self.tree_parent = None
        self.tree_children = []

    def run(self):
        self.broadcast(WaveMessage(self.process_id))
        self.state = State.ACTIVE

        while self.manager.check_active():  # Only continue if there are messages being processed
            msg = self.manager.receive_message(self.process_id)
            if msg and isinstance(msg, WaveMessage):
                if msg.highest_id > self.highest_id:
                    self.highest_id = msg.highest_id
                    self.broadcast(WaveMessage(self.highest_id))
                    # Update parent and children
                    self.tree_parent = msg.highest_id
                    self.tree_children = [neighbor for neighbor in self.neighbors if neighbor != self.tree_parent]
            sleep(0.01)  # Sleep to reduce CPU usage

        self.state = State.INACTIVE

    def broadcast(self, message):
        for neighbor in self.neighbors:
            if neighbor != self.process_id:  # Prevent sending to self
                self.manager.send_message(self.process_id, neighbor, message)

def setup_processes(num_processes: int) -> Tuple[List[Process], MessageManager, nx.Graph]:
    manager = MessageManager()
    graph = nx.connected_watts_strogatz_graph(num_processes, 3, 0.5, seed=42)
    processes = [Process(node, list(graph.adj[node]), manager) for node in graph.nodes()]
    return processes, manager, graph

def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=500)
    plt.title(title)
    plt.show()

def draw_tree(processes):
    G = nx.Graph()
    for process in processes:
        if process.tree_parent is not None:
            G.add_edge(process.process_id, process.tree_parent)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=500)
    plt.title("Output Tree Graph")
    plt.show()

def run_simulation(num_processes: int):
    processes, manager, graph = setup_processes(num_processes)
    draw_graph(graph, "Initial Network Topology")
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    leader_id = max((p.highest_id for p in processes), default=None)
    print(f"The elected leader is Process {leader_id}")
    
    draw_tree(processes)

run_simulation(8)  # Running the simulation with 8 processes