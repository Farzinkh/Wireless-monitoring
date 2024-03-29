## ESP32 UDP Client & Real time Monitoring on server

The application creates UDP socket and sends message to the predefined port and IP address. After the server's reply, the application prints received reply as ASCII text, waits for 2 seconds and sends another message which can be int or float type data and finally you can see resault on monitoring graph for example in this project we will stream internal hall sensor readed values as long as we need.

## How to use monitor

In order to start UDP server that communicates with UDP Client, run `python monitor.py` and push your ESP32 reset button you can cancel monitoring by just closeing monitor by pushing exit button.

### Screenshots
![Screenshot for internal hall sensor](https://github.com/Farzinkh/Wireless-monitoring/blob/master/Screenshot%20.png?raw=true "Screenshot for internal hall sensor")

## Hardware Required

This project can be run on any commonly available ESP32 development board.

## Configure the project

```
idf.py menuconfig
```

Set following parameters under project Configuration Options:

* Set `IP version` to be IPV4 or IPV6.

* Set `IPV4 Address` in case your chose IP version IPV4 above.

* Set `IPV6 Address` in case your chose IP version IPV6 above.

* Set `Port` number that represents remote port the client will send data and receive data from.

Configure Wi-Fi or Ethernet under "Example Connection Configuration" menu. See "Establishing Wi-Fi or Ethernet Connection" section in [examples/protocols/README.md](../../README.md) for more details.


## Build and Flash

Build the project and flash it to the board, then run monitor tool to view serial output:

```
idf.py -p PORT flash monitor
```

(To exit the serial monitor, type ``Ctrl-]``.)

See the Getting Started Guide for full steps to configure and use ESP-IDF to build projects.


## Troubleshooting

Start server first, to receive data sent from the client (application).
