from sympy import symbols, Eq, solve, Sum
import websockets, time, asyncio
from pendulum import Pendulum

async def recibir_mensajes(websocket, path):
    try:
        async for mensaje in websocket:
            print("Mensaje recibido:", mensaje)

            # a, b, c = symbols('a b c')
            # ecuacion1 = Eq(a + 2*b + c**2, 18)
            # ecuacion2 = Eq(a + 1*b + c, 6)
            # ecuacion3 = Eq(3*a + 4*b + 2*c, 10)
            # soluciones = solve((ecuacion1, ecuacion2, ecuacion3), (b, a, c))
            # try:
            #     for key,element in soluciones.items():
            await websocket.send(f"HOLA {mensaje}") 

            #         # print(element)
            # except AttributeError:
            #     for i in soluciones:
            #         # print(i)
            #         await websocket.send(f"{i}")

    except websockets.ConnectionClosed:
        print("Conexión cerrada")

async def main():
    servidor = await websockets.serve(recibir_mensajes, "localhost", 8025)
    await servidor.wait_closed()

# Ejecutar el bucle de eventos de asyncio
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

i = symbols('i')
expresion = i**2
sumatoria = Sum(expresion, (i, 1, 10))  # Sumar i^2 desde i=1 hasta i=10
resultado = sumatoria.doit()
print("El resultado de la sumatoria es:", resultado)