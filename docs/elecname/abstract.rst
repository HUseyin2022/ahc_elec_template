.. include:: substitutions.rst
========
Abstract
========

In a distributed system, a leader is needed to provide coordination and execution the  on behalf of other entities in the system.  Leader Election is a process where we elect a leader/coordinator from the existing entitites in the network. Leader election is a required to improve efficiency and reduce coordination as well as operations.
Synchronization can be costly in a big distributed system. When each entity in the network recognizes a unique node as the task leader, it will be possible to reduce the sysncronization cost. All entities in the network got informed after the election has taken place. There are various algorithms for leader election. All algorithms try to improve complexity. Algorithms for leader election various according to communication mechanism, process name, network topology and size of network.
There are different types of leader election algorithms for different network topologies. The network can have a ring topology, tree topology, star topology, bus topology, and other topologies.
=======
