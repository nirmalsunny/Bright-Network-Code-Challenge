"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
       self._playlists = {
           "Funny_Videos" : ["funny_dogs_video_id",]    #Demo Playlist
       }

    def get_playlists():
        return self._playlists.keys()

    def get_videos(playlist):
        return self._playlists[playlist]

    def add_videos(playlist, videos):
        self._playlists[playlist] = videos

    def add_playlist(playlist_name):
        self._playlists[playlist_name] = []
        
    def remove_playlist(playlist_name):
        return self._playlists.pop(playlist_name)