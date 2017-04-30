import serial
#from ubidots import ApiClient
#api = ApiClient(token='09b329cb78c54feddc84840a047e615d20669d20')
#uTemperatura = api.get_variable('590571bf762542534bbed865')
#uHumedad = api.get_variable('5590571b4762542534bbed7c6')
#uVelocidad = api.get_variable('590571e9762542534807e40e')
#uAlarma = api.get_variable('590578f07625425349d0bae9')
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACa6c26142499210593955c9d94d2f4a60"
# Your Auth Token from twilio.com/console
auth_token  = "362cf7815973e57a4a389ccf490ce1ce"

client = Client(account_sid, auth_token)

ser = serial.Serial('/dev/cu.usbmodem1411', 9600) #:v
time.sleep(2)
while true:
    dataAll = ser.readline()
    dataSplit = dataAll.split(" ")
    temperatura = float(dataSplit[0])
    humedad = float(dataSplit[1])
    velocidad = float(dataSplit[2])
    alarma = float(dataSplit[3])
    if velocidad >= 5:
        text = "fuerte"
    else if velocidad<= 1:
        text = "suave"
    else:
        text = "normal"
    if int(float(dataSplit[3])) =  1 && sent!= True:
        message = client.messages.create(
            to="+56977788092",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message.sid)
        message1 = client.messages.create(
            to="+56997161207",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message1.sid)
        message2 = client.messages.create(
            to="+56972923267",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message2.sid)
        message3 = client.messages.create(
            to="+56971026348",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message3.sid)
        message4 = client.messages.create(
            to="+56942427077",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print (message4.sid)
        message5 = client.messages.create(
            to="+56930247080",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message5.sid)
        message6 = client.messages.create(
            to="+56949878426",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message6.sid)
        message7 = client.messages.create(
            to="+56966793790",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message7.sid)
        message8 = client.messages.create(
            to="+56971039083",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message8.sid)
        message9 = client.messages.create(
            to="+56979139524",
            from_="+56964590317",
            body="Se a detectado un posible foco de incendio en el sector de aula de la utfsm, se recomienda tomar precauciones, el viento es "+text)
        print(message9.sid)
        sent = True
