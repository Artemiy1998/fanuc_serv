import socket
import time

def converByteToInt(data):
    udata = data.decode("utf-8")
    new_data_str = udata.split()
    new_data_int = [float(item) for item in new_data_str]
    return new_data_int

def parse1(data):
    new_data_int = converByteToInt(data)
    if new_data_int[0] == 1:
        global coor_x
        coor_x = new_data_int[1]
        global coor_y
        coor_y = new_data_int[2]
        global coor_z
        coor_z = new_data_int[3]
        global coor_w
        coor_w = new_data_int[4]
        global coor_p
        coor_p = new_data_int[5]
        global coor_r
        coor_r = new_data_int[6]
        global seg
        seg = new_data_int[7]
        global ControlParam
        ControlParam = new_data_int[8]
    else:
        pass

def parse2(data):
    new_data_int = converByteToInt(data)
    if new_data_int[0] == 2:
        global CoordinateSystem
        CoordinateSystem = new_data_int[1]
        global TermType
        TermType = new_data_int[2]
        global MotionType
        MotionType = new_data_int[3]
        global Nowait
        Nowait = new_data_int[4]
        global TypeOfReturnCoordinate
        TypeOfReturnCoordinate = new_data_int[5]
        global eps
        eps = new_data_int[6]
        global ControlParam
        ControlParam = new_data_int[8]
    else:
        pass
def WorkToShvat(typeOfSchvat):
    if typeOfSchvat==2:
        client_sock.send('Schvat 1'.encode())
    elif typeOfSchvat == 3:
        client_sock.send('Schvat 3'.encode())
    elif typeOfSchvat==4:
        client_sock.send('Schvat 4'.encode())
    time.sleep(1)
def MoveToPoint(client_sock):
    client_sock.send('1085 0 940 180 0 0 '.encode())
    time.sleep(1)
def HomePosition(sock):
    client_sock.send('Home'.encode())
    time.sleep(1)
    sock.close()
coor_x = 0
coor_y = 0
coor_z = 0
coor_w = 0
coor_p = 0
coor_r = 0
seg = 32
ControlParam = 0
CoordinateSystem = 2
TypeOfMotion = 0
TypeOfReturnCoordinate = 0
eps = 0
ses = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9092))
sock.listen(10)
while True:
    ses +=1

    client_sock, addr_sock = sock.accept()
    print(ses,"   ","Connect", addr_sock)
    while True:
        data = client_sock.recv(1024)
        print(type(data))
        data_list = converByteToInt(data)
        print(data_list)
        if data_list[0] == 1: #если пришел первый пакет, то двигаем
            parse1(data)
            if ControlParam !=1:
                WorkToShvat(ControlParam)
                MoveToPoint(client_sock)
            else:
                HomePosition(client_sock)
                print("Disconnect", addr_sock)
                client_sock.close()


        elif data_list[0] == 2:#если второй меняем параметры
            parse2(data)

            if CoordinateSystem >4:
                client_sock.send('Uncorrect coordinate system'.encode())
        elif data_list[0]==0:
            pass
            #надо дописать
        else:
            pass
        break
    print("close connection")




