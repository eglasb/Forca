## Building a Hangman Game in Python - With a Linguistic Twist! – Python OOP

This is a Hangman game implemented using Object-Oriented Programming (OOP) in Python.

## In_r_duc_i_n ##
      ________
       |/     |
       |     ___
       |    |ó,ò|
       |    \_-_/
       |      
       |
       |

Ever wanted to learn Portuguese while playing a classic game? Well, you might not become fluent, but playing my Hangman (Forca) game in Portuguese will at least teach you some words — and test your guessing skills! As part of my Python learning journey, I decided to build a Hangman game in the terminal. This project helped me understand concepts like string manipulation, loops, and object-oriented programming while having fun. The ideia was to make it a very polished experience, without unexpected crashes, counting games and victories, calling the player by the name.
## The Project "Forca"

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1fl1vsta8vin157inbjt.jpg)
Prepare for gruesome death!


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xd5jc1xrybgoh6tortx4.jpg)
And Victory!

For this project I´ve created 4 classes and a utility file:
* Game - manages game flow
* Player - manages player data (lives, letters played, etc.)
* SecretWord - deals with word management and revealing letters
* HangmanDoll - holds the ASCII art.
* utils.py - contains some shared functions for reading file, clearing screen and input validation
I tried to use a modular approach and type hints to really exercise OOP.

It was a great learning experience and I think the game turned out to be really funny to play!

I used Python in VScode for the entire game logic and Git for version control.

## Code on GitHub
https://github.com/eglasb/Forca.git

## Future improvements
I intend to eventually add graphics. Maybe Pygame?