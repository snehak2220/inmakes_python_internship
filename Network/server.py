import socket
from tkinter import *


def send(listbox,entry):
    message=entry.get()
    listbox.insert('end','Server:',message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))
def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end','Client:',message_from_client.decode('utf-8'))
    print("client:")

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
sende=Button(root,text='Send',command=lambda :send(listbox,entry))
sende.pack(side=BOTTOM)
recev=Button(root,text='Receive',command=lambda :receive(listbox))
recev.pack(side=BOTTOM)
root.title("server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)

client, address = s.accept()
#while True:
    #message=input("Server:")
   #


root.mainloop()