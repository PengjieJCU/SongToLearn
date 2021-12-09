CP1404 Assignment 2 – Songs To Learn 2.0 
Task:
Create a Graphical User Interface (GUI) program similar using Python 3 and the Kivy toolkit, as described in the following information and accompanying screencast. This assignment will help you build skills using classes and GUIs as well as giving you more practice using techniques like selection, repetition, exceptions, lists, file I/O and functions. 


<img width="435" alt="SongToLearn screenshot 1" src="https://user-images.githubusercontent.com/44990567/145338974-22aa1a23-587a-4c13-9a50-4356658e7591.png">

Program Overview:
Ensure that your program GUI has the following features, as demonstrated in the screenshots and accompanying screencast:
1. the left side of the screen contains a drop-down "spinner" for the user to choose the song sorting, and text entry fields for inputting information for a new song.
2. the right side contains buttons for the songs, colour-coded based on whether they are learned or not
3. the status bar at the top of the right side shows the number of songs learned and still to learn
4. the status bar at the bottom of the right side shows messages about the state of the program, including updating when a song is clicked on
5. the user can add a new song by entering text in the input fields and clicking “Add Song”
6. the exact style (including colours) is up to you, but ensure that all functionality is readily accessible with your chosen GUI style

Program Functionality Details:
Complete the main program in a Kivy App subclass in main.py. There will be no main() function, but rather your program will run() the Kivy app in the same way as you've seen in our example programs. The program should start by loading the same CSV file of songs as with your first assignment. This must be done with a method of your main app class and will save the songs as Song instances in a SongList instance (see below for details).
The songs file must be saved when the program ends, updating any changes made with the app by the user (adding new songs or marking them as learned).

Adding features:
All song fields are required. If a field is left blank, the bottom status bar should display “All fields must be completed” when “Add Song” is clicked.
The year field must be a valid integer. If this is invalid, the status bar should display “Please enter a valid number”.
Pressing the Tab key should move between the text fields. 
When the user successfully adds a song, the fields should be cleared and the song should appear in the songs list on the right. 
When the user clicks the “Clear” button, all text in the input fields and the status bar should be cleared.
