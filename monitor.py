import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import socket,time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(60.0)
server.bind(('', 3333))

fig = plt.gcf()
plt.style.use('fivethirtyeight')
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('Hall')
plt.xlabel('Time')
plt.title('Dynamic line graphs')
t=time.time()
x_values = []
y_values = []
counter = 0

def data_gen(i):
    global counter
    try:
        counter=1+counter
        x_values.append(time.time()-t)
        data, addr = server.recvfrom(1024)
        if not data:
            return
        data = data.decode().replace("\x00",'')
        Data=float(data)
        y_values.append(Data)
        print('Reply[' + addr[0] + ':' + str(addr[1]) + '] - ' + data)
        reply = 'OK: ' + data
        server.sendto(reply.encode(), addr)
        if counter >100:
            x_values.pop(0)
            y_values.pop(0)
            plt.cla()
        plt.plot(x_values, y_values,color='r')    
        time.sleep(0.25)    
    except Exception as e:
        print('Running server failed:{}'.format(e))

        
ani = FuncAnimation(fig,data_gen,interval=100)
plt.tight_layout()
plt.show()
