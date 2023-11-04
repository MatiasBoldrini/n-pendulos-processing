import websockets.*;

WebsocketServer ws;
int now;
float x,y;
pendulum[] pendulums = new pendulum[100];
float[] posX = new float[101];
float[] posY = new float[101];
void setup() {
    ws = new WebSocketClient(this, "ws://localhost:8025/john"); // Reemplaza la URL con la dirección del servidor WebSocket al que te quieres conectar
    fullScreen();
    posX[0] = 0;
    posY[0] = 0;
    for (int i = 0; i < 100; i++) {
        pendulums[i] = new pendulum(50 / pow(2, i),10.7, PI / 4,0.01);//pow(2, i) //perfect length 10.7
        posX[i + 1] = posX[i] + pendulums[i].posX();
        posY[i + 1] = posY[i] + pendulums[i].posY();
        //println(posY[i]);
    }
    now = millis();
}
void draw() {
    background(#DE1B9A);
    stroke(0);
    strokeWeight(4);
    translate(width / 2,0);//height/2
    for(int i = 0;i < 100;i++) {
        	line(posX[i],posY[i],posX[i + 1],posY[i + 1]);
        	fill(0);
        	ellipse(posX[i + 1],posY[i + 1],2,2);//pendulums[i].mass,pendulums[i].mass
        	posX[i+ 1] = posX[i] + pendulums[i].posX();
        	posY[i+ 1] = posY[i] + pendulums[i].posY();
        }
    if (millis()>now + 1000) {
        ws.sendMessage("Envio desde processing");
        now = millis();
	}
    	pendulums[0].posAngle += pendulums[0].vel;
    }
void webSocketServerEvent(String msg) {
    println(msg);
}