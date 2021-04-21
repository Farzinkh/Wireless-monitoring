import os
import re
import sys
import socket,time
from builtins import input
from matplotlib import style
from threading import Event, Thread
import matplotlib.animation as animation
from __future__ import print_function, unicode_literals



# -----------  Config  ----------
PORT = 3333
INTERFACE = 'eth0'
# -------------------------------



style.use('fivethirtyeight')


class UdpServer:

    def __init__(self, port, family_addr, persist=False):
        self.port = port
        self.family_addr = family_addr
        self.socket = socket.socket(family_addr, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(60.0)
        self.shutdown = Event()
        self.persist = persist
        self.fig=plt.figure()
        self.ax1= self.fig.add_subplot(1,1,1)
        self.time=time.time()
        self.data=0
        
    def __enter__(self):
        try:
            self.socket.bind(('', self.port))
        except socket.error as e:
            print('Bind failed:{}'.format(e))
            raise

        print('Starting server on port={} family_addr={}'.format(self.port, self.family_addr))
        self.server_thread = Thread(target=self.run_server)
        self.server_thread.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.persist:
            sock = socket.socket(self.family_addr, socket.SOCK_DGRAM)
            sock.sendto(b'Stop', ('localhost', self.port))
            sock.close()
            self.shutdown.set()
        self.server_thread.join()
        self.socket.close()

    def run_server(self):
        while not self.shutdown.is_set():
            try:
                data, addr = self.socket.recvfrom(1024)
                if not data:
                    return
                self.data = data.decode()
                ani = animation.FuncAnimation(self.fig, self.plot, interval=1000)
                plt.show()
                print('Reply[' + addr[0] + ':' + str(addr[1]) + '] - ' + self.data)
                reply = 'OK: ' + self.data
                self.socket.sendto(reply.encode(), addr)
            except socket.error as e:
                print('Running server failed:{}'.format(e))
                raise
            if not self.persist:
                break
    def plot(self):
        xs = []
        ys = []
        xs.append(float(self.data))
        ys.append(float(time.time()-self.time()))
        self.ax1.clear()
        self.ax1.plot(xs, ys)


if __name__ == '__main__':
    if sys.argv[1:] and sys.argv[1].startswith('IPv'):     # if additional arguments provided:
        # Usage: example_test.py <IPv4|IPv6>
        family_addr = socket.AF_INET6 if sys.argv[1] == 'IPv6' else socket.AF_INET
        with UdpServer(PORT, family_addr, persist=True) as s:
            print(input('Press Enter to stop the server...'))
    else:
        print("wrong parameter")
