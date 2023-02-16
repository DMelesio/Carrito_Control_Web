import network
import socket
from time import sleep
import machine
from machine import Pin

#RED WiFi
ssid = 'INFINITUMB70C_2.4_EXT'
password= 'UM7YAsMJ2p'
#ssid = 'INFINITUMusrb'
#password = 'ca34300df8'

#Asignación de Pins!
MotorA_Adelante = Pin(5, Pin.OUT)
MotorA_Atras = Pin(4, Pin.OUT)
MotorB_Adelante = Pin(3, Pin.OUT)
MotorB_Atras = Pin(2, Pin.OUT)

enA = Pin(6, Pin.OUT)
enB = Pin(7, Pin.OUT)

 

def adelante():
    enA(1)  
    enB(1) 
    
    MotorA_Adelante.value(1)
    MotorB_Adelante.value(1)
    MotorA_Atras.value(0)
    MotorB_Atras.value(0)
    
def reversa():
    enA(1)  
    enB(1)
        
    MotorA_Adelante.value(0)
    MotorB_Adelante.value(0)
    MotorA_Atras.value(1)
    MotorB_Atras.value(1)

def stop():
    enA(1)  
    enB(1)
    
    MotorA_Adelante.value(0)
    MotorB_Adelante.value(0)
    MotorA_Atras.value(0)
    MotorB_Atras.value(0)

def izquierda(): #rueda izquierda detenida
    enA(0)  
    enB(1)
    
    MotorA_Adelante.value(1)
    MotorB_Adelante.value(1)
    MotorA_Atras.value(0)
    MotorB_Atras.value(0)
    
def derecha(): #rueda derecha detenida
    enA(1)  
    enB(0)
    
    MotorA_Adelante.value(1)
    MotorB_Adelante.value(1)
    MotorA_Atras.value(0)
    MotorB_Atras.value(0)

def giroderecha(): #una rueda adelante, la otra atras
    enA(1)  
    enB(1)
    
    MotorA_Adelante.value(1)
    MotorB_Adelante.value(0)
    MotorA_Atras.value(0)
    MotorB_Atras.value(1)
    
def giroizquierda(): #una rueda adelante, la otra atras
    enA(1)  
    enB(1)
    
    MotorA_Adelante.value(0)
    MotorB_Adelante.value(1)
    MotorA_Atras.value(1)
    MotorB_Atras.value(0)
    
def reversaizquierda():
    enA(1)  
    enB(0)
    
    MotorA_Adelante.value(0)
    MotorB_Adelante.value(0)
    MotorA_Atras.value(0)
    MotorB_Atras.value(1)
    
def reversaderecha(): #rueda izquierda detenida
    enA(0)  
    enB(1)
    
    MotorA_Adelante.value(0)
    MotorB_Adelante.value(0)
    MotorA_Atras.value(1)
    MotorB_Atras.value(0)
    
#Detener el carrito
stop()
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Esperando Conexión...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Conectado a {ip}')
    return ip
    
def open_socket(ip):
    # Open socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    #Template HTML
    html = f"""
            
    <!DOCTYPE html>
<html lang="es">
    
<head>
    <title>CONTROL</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="autor" content="Daniela Melesio">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	
</head>
    
<header id="headr" style="width: 100%; height: 40px; position: static; background: black; font-family:'Josefin Sans', sans-serif; padding: 10px 10px 50px 0; ">
        <section id="TOP">
            <div id="titulo">
                <ul>
                    <li>
                        <h1 style="text-align: center; color: #FFD700; font-size:1.5em">Controles Wireless Car</h1>
                    </li>
                </ul>
            </div>
        </section>
</header>
    
<body style="margin: 0; padding: 0; background-color: black;">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.4/socket.io.js"></script> <!-- include socket.io client side script -->
    <script> var socket = io(); //load socket.io-client and connect to the host that serves the page </script>
    
    <!--Inicio Controles-->
    <section id="controles" style="width: 100%; height: 300px;
        background: url(https://i.pinimg.com/originals/20/8a/8d/208a8dd88aa96f002b394b5befa6bc13.jpg) 50% 0 ; background-size: cover; background-position:center;">
    <div id="control" style="position: relative; top: 20px; width: 60%; height: 90%; margin: 0 auto; background-color: rgba( 26, 6, 63, 0.5); border-radius: 50px;">  
        <center>
            <form action="./adelante">              
                <input type="submit" value=" " 
                style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/arriba.png); background-color: transparent;
                border:none; width:57px; height:57px;"/> 
            </form>

            <table >
                <tr>
                    <td>
                        <form action="./giroizquierda">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/GIzqu.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/> 
                        </form>
                    </td>
                    <td>
                        <form action="./izquierda">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/izqu.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/> 
                        </form>
                    </td>
        
                    <td>
                        <form action="./stop">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/stop.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/> 
                        </form>
                    </td>
                    <td>
                        <form action="./derecha">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/derecha.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/>
                        </form>
                    </td>
                    <td>
                        <form action="./giroderecha">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/GDere.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/>
                        </form>
                    </td>
                </tr>
            </table>
            
            <form action="./reversa">
            <input type="submit" value=" " 
                style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/reversa.png); background-color: transparent;
                border:none; width:57px; height:57px;"/>
            </form>
            
                <table>
                <tr>
                    <td><form action="./reversaizquierda">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/revizqu.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/>
                        </form></td>
                    <td><form action="./reversaderecha">
                        <input type="submit" value=" " 
                        style="background-image: url(https://raw.githubusercontent.com/DMelesio/css-carrito/main/revdere.png); background-color: transparent;
                        border:none; width:57px; height:57px;"/>
                        </form></td>
                </tr>
                </table>
        </center>
    </div>
    </section><!--controles-->
</body>

</html>
            """
    return str(html)

def serve(connection):
    #Inicio del servidor
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/adelante?':
            adelante()
        elif request =='/izquierda?':
            izquierda()
        elif request =='/stop?':
            stop()
        elif request =='/derecha?':
            derecha()
        elif request =='/reversa?':
            reversa()
        elif request =='/giroderecha?':
            giroderecha()
        elif request =='/giroizquierda?':
            giroizquierda()
        elif request =='/reversaderecha?':
            reversaderecha()
        elif request =='/reversaizquierda?':
            reversaizquierda()
            
        html = webpage()
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()