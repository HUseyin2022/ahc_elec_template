.. include:: substitutions.rst

Implementation, Results and Discussion
======================================

Implementation and Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The process of electing a leader using the Dolev-Klawe-Rodeh algorithm with the provided code.


This implementation follows the rules of the AHC framework, utilizing components, event handling, and queue-based communication. It represents nodes in the Dolev-Klawe-Rodeh algorithm and simulates the election process. Each node selects an ID and initiates the election process. If a node receives a message with a higher ID, it becomes passive for the current round and triggers the election process again. If a node receives a message with a lower ID, it ignores the message. If a node receives a message with the same ID, it becomes the leader.

In the DolevKlaweRodehNode class, each node has a unique identifier id_p, which is initialized to a hash value derived from the node's name and instance number modulo the ring size. This identifier represents the node's position in the ring.

Initialization (on_init method): Each node initializes its id_p and prints it along with its name and instance number. This step ensures that each node has a unique identifier for the current round of election.
Start Election (start_election method): When a node receives a "start_election" event, it checks if it is in the "ACTIVE" state. If so, it creates a message containing its identifier (id_p) and the current election round number, and sends this message to its peers.
Receive Message (receive_message method): When a node receives a message from a peer, it compares the round number and identifier in the message with its own. Based on the comparison, the node can take one of the following actions:
If the received round number is greater than its current round number, or if the received round number is equal to its current round number but the received identifier is greater, the node transitions to the "PASSIVE" state, updates its round number, clears its own identifier, and starts a new election.
If the received round number and identifier are both less than its own, the node ignores the message.
If the received round number and identifier are both equal to its own, the node declares itself the leader and prints a message indicating that it has been elected as the leader.
Simulating Events: Finally, the example usage simulates the initialization and start of election events for each node in the network.

In Echo Extinction algorithm, the State enum has been extended to include the ECHO state to represent the phase where a node receives echo messages. The receive_message method is updated to transition the node to the ECHO state when it receives an echo message, and it keeps track of the neighbors from which echo messages are received. Finally, the experiment execute_echo_algorithm is created to simulate the echo algorithm process.


Results
~~~~~~~~
DolevKlaweRodeh algorithm
Node Node-1 selected 4 as their ID for round 1
Node Node-1 is the elected leader.
Node Node-2 selected 4 as their ID for round 1
Node Node-2 is the elected leader.
Node Node-3 selected 3 as their ID for round 1
Node Node-4 selected 0 as their ID for round 1
Node Node-5 selected 2 as their ID for round 1

    .. image:: figures/Screen4.jpg
      :width: 400 

Echo Extinction algorithm
Node Node-1 selected 0 as their ID for round 1
Node Node-2 selected 4 as their ID for round 1
Node Node-3 selected 1 as their ID for round 1
Node Node-4 selected 1 as their ID for round 1
Node Node-5 selected 1 as their ID for round 1
Elected leader: Node 2


    .. image:: figures/Screen4.jpg
      :width: 400 


Echo Extinction algorithm Discussion

To analyze the time and message complexity of the provided code,  the key components:

Time Complexity:
The handle_event method is called for each event, iterating over all nodes and processing each event for each node. Therefore, the time complexity of handling events is O(N * E), where N is the number of nodes and E is the number of events.
In the receive_message method, the time complexity mainly depends on the conditions checking the message round and ID. Since these are constant time operations, the overall time complexity is O(1).
Message Complexity:
In the send_peer method, a message is created and sent to peers. However, the method body is empty, indicating that no actual messages are sent between nodes. Therefore, the message complexity is O(0), meaning there are no messages exchanged between nodes in this implementation.
In summary:

Time Complexity: O(N * E)
Message Complexity: O(0)




