from sympy import symbols, Eq, solve
import asyncio
import websockets, time
async def send_message():
    uri = "ws://localhost:8025/john"  # Reemplaza con la URL y el puerto del servidor WebSocket de Processing
    async with websockets.connect(uri) as websocket:
        while True:
            mensaje = ''
            mensaje_recibido = await websocket.recv()
            print(f"< {mensaje_recibido}")
            await websocket.send('Hola desde python')
if __name__ == '__main__':
    while True:
        try:
            asyncio.get_event_loop().run_until_complete(send_message())
        except OSError:
            time.sleep(1)
            print(f"No se pudo enviar el mensaje. Ejecute el servidor WebSocket de Processing y vuelva a intentarlo.")

    a, b, c = symbols('a b c')
    ecuacion1 = Eq(a + 2*b + c**2, 18)
    ecuacion2 = Eq(a + 1*b + c, 6)
    ecuacion3 = Eq(3*a + 4*b + 2*c, 10)
    soluciones = solve((ecuacion1, ecuacion2, ecuacion3), (b, a, c))
    try:
        for key,element in soluciones.items():
            print(key, element)
    except AttributeError:
        for i in soluciones:
            print(i)