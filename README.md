# tock-ping
Used to verify the Tock OS 6LoWPAN/IEEE 802.15.4 stack implementation by forwarding IPv6 ICMP packets to and from the Internet via Linux.

End goal is a setup like this:

```
[imix running Tock OS] ))) ((( [imix running Tock OS] <----> [Raspberry Pi running Linux] <----> Internet
```

The second imix will transfer packets to and from the Raspberry Pi using SLIP.

## Files in this repo:
- [`serial_log.py`](https://github.com/mog96/tock-ping/blob/master/serial_log.py): Reads from serial on the Raspberry Pi and prints to the console.
- [`tun_ping.py`](https://github.com/mog96/tock-ping/blob/master/tun_ping.py): An first stab at stuffing packets into a Linux network interface by setting up a tunnel device.

## Files related to this repo:
- [`radio_rx_slip_tx`](https://github.com/mog96/tock/tree/mog-radio-slip/userland/examples/radio_rx_slip_tx): Tock userspace program that implements SLIP in one direction. Writes all radio packets received to serial using `printf()`.
