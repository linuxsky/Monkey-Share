Monkey-Share
============

A lightweight and naive P2P file sharing application using sockets written in Python, using PyQT as the GUI.

Originally used to learn about Python and sockets. Someday, I'll rewrite this with cleaner and more elegant code.

When I gave a demo in a programming class, I stripped off the UI and used my iPhone as a peer.

__Caution:__
Since entire files are loaded into memory before they are transferred, it's probably not a good idea to send large files. In the future, it will be better to read each line of the file individually.
