import oscP5.*;
import netP5.*;
OscP5 oscP5;
NetAddress dest;

int xPos=200;
int xDir=0;
int yDir=0;
int yPos=200;
int speed=1;

void setup()
{
  oscP5 = new OscP5(this, 9000);
  size (400,400);
  smooth();
  background(0);
  noStroke();
  fill(0,255,0);
}

//This is called automatically when OSC message is received
void oscEvent(OscMessage theOscMessage) {
 if (theOscMessage.checkAddrPattern("/wek/outputs")==true) {
        float move = theOscMessage.get(0).floatValue();//get this parameter
        move = (int)move;
        if (move == 1){
           yDir = 1; 
        }else if(move == 2){
           yDir = -1; 
        }else if(move == 3){
           xDir = -1; 
        }else{
          xDir = 1;
        }
 }
}

void draw()
{
  background(0);
  ellipse(xPos, yPos, 40, 40);
  xPos=xPos+xDir*speed;
  yPos=yPos+yDir*speed;
  if (xPos>width-20 || xPos<20)
  {
    xDir=-xDir;
  }
}