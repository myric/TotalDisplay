// Example 10-7: Drops one at a time

// An array of drops
Drop[] drops = new Drop[25];
Drop drop1;
Drop drop2;

// New variable to keep track of total number of drops we want to use!
int totalDrops;

void setup() {
  size(480, 270);
  totalDrops = 0;
  drop1 = new Drop(this);
  drop2 = new Drop();
}

void draw() {
  background(255);

  drop1.move();
  drop1.display();

  drop2.move();
  drop2.display();

  println(totalDrops); //<>//

  // Initialize one drop
  if((totalDrops % 2) == 0) {
    drops[totalDrops] = new Drop();
  } else {
    drops[totalDrops] = new Drop(this);
  }

  // Increment totalDrops
  totalDrops++ ;

  // If we hit the end of the array
  if (totalDrops >= drops.length) {
    totalDrops = 0; //Start over
  }
  
  // Move and display drops
  // New! We no longer move and display 
  // all drops, but rather only the “totalDrops” 
  // that are currently present in the game.
  
  for (int i = 0; i < totalDrops; i++ ) {
    drops[i].move();
    drops[i].display();
  }
}
