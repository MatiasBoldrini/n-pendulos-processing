import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8025/john"  # Reemplaza con la URL y el puerto del servidor WebSocket de Processing
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Ingrese un mensaje para enviar al servidor WebSocket de Processing: ")
            await websocket.send(message)
            print(f"Mensaje enviado al servidor: {message}")

asyncio.get_event_loop().run_until_complete(send_message())
