.. include:: substitutions.rst

|ElecName|
=========================================

Background and Related Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Election algorithm provides that each process has the same local algorithm, it is decentralized meaning a computation can be initialized by an arbitrary non empty subset of the process. The algorithm reaches a configuration defining one process is the state leader and others are state lost. 
It is needed to be studied under assumptions such as the system is fully asynchronous and identified by a unique name.
In this section, election algorithms, will focus on two ones: the Ring Election: Dolev-Klawe-Rodeh algorithm and the Echo algorithm with extinction algorithm. We will present the principles behind these algorithms, their implementation details, and compare their strengths and weaknesses.

Distributed Algorithm: |ElecName| 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Dolev-Klawe-Rodeh algorithm uses directed rings which messages cannot travel in both directions. Active process whose ID is p and next active neighbors are q and r. The Ids are collected at r. There are three cases to evaluate the election process.
If p>q and r; r remains active and progress to the next election round
If p<q or r; r becomes passive
If p=q and r; r becomes the leader. 

When a process receives a message START(), it initializes competitori and maxidi before sending a message ELECTION(1, idi) on its single outgoing channel (line 1). Let us observe that messages do not carry round numbers. Actually, round numbers are used only to explain the behavior of the algorithm and compute the total number of messages. When a process pi receives a message ELECTION(1, id), pi forwards it on its outgoing channel if it is no longer a competitor. If pi is a competitor, there are two cases.
If the message ELECTION(1, idi ) is such that id = maxidi , then it has made a full turn on the ring, and consequently maxidi is the greatest identity. In this case, pi sends the message ELECTED(maxidi , idi ), which is propagated on the ring to inform all the processes. If message ELECTION(1, id) is such that id != maxidi , pi copies id in proxy_fori, and forwards the message ELECTION(2, id) on its outgoing channel.
When a process pi receives a message ELECTION(2, id), it forwards it (as previously) on its outgoing channel if it is no longer a competitor. If it is a competitor, pi checks if proxy_fori > max(id, maxidi ), i.e., if the identity of the process it has to compete for (namely, proxy_fori) is greater than both maxidi (the identity of the process on behalf of which pi was previously competing) and the identity id it has just received. If it is the case, pi updates maxidi and starts a new round. Otherwise, proxy_fori is not the highest identity. Consequently, as pi should compete for an identity that cannot be elected, it stops competing.
    
    .. image:: figures/Screen1.jpg
      :width: 400

**The Dolev-Klawe-Rodeh Algorithm:**

The Dolev-Klawe-Rodeh :ref:`Algorithm <DolevKlaweRodehAlgorithm>` [Raynal2013]_ . The algorithm presented below is due to D. Dolev, M. Klawe, and M.Rodeh (1982). As in the other election algorithms, initially all processes compete to be elected as a leader, and execute consecutive rounds to that end. During each round, at most half of the processes that are competitors remain competitors during the next round.

.. _DolevKlaweRodehAlgorithm:

    .. code-block:: RST
        :linenos:
        :caption: The Dolev-Klawe-Rodeh Algorithm [Raynal2013]_.
                
        when START() is received do
            competitori ←true; maxidi ←idi ; send ELECTION(1, idi ).
       
        when ELECTION(1, id) is received do
            if (¬competitori)
                then send ELECTION(1, id)
                else if (id != maxidi ) 
                     then send ELECTION(2, id); proxy_fori←id
                     else send ELECTED(id, idi )
                    end if
            end if.
        when ELECTION(2, id) is received do
            if (¬competitori )
                then send ELECTION(2, id)
                else if (proxy_fori > max(id, maxidi ))
                then maxidi ←proxy_fori ; send ELECTION(1, proxy_fori )
                else competitori←false
              end if
            end if.
        when ELECTED(id1, id2) is received do
             leaderi ←id1; donei ←true; electedi ←(id1 = idi);
             if (id2 != idi ) then send ELECTED(id1, id2) end if.

**Correctness:**
    
*Termination (liveness)*: When pi updates the greatest identity known by pi and starts a new round, pi should compete for an identity that cannot be elected, it stops competing. [Raynal2013]_.

