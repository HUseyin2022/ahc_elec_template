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
Node 0 initialized with alias 0
Node 1 initialized with alias 1
Node 2 initialized with alias 2
Node 3 initialized with alias 3
Node 4 initialized with alias 4
Node 5 initialized with alias 5
Node 6 initialized with alias 6
Node 7 initialized with alias 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 0 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 1 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 2 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 3 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 4 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 5 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 6 from Node 6
Node 7 (ID: 7) sending alias to Node 0
Node 0 (ID: 0) received alias 7 from Node 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 7 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 7 (ID: 7) sending alias to Node 0
Node 0 (ID: 0) received alias 7 from Node 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 7 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Total messages sent: 44
Total messages received: 44
Leader is node 7 with alias 7

    .. image:: figures/Screen4.jpg
      :width: 400 

Echo Extinction algorithm
Node 0 initialized with alias 0
Node 1 initialized with alias 1
Node 2 initialized with alias 2
Node 3 initialized with alias 3
Node 4 initialized with alias 4
Node 5 initialized with alias 5
Node 6 initialized with alias 6
Node 7 initialized with alias 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 0 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 1 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 2 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 3 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 4 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 5 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 6 from Node 6
Node 7 (ID: 7) sending alias to Node 0
Node 0 (ID: 0) received alias 7 from Node 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 7 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Node 7 (ID: 7) sending alias to Node 0
Node 0 (ID: 0) received alias 7 from Node 7
Node 0 (ID: 0) sending alias to Node 1
Node 1 (ID: 1) received alias 7 from Node 0
Node 1 (ID: 1) sending alias to Node 2
Node 2 (ID: 2) received alias 7 from Node 1
Node 2 (ID: 2) sending alias to Node 3
Node 3 (ID: 3) received alias 7 from Node 2
Node 3 (ID: 3) sending alias to Node 4
Node 4 (ID: 4) received alias 7 from Node 3
Node 4 (ID: 4) sending alias to Node 5
Node 5 (ID: 5) received alias 7 from Node 4
Node 5 (ID: 5) sending alias to Node 6
Node 6 (ID: 6) received alias 7 from Node 5
Node 6 (ID: 6) sending alias to Node 7
Node 7 (ID: 7) received alias 7 from Node 6
Node 7 is the elected leader.
Total messages sent: 44
Total messages received: 44
Leader is node 7 with alias 7
PS C:\Users\hsagi\OneDrive\Masaüstü\C532\ahc_elec_template> ^C
PS C:\Users\hsagi\OneDrive\Masaüstü\C532\ahc_elec_template>
PS C:\Users\hsagi\OneDrive\Masaüstü\C532\ahc_elec_template>  c:; cd 'c:\Users\hsagi\OneDrive\Masaüstü\C532\ahc_elec_template'; & 'c:\Users\hsagi\AppData\Local\Programs\Python\Python311\python.exe' 'c:\Users\hsagi\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher' '52570' '--' 'c:\Users\hsagi\OneDrive\Masaüstü\C532\ahc_elec_template\elecname\echoelection' 
Message sent from Process 0 to Process 1: <Wave, Highest ID: 0>
Message sent from Process 0 to Process 5: <Wave, Highest ID: 0>
Message sent from Process 1 to Process 0: <Wave, Highest ID: 1>
Message sent from Process 1 to Process 4: <Wave, Highest ID: 1>
Message sent from Process 1 to Process 2: <Wave, Highest ID: 1>
Message sent from Process 3 to Process 4: <Wave, Highest ID: 3>
Message sent from Process 3 to Process 6: <Wave, Highest ID: 3>
Message sent from Process 3 to Process 7: <Wave, Highest ID: 3>
Message sent from Process 6 to Process 3: <Wave, Highest ID: 6>
Message sent from Process 7 to Process 3: <Wave, Highest ID: 7>
Message sent from Process 4 to Process 3: <Wave, Highest ID: 4>
Message sent from Process 4 to Process 5: <Wave, Highest ID: 4>
Message sent from Process 4 to Process 1: <Wave, Highest ID: 4>
Message sent from Process 2 to Process 1: <Wave, Highest ID: 2>
Message sent from Process 5 to Process 4: <Wave, Highest ID: 5>
Message sent from Process 5 to Process 0: <Wave, Highest ID: 5>
Message received by Process 3: <Wave, Highest ID: 7>
Message sent from Process 3 to Process 4: <Wave, Highest ID: 7>
Message sent from Process 3 to Process 6: <Wave, Highest ID: 7>
Message sent from Process 3 to Process 7: <Wave, Highest ID: 7>
Message received by Process 3: <Wave, Highest ID: 6>
Message received by Process 4: <Wave, Highest ID: 1>
Message received by Process 0: <Wave, Highest ID: 1>
Message sent from Process 0 to Process 1: <Wave, Highest ID: 1>
Message sent from Process 0 to Process 5: <Wave, Highest ID: 1>
Message received by Process 2: <Wave, Highest ID: 1>
Message received by Process 6: <Wave, Highest ID: 7>
Message received by Process 4: <Wave, Highest ID: 7>
Message sent from Process 6 to Process 3: <Wave, Highest ID: 7>
Message sent from Process 4 to Process 3: <Wave, Highest ID: 7>
Message sent from Process 4 to Process 5: <Wave, Highest ID: 7>
Message sent from Process 4 to Process 1: <Wave, Highest ID: 7>
Message received by Process 7: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 2>
Message sent from Process 1 to Process 0: <Wave, Highest ID: 2>
Message sent from Process 1 to Process 4: <Wave, Highest ID: 2>
Message sent from Process 1 to Process 2: <Wave, Highest ID: 2>
Message received by Process 1: <Wave, Highest ID: 1>
Message received by Process 5: <Wave, Highest ID: 1>
Message received by Process 3: <Wave, Highest ID: 7>
Message received by Process 5: <Wave, Highest ID: 0>
Message received by Process 1: <Wave, Highest ID: 0>
Message received by Process 0: <Wave, Highest ID: 2>
Message sent from Process 0 to Process 1: <Wave, Highest ID: 2>
Message sent from Process 0 to Process 5: <Wave, Highest ID: 2>
Message received by Process 4: <Wave, Highest ID: 2>
Message received by Process 2: <Wave, Highest ID: 2>
Message received by Process 4: <Wave, Highest ID: 3>
Message received by Process 6: <Wave, Highest ID: 3>
Message received by Process 7: <Wave, Highest ID: 3>
Message received by Process 1: <Wave, Highest ID: 4>
Message sent from Process 1 to Process 0: <Wave, Highest ID: 4>
Message sent from Process 1 to Process 4: <Wave, Highest ID: 4>
Message sent from Process 1 to Process 2: <Wave, Highest ID: 4>
Message received by Process 3: <Wave, Highest ID: 4>
Message received by Process 5: <Wave, Highest ID: 4>
Message received by Process 4: <Wave, Highest ID: 5>
Message received by Process 0: <Wave, Highest ID: 5>
Message sent from Process 0 to Process 1: <Wave, Highest ID: 5>
Message sent from Process 0 to Process 5: <Wave, Highest ID: 5>
Message received by Process 5: <Wave, Highest ID: 7>
Message received by Process 3: <Wave, Highest ID: 7>
Message sent from Process 5 to Process 4: <Wave, Highest ID: 7>
Message sent from Process 5 to Process 0: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 7>
Message sent from Process 1 to Process 0: <Wave, Highest ID: 7>
Message sent from Process 1 to Process 4: <Wave, Highest ID: 7>
Message sent from Process 1 to Process 2: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 2>
Message received by Process 5: <Wave, Highest ID: 2>
Message received by Process 4: <Wave, Highest ID: 4>
Message received by Process 2: <Wave, Highest ID: 4>
Message sent from Process 2 to Process 1: <Wave, Highest ID: 4>
Message received by Process 0: <Wave, Highest ID: 4>
Message received by Process 4: <Wave, Highest ID: 7>
Message received by Process 0: <Wave, Highest ID: 7>
Message sent from Process 0 to Process 1: <Wave, Highest ID: 7>
Message sent from Process 0 to Process 5: <Wave, Highest ID: 7>
Message received by Process 5: <Wave, Highest ID: 5>
Message received by Process 1: <Wave, Highest ID: 5>
Message received by Process 2: <Wave, Highest ID: 7>
Message received by Process 4: <Wave, Highest ID: 7>
Message sent from Process 2 to Process 1: <Wave, Highest ID: 7>
Message received by Process 0: <Wave, Highest ID: 7>
Message received by Process 5: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 7>
Message received by Process 1: <Wave, Highest ID: 4>
The elected leader is Process 7


    .. image:: figures/Screen5.jpg
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
The message complexity of the Echo with Extinction (EwE) algorithm in a ring topology is O(n) is the number of nodes in the ring




