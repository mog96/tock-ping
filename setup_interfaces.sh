#! /bin/bash
modproble fakelb
iwpan dev wpan0 set pan_id 0xabcd
iwpan dev wpan1 set pan_id 0xabcd
ip link add link wpan0 name lowpan0 type lowpan
ip link add link wpan1 name lowpan1 type lowpan
ip link set wpan0 up
ip link set wpan1 up
ip link set lowpan0 up
ip link set lowpan1 up
