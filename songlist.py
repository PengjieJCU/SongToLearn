# create your SongList class in this file
from song import Song# import Song class

class SongList:
    def __init__(self):
        self.list_songs = []# Create a empty list

    def load_songs(self):
        """
        Load the songs from csv file and append them to list_songs
        """
        myFile = open("songs.csv", "r")
        lines = myFile.readlines()
        for line in lines:
            song_item = line.split(',')
            song_item[3] = song_item[3].strip('\n')
            loaded_song = Song(song_item[0],song_item[1],song_item[2],song_item[3])
            self.list_songs.append(loaded_song)# Add the song to the list_songs
        myFile.close()# Close the file

    def add_to_list(self, title, artist, year, is_required):
        #add the inputted song to the song list
        newSong = Song(title, artist, year, 'y')
        self.list_songs.append(newSong)