*Correctness*: Each process receives alternately a message ELECTION(1,-) followed by a message ELECTION(2,-). As the channels are FIFO, it follows that the numbers 1 and 2 used to tag the messages are useless: A message ELECTION() needs to carry only a process identifier, and consequently, there are only n different messages ELECTION(). [Raynal2013]_.

**Complexity:**

1. **Time Complexity**  The Dolev-Klawe-Rodeh :ref:`Algorithm <DolevKlaweRodehAlgorithm>` The Dolev-Klawe-Rodeh algorithm :ref:`Algorithm <DolevKlaweRodehAlgorithm>` The time complexity measures the number of rounds or steps required for the algorithm to complete its execution. Each round typically involves processes exchanging messages and performing local computations. The number of processes is defined as N. Each round in the algorithm involves each process sending and receiving messages to and from other processes. Therefore, the time complexity is directly proportional to the number of messages exchanged in each round.the time complexity of the algorithm in terms of the number of messages exchanged is linear: O(E)
2. **Message Complexity:** The Dolev-Klawe-Rodeh :ref:`Algorithm <DolevKlaweRodehAlgorithm>` The message complexity of the algorithm can be analyzed in terms of the the number of processes (N). Each process needs to send a request message to every other process in the network. The message complexity of the algorithm is O(NlogN).

**Echo Algorithm with Extinction Algorithm:**

Echo algorithm with extinction processes propagate an "echo" message through the network. Echo messages are forwarded among processes, ensuring every process becomes aware of others' status or candidacy. Upon receiving echo messages from all neighbors, a process confirms its status or candidacy.  Processes that haven't heard from any higher-priority process declare themselves as leaders and broadcast victory messages.The algorithm concludes when all processes have confirmed their status or acknowledged the leader's victory, signaling successful termination or leader election.

Suppose a process p in a wave q is hit by a wave r.
If q<r then p makes the sender its parent, switches to the wave r.
If q>r then p continues with the wave tagged with q.
If q=r then p treats the incoming message according to the echo algorithm of the wave q.
If the wave tagged with p completes by executing a decide event at p, then p becomes the leader.

 .. image:: figures/Screen3.jpg
      :width: 400

.. _EchoAlgorithmwithExtinction:
 
    .. code-block:: RST
        :linenos:
        :caption: Echo Algorithm with Extinction [Fokking2013]_.

        nat receivedp;
        pro parentp;
        If p is the iniaator
        send<wave> to each r Neighborsp;
        If p receives <wave> from a neighborr mess-queue
        received ← receivedp+1;
        if parentp=  and p is a noninitiator then
            parentp ← q;
            if|Neighborsp|>1 then
                send<wave> to each r Neighborsp \ {q};
            else
                send<wave> to q;
            end if
        else if receivedp = |Neighborsp| then
            if parentp =  then
                send <wave> to parentp;
            else
                decide;
            end if
        end if

**Correctness:**
    
*Termination (liveness)*: The term "extinction" refers to the algorithm's termination, indicating that every process has completed its role in the termination detection or leader election process.
    
*Correctness*: The wave of the initiator with the largest ID is guaranteed to complete, because each process will eventually switch to that wave. 
    
**Complexity:**

1. **Time Complexity**  Echo algorithm with extinction :ref:`Algorithm <EchoAlgorithmwithExtinction>` The worst case message complexity of the algorithm is O(NE) where there are at most N waves, at most 2E message in each wave.
2. **Message Complexity:** Echo algorithm with extinction :ref:`Algorithm <EchoAlgorithmwithExtinction>` The worst case message complexity of the algorithm is O(NE), at most 2E message in each wave.
 
.. [Fokking2013] Wan Fokkink, Distributed Algorithms An Intuitive Approach, The MIT Press Cambridge, Massachusetts London, England, 2013
.. [Tel2001] Gerard Tel, Introduction to Distributed Algorithms, CAMBRIDGE UNIVERSITY PRESS, 2001
.. [Lamport1985] Leslie Lamport, K. Mani Chandy: Distributed Snapshots: Determining Global States of a Distributed System. In: ACM Transactions on Computer Systems 3. Nr. 1, Februar 1985.
.. [Raynal2013] Michel Raynal, Distributed Algorithms for Message-Passing Systems, Springer, 2013