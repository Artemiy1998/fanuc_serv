import unittest
import math
import time
import socket
def converByteToInt(data):
    udata = data.decode("utf-8")
    new_data_str = udata.split()
    new_data_int = [float(item) for item in new_data_str]
    return new_data_int
def dataRes(x,y,z,w,p,r,v,cntrl):
    dataToSend = str(x)+' '+str(y)+' '+str(z)+' '+str(w)+' '+str(p)+' '+str(r)
    data_to_send = '1'+' '+dataToSend+' '+str(v)+' '+str(cntrl)
    return data_to_send


def chek(data_float, x,y,z,w,p,r,eps):
    flag = False
    if math.fabs(data_float[0] - x) < eps and math.fabs(data_float[1] - y) < eps and math.fabs(
        data_float[2] - z) < eps and  math.fabs(data_float[3]-w) <eps and math.fabs(data_float[4]-p) <eps and math.fabs(data_float[5]-r) <eps:
        flag = True
    return flag

class TestServModel(unittest.TestCase):
    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 9092))
        pass

    def test_RobotControl1_1_1(self):
        x = 1085.
        y = 0.
        z = 940.
        w = 180.
        p = 0.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x,y,z,w,p,r,v,cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float,x,y,z,w,p,r,eps)
        self.assertEqual(flages,True,'ok')

    def test_RobotControl1_1_2(self):
        x = 985.
        y = 100.
        z = 940.
        w = 180.
        p = 0.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_3(self):
        x = 985.
        y = 0.
        z = 1140.
        w = 180.
        p = 0.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_4(self):
        x = 985.
        y = 0.
        z = 940.
        w = 90.
        p = 0.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_5(self):
        x = 985.
        y = 0.
        z = 940.
        w = 180.
        p = 45.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_6(self):
        x = 985.
        y = 0.
        z = 940.
        w = 180.
        p = 0.
        r = 45.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_7(self):
        x = 1085.
        y = 0.
        z = 940.
        w = 180.
        p = 0.
        r = 0.
        v = 32.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def test_RobotControl1_1_7(self):
        x = 785.
        y = 0.
        z = 940.
        w = 180.
        p = 0.
        r = 0.
        v = 80.
        cntrl = 0.
        eps = 0.001
        dataStr_to_send = dataRes(x, y, z, w, p, r, v, cntrl)
        self.sock.send(dataStr_to_send.encode())
        data = self.sock.recv(1024)
        data_float = converByteToInt(data)
        print(data_float)
        flages = chek(data_float, x, y, z, w, p, r, eps)
        self.assertEqual(flages, True, 'ok')

    def tearDown(self):
        self.sock.close()
        pass

if __name__ == "__main__":
    unittest.main()
