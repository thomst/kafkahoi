kafkahoi
========

Kafkahoi is a little shooter game with a special concept of controlling your
charaktars.

You are a team of two little asterisks anywhere out in the wild -trying to
survive and to collect the little sweet letters of a beautiful poem.
One of you is the hunter, killing murderous flies with his sharp arrows and
protecting you from a big ugly bug.
The other one is the gatherer, never tired to find and collect the precious
little letters.

But keep your powder dry! Your two little asterisks are a twirly little
bunch, and you cannot control their movements directly -only influence their
woozily fuss...


Latest Version
--------------
The latest version of this project can be found at : http://github.com/thomst/kafkahoi.


Installation
------------

You need:

* pygame (http://pygame.org) and
* Tkinker (http://docs.python.org/2/library/tkinter.html)

On Linux/Ubuntu do ::

    sudo apt-get install python-pygame
    sudo apt-get install python-tk

Get the zip-archive from github ::

    wget https://github.com/thomst/kafkahoi/archive/master.zip
    unzip master.zip
    cd kafkahoi-master/

Or download the tarball at http://sourceforge.net/projects/kafkahoi/
and unpacking it ::

    tar -xzf kafkahoi-1.0.4.tar.gz
    cd kafkahoi-1.0.4/

Install kafkahoi ::

    sudo python setup.py install

Start the game with just typing ::

    kafkahoi


Gameplay
--------

Collect all letters and complete the poem!
Kill the flies and lame the bug with your hunter's arrows. But beware of
touching them!


Gamecontrol
-----------

The movements of the asterisks are influenced by the position of the mouse.
Tip: keep the mouse near the asterisks to minimalize their movements.

playing-mode:

* <s>/<f> or ←/→:
            rotate the hunter (white asterisk) for aiming
* <space> or ↓:
            throw the collected letters. They will find their right place if
            they are enough to build or complete a whole word.
* left mouse-button:
            shoot with the hunter (white asterisk)
* right mouse-button:
            collect letters with the gatherer (lilac asterisk)
* mouse-scroll:
            quick correction of the hunter's movement
* mouse-scroll + right mouse-button:
            quick correction of the gatherer's movement
* <p>:
            pause

menu-mode:

* <p>:
            choose poem
* <d>:
            choose level of dificulty
* <e>:
            start editor (there you can add/delete poems)


always:

* <s>:
            on/off sound
* <esc>:
            quit the game


Contribution
------------
Every kind of feedback is very welcome.


Reporting Bugs
--------------
Please report bugs at github issue tracker:
https://github.com/thomst/kafkahoi/issues


Author
------
thomst <thomaslfuss@gmx.de>
Thomas Leichtfuß

* http://github.com/thomst
