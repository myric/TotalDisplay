# TotalDisplay

This extraordinarly simple display will animate a cascade of animated gifs - a random selection from Giphy - down the screen. Unless it runs out of memory.

## How It Works

At boot, the python script will run, sending 5 quick API requests to giphy and saving a series of gifs in a folder. Afterwards, the Processing script should run, fill the whole screen, and cascade them down until the plug is pulled.

## What It Shows Us

In a similar vein to Know Your Meme, Giphy is a compendium of modern culture's obessive, recursive recuration of its own media creations. TotalDisplay is hidden mirror on high street (as it turns out they call 'main street' here). The same gifs we browse through as we contemplate responding to the group chat remain with us, and the mirror reminds us of that.

## What Doesn't Work

Ideally, this would continuously refresh from giphy and the gifs would have a better frame rate. 

To save space, I've selected the "downsampled" option, since otherwise some of them can be several MB. I have upgraded the max memory allocation on Processing to 2GB, but it still seems to complain when it tries to load several pictures under normal compression
