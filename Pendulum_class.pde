class pendulum {
  float mass;
  float lineLength;
  float posAngle;
  float vel; 
  
  pendulum (float tempMass, float tempLineLength, float tempPosAngle,float tempVel){
    mass=tempMass;
    lineLength=tempLineLength;
    posAngle=tempPosAngle;
    vel=tempVel;
  }
  float posX(){
    return lineLength*sin(posAngle);
  }
  float posY(){
    return lineLength*cos(posAngle);
  }
  float mass(){
    return mass;  
    }
  float posAngle(){
    return posAngle;  
    }
  float vel(){
    return vel;  
    }
}
