import socket		
import threading
from queue import Queue

print_lock = threading.Lock()

def inp_target():
    input("Website: ")

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port {} is open'.format(port))
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

if __name__ == '__main__':
    port = int(input("Port: "))
    port_range = int(port+1)
    q = Queue()
    for x in range(30):
        t =threading.Thread(target=threader)
        t.daemon = True
        t.start()
    for worker in range(port,port_range):
        q.put(worker)
    q.join()

