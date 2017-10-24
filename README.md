# tock-ping
Ping app used to verify the Tock OS 6LoWPAN/IEEE 802.15.4 stack implementation. Forwards IPv6 ICMP packets to and from the Internet via Linux.

End goal is a setup like this:

```
[imix running Tock OS]  )))  (((  [imix running Tock OS] <----> [Raspberry Pi running Linux] <----> Internet
```

The second imix will transfer packets to and from the Raspberry Pi using SLIP.

## Files in this repo:
- [`serial_log.py`](https://github.com/mog96/tock-ping/blob/master/serial_log.py): Reads from serial on the Raspberry Pi and prints to the console.
- [`tun_ping.py`](https://github.com/mog96/tock-ping/blob/master/tun_ping.py): A first stab at stuffing raw bytes into a Linux network interface by setting up a tunnel device.
- [`setup_interfaces.sh`](https://github.com/mog96/tock-ping/blob/master/setup_interfaces.sh): Sets up wpan and lowpan interfaces on the Raspberry Pi.

## Files related to this repo:
- [`radio_rx_slip_tx/`](https://github.com/mog96/tock/tree/mog-radio-slip/userland/examples/radio_rx_slip_tx): Tock userspace program that implements SLIP in one direction. Writes all radio packets received to serial using `printf()`.
- [`lowpan_frag_dummy.rs`](https://github.com/ptcrews/tock/blob/mog-ptc-ping/boards/imix/src/lowpan_frag_dummy.rs): Tock kernel space program that sends ICMP packets over IEEE 802.15.4.
- [`pyCCSniffer`](https://github.com/ptcrews/pyCCSniffer): Uses a Texas Instruments CC2531emk USB dongle to sniff packets, dissect them, and stuff them into a WPAN interface on Linux. @ptcrews and I were using this to develop the outbound side of the ping app (the TI dongle can only receive IEEE 802.15.4 frames, not transmit).
