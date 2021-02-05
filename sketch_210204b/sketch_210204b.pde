// Example 10-7: Drops one at a time

// An array of drops
Drop[] drops = new Drop[10];
Drop drop1;
Drop drop2;

// New variable to keep track of total number of drops we want to use!
//int totalDrops;

void setup() {
  size(480, 270);
  
  //initialize drops
  for(int d = 0; d < drops.length; d++) {
    if((d % 2) == 0) {
      drops[d] = new Drop();
    } else {
      drops[d] = new Drop(this);
    }
  }
  
  drop1 = new Drop(this);
  drop2 = new Drop();
}

void draw() { //<>//
  background(255);

  drop1.move();
  drop1.display();

  drop2.move();
  drop2.display();

  // If we hit the end of the array
  //if (totalDrops >= drops.length) {
  //  totalDrops = 0; //Start over
  //}
  
  // Move and display drops
  // New! We no longer move and display 
  // all drops, but rather only the “totalDrops” 
  // that are currently present in the game.
  
  for (int i = 0; i < drops.length; i++ ) {
    drops[i].move();
    drops[i].display();
    
    if(drops[i].reachedBottom()) {
      drops[i].reset();
    }
  }
}
