#!/bin/bash
a=$(cat /proc/net/arp | grep "[:digit:]*\." | sed -e 's/ .*//')
echo $a >> ip_addresses.txt
