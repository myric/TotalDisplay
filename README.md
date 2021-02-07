# TotalDisplay

This extraordinarily simple display will animate a cascade of animated gifs - a random selection from Giphy - down the screen. Unless it runs out of memory. There is also a festive rainbow pinwheel.

## What It Does

At boot, the python script will run, sending a few quick API requests (some requests pull a list while 'random' only returns info for a single gif) to giphy and saving a series of gifs in a folder. Shortly afterwards, the Processing script runs, filling the whole screen, and cascades them down until the plug is pulled.

## What It Shows Us

In a similar vein to Know Your Meme, Giphy is a compendium of modern culture's obessive, recursive curation and recuration of its own media creations. Through their API, they offer random access to their database of gifs and still images in a variety of formats. Platforms like WhatsApp, Slack, and Discord (which uses a similar service) offer these gifs to their users as a directly emotive language of expression.  TotalDisplay is a hidden mirror on high street (as it turns out they call 'main street' here). The same gifs we browse through as we contemplate responding to the group chat remain with us, and the mirror reminds us of that.

## How It Works
The primary code included in this repo consists of sketch\_210204b, franken.py, and berry.py. Franken and berry run boot from rc.local, and respectively control the API calls to Giphy and the LED device. rc.local from /etc has been edited to run them both in forked processes.

In addition, a script 'sketcher.desktop' has been added to ~/.config/autostart/ to run the Processing sketch as soon as the GUI has loaded. Between the delay built into the franken.py script and the time to start the GUI, that seems to be enough time for the gifs to be loaded from Giphy.

## Replication

In addition to this repo and the startup scripts, one also needs to sign up for Giphy's API. This is very straightforward as they offer beta access just to sign up with an email and a name.

Secondly, Processing requires loading a separate library, gifAnimation, for it to easily handle and display gifs. (Otherwise you have to load them as arrays of animations and more closely manipulate them. This can be aquired from: https://github.com/extrapixel/gif-animation/tree/master

The LED requires the NeoPixel library to be loaded for python and additionally requires that its scripts be run by root. Under normal operations, run them with sudo. In the case of this project, rc.local runs things as root, so the problem takes care of itself.

## What Doesn't Work

Ideally, there would be many more pictures loaded, they would continuously refresh from giphy with every refresh at the bottom of the screen, and the whole display would have a better frame rate. A fuller screen would more properly communicate the visual cacophony. On my laptop the framework doesn't seem so bad, but the Pi struggles.

To save space, I've selected the "downsampled" option, since otherwise some of them can be several MB. I have upgraded the max memory allocation on Processing to 2GB, and that combined with the downsampled gifs has allowed it to work, but at the expense of the gifs being pretty choppy. 

## Odds And Ends

Also included in this repo are a few extra things:
- 200.gif and alt.jpg are there for testing.
- sketch\_210204a contains the trial code for using the gifAnimation library for Processing
- UVtransform is an example animation using the Shape3d library. This library contains methods for rendering 3D shapes with processing, as well as for their rotation / camera rotation around these objects. It also contains a method for 'animating', to some degree, a still image across a 3D surface. Unfortunately their texture method does not seem prepared to handle gifAnimation's GIF objects, so further development will have to come at another time.
