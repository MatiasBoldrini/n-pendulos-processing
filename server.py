import asyncio
import websockets, time
# from scipy.integrate import odeint
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.complex_ode.html
async def send_message():
    uri = "ws://localhost:8025/john"  # Reemplaza con la URL y el puerto del servidor WebSocket de Processing
    async with websockets.connect(uri) as websocket:
        while True:
            mensaje = ''
            mensaje_recibido = await websocket.recv()
            if mensaje_recibido:
                
                await websocket.send('Recibido')
            print(f"< {mensaje_recibido}")
if __name__ == '__main__':
    while True:
        try:
            asyncio.get_event_loop().run_until_complete(send_message())
        except OSError:
            time.sleep(1)
            print(f"No se pudo enviar el mensaje. Ejecute el servidor WebSocket de Processing y vuelva a intentarlo.")