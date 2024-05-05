# Lab-0x01
## Overview
<b>Task</b>: 
* perform Voltage Fault Injection Attacks against general purpose microcontroller (ATMEGA328P)
* disclosing secret data contained within a read-protected memory region

<b>Structure</b>:
1. Understanding the DuT:
    * Read the specification and run the target
    * Disassemble the Firmware to find potential targets and secrets
2. Assemble the Glitcher:
    * Implement a hardware design dedicated to Voltage Fault Injection
    * Put the Fault Injection circuitry together on a bread board
3. Voltage Fault Injection:
   * Characterize the DuT’s fault response
   * Break the DuT’s authentication scheme and access the secure 
memory

make use of the binary firmware

Ask about their authorization status (AUTHORIZED, UNAUTHORIZED)
• Request to be authorized by providing a password
• Access their password and seed in secure memory once AUTHORIZED
• Ping the wallet to see if it is up and running

get owners' seed-phradea
takes place via 
RS233 (UART) 

[youtube](https://www.youtube.com/watch?v=6Pf3pY3GxBM&t=101s) <br>
[file](https://www.synacktiv.com/publications/how-to-voltage-fault-injection)