# tock-ping
Used to verify the Tock OS 6LoWPAN/IEEE 802.15.4 stack implementation by forwarding IPv6 ICMP packets to and from the Internet via Linux.

End goal is a setup like this:

```
[imix running Tock OS] ))) ((( [imix running Tock OS] <----> [Raspberry Pi running Linux] <----> Internet
```

The second imix will transfer packets to and from the Raspberry Pi using SLIP. A one-way SLIP implementation lives [here](https://github.com/mog96/tock/tree/mog-radio-slip/userland/examples/radio_rx_slip_tx). It is written in userspace, and writes received packets over serial using `printf()`.

Files in this repo:
- [`serial_log.py`](https://github.com/mog96/tock-ping/blob/master/serial_log.py): Reads from serial on the Raspberry pi and prints to the console.
- 
