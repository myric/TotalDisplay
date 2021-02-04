import gifAnimation.*;

//PImage img;  // Declare variable "a" of type PImage
//PImage[] allFrames;
Gif giphy;

void setup() {
  size(640, 360);
  // The image file must be in the data folder of the current sketch 
  // to load successfully
  //img = loadImage("../200.gif");  // Load the image into the program
  //allFrames = Gif.getPImages(this, "../200.gif");
  giphy = new Gif(this, "../200.gif");
  giphy.play();
}

void draw() {
  // Displays the image at its actual size at point (0,0)
  //image(img, 0, 0);
  // Displays the image at point (0, height/2) at half of its size
  //image(img, 0, height/2, img.width/2, img.height/2);
  
  image(giphy, 10, 10);
}
