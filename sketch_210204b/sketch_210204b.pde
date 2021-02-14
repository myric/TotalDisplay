// Example 10-7: Drops one at a time

// An array of drops
static int size = 40;
static int numpics = 10;

Drop[] drops = new Drop[size];

// New variable to keep track of total number of drops we want to use!
//int totalDrops;

void setup() {
  //size(1440, 810);
  fullScreen();
  
  //initialize drops
  //for(int d = 0; d < drops.length; d++) {
  //  if((d % 2) == 0) {
  //    drops[d] = new Drop();
  //  } else {
  //    drops[d] = new Drop(this);
  //  }
  //}
  
  for(int d = 0; d < size; d++) {
    drops[d] = new Drop(this, (d % numpics));
  }
  
} //<>//

void draw() {
  background(10);
  
  // Move and display drops
  // New! We no longer move and display 
  // all drops, but rather only the “totalDrops” 
  // that are currently present in the game.
  
  for (int i = 0; i < size; i++ ) {
    drops[i].move();
    drops[i].display();
    
    if(drops[i].reachedBottom()) {
      drops[i].reset();
    }
  }
}
