"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playlist = Playlist()
        self.current_video_title = ""
        self.current_video_id = ""
        self.current_video_tags = ""
        self.video_status = ""

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        videos.sort(key= lambda e:e.title)
        print("Here's a list of all available videos:")
        for video in videos:
            tags = ""
            for tag in video.tags:
                tags += " " + tag
            tags = tags.lstrip()
            tags = "[" + tags + "]"
            video_id = "(" + video.video_id + ")"
            print(video.title, video_id, tags)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            #if self.current_video_title != "":
                #print("Playing video:", self.current_video_title)
            print("Cannot play video: Video does not exist")
        else:
            if self.current_video_title == "": #Check whether any video is playing
                self.current_video_title = video.title
                self.current_video_id = video.video_id
                self.current_video_tags = video.tags
                self.video_status = "playing"
                print("Playing video:", self.current_video_title)
            else:
                print("Stopping video:", self.current_video_title)
                self.current_video_title = video.title
                self.current_video_id = video.video_id
                self.current_video_tags = video.tags
                self.video_status = "playing"
                print("Playing video:", self.current_video_title)


    def stop_video(self):
        """Stops the current video."""
        if self.current_video_title == "": #Player is empty
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self.current_video_title)
            self.current_video_title = ""
            self.current_video_id = ""
            self.current_video_tags = ""
            self.video_status = ""

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        video = random.choice(videos)

        self.play_video(video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.current_video_title == "": #no video is playing
            print("Cannot pause video: No video is currently playing")
        else:
            if self.video_status == "paused":
                print("Video already paused:", self.current_video_title)
            else:
                print("Pausing video:", self.current_video_title)  
                self.video_status = "paused" 

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current_video_title == "": #no video is playing
            print("Cannot continue video: No video is currently playing")
        else:
            if self.video_status == "playing":
                print("Cannot continue video: Video is not paused")
            else:
                print("Continuing video:", self.current_video_title)  
                self.video_status = "playing" 


    def show_playing(self):
        """Displays video currently playing."""
        if self.current_video_title == "": # no video is playing
            print("No video is currently playing")
        else:
            video = "Currently playing: " + self.current_video_title + " (" + self.current_video_id + ") "
            tags = ""
            for tag in self.current_video_tags:
                tags += " " + tag
            tags = tags.lstrip()
            tags = "[" + tags + "]"
            video += tags
            if self.video_status == "playing":
                print(video)
            else:
                print(video, "- PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        
        print("playlists")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
