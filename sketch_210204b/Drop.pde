// Example 10-7: Drops one at a time

import gifAnimation.*;

class Drop {

  PImage img;
  Gif giphy;
  int option;
  
  float x, y;   // Variables for location of raindrop
  float speed; // Speed of raindrop
  color c;
  float r;     // Radius of raindrop

  Drop() {
    r = 32;                 // All raindrops are the same size
    x = random(width);     // Start with a random x location
    //y = -r*4;              // Start a little above the window
    y = -r;
    speed = random(1, 5);   // Pick a random speed
    c = color(255, 255, 255); // Color
    img = loadImage("../alt.jpg");
    option = 0;
  }
  
  Drop(PApplet parent) {
    r = 32;                 // All raindrops are the same size
    x = random(width);     // Start with a random x location
    //y = -r*4;              // Start a little above the window
    y = -r;
    speed = random(1, 5);   // Pick a random speed
    c = color(255, 255, 255); // Color
    
    giphy = new Gif(parent, "../200.gif");
    giphy.play();
    option = 1;
  }
  
  // Move the raindrop down
  void move() {
    // Increment by speed
    y += speed;
  }

  // Check if it hits the bottom
  boolean reachedBottom() {
    // If we go a little beyond the bottom
    if (y > height + r*4) { 
      return true;
    } else {
      return false;
    }
  }
  
  void reset() {
    x = random(width);
    y = -r;
    speed = random(1, 5);
  }

  // Display the raindrop
  void display() {
    if(option == 0) {
      // Display the drop
      //stroke(0);
      //fill(c);
      //noStroke();
      //ellipse(x, y, r*2, r*2);
      image(img, x, y, r*2, r*2);
    } else {
      imageMode(CENTER);
      image(giphy,x,y, r*2, r*2);
    }
  }

  // If the drop is caught
  void caught() {
    // Stop it from moving by setting speed equal to zero
    speed = 0; 
    // Set the location to somewhere way off-screen
    y = -1000;
  }
}
