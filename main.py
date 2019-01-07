"""
Name: PengJie
Date: 6/1/2019
Brief Project Description: Assignment 2
GitHub URL: https://github.com/JCUS-CP1404/a2--PengjieJCU
"""
import pandas as pd
from kivy.app import App
from kivy.lang import Builder
from songlist import SongList
from song import Song
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button

# Create your main program in this file, using the SongsToLearnApp class

class SongsToLearnApp(App):
    message = StringProperty()
    message2 = StringProperty()
    current_state = StringProperty()
    sort_by = ListProperty()

    def __init__(self, **kwargs):
        """
        construct the main app
        """
        super(SongsToLearnApp, self).__init__(**kwargs)
        self.sort_by = ["Title", "Artist", "Year", "Is_required"]# Create a list for "spinner"
        self.current_state = self.sort_by[0]# Set the "Title" as the default option
        self.song_list = SongList()
        self.song_list.load_songs()

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Songs to learn 2.0 by PengJie"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def change_sort(self):
        self.song_list.sort_songs.sort(self)

    def press_clear(self):
        # Clean the all the inputs
        self.root.ids.title.text = ''
        self.root.ids.artist.text = ''
        self.root.ids.year.text = ''

    def create_widgets(self):
        """
        Create widgets to show the song list
        """
        num_song = len(self.song_list.list_songs)
        learned_song = 0# Set the 0 to the number of songs learned
        for song in self.song_list.list_songs:# create a button for each data entry, specifying the text and id
            title = song.title
            artist = song.artist
            year = song.year
            learned = song.is_required
            display_text = self.formatText(title, artist, year, learned)# Display what should be added to the widget
            if learned == "n":
                learned_song += 1
                button_color = [0.7, 1, 0, 1]# If the song is learned,display green button
            else:
                button_color = [255, 0, 0, 1]  # If the song is not learned, display red button
            #If users click a song, the song will be learned
            temp_button = Button(text=display_text, id=song.title, background_color=button_color)
            temp_button.bind(on_release=self.press_entry)# The message2 will display that the song is learned
            self.root.ids.entriesBox.add_widget(temp_button)
        self.message = "To learn: {}. Learned: {}".format(num_song - learned_song, learned_song)# Display number of songs learned and not learned

    def formatText(self, title, artist, year, learned):
        """
        Format the text displayed in the messages2
        """
        if learned == "n":
            display_text = "{} by {} ({}) (Learned)".format(title, artist, year)
        else:
            display_text = "{} by {} ({})".format(title, artist, year)
        return display_text


    def press_entry(self, button):
        """
        The text displays in the message2
        :param instance: the Kivy button instance
        :return: None
        """
        buttonText = button.text #Determine the text on the widget buttons
        selectedSong = Song()
        for song in self.song_list.list_songs:
            displaymessage = self.formatText(song.title, song.artist, song.year, song.is_required)
            if buttonText == displaymessage:
                selectedSong = song
                break
        selectedSong.mark_learned()  # Mark the song learned
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()
        self.message2 = "You have learned {}".format(selectedSong.title)#Display the song you have learned

    def add_songs(self):
        """
        Users add song to the song list
        """
        #Check whether users input empty information
        if self.root.ids.title.text == "" or self.root.ids.artist.text == "" or self.root.ids.year.text == "":
            self.message2 = "The field can not be blank"
        try:
            # check whether users input valid information
            is_required = "y"
            title = str(self.root.ids.title.text)
            artist = str(self.root.ids.artist.text)
            year = int(self.root.ids.year.text)
            # Add the song inputted to the song list
            self.song_list.add_to_list(title, artist, year, is_required)
            temp_button = Button(text=self.formatText(title, artist, year, is_required))
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)
            # Empty the inputs after adding the song
            self.root.ids.title.text = ""
            self.root.ids.artist.text = ""
            self.root.ids.year.text = ""
        except ValueError:
            self.message2 = "Please enter a valid number"


SongsToLearnApp().run()

