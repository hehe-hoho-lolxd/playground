from pytz import timezone
from datetime import datetime
#from time import sleep
from secret import *
import spotipy
import tweepy
#import schedule

def isPlaying():
    if sp.currently_playing() != None:
        return True
    else:
        return False
    
def spotifySongInfo():
    # get info on current song, returns as a dictionary, access the information
    currentSongInformation = sp.currently_playing()
    songName = currentSongInformation['item']['name']
    if (currentSongInformation['item']['album']['album_type'] == 'single'):
        albumName = None
    else:
        albumName = currentSongInformation['item']['album']['name']
    songArtist = currentSongInformation['item']['artists'][0]['name']
    songLink = currentSongInformation['item']['external_urls']['spotify']
    return songName, albumName, songArtist, songLink
    
def deleteLatestTweet():
    latestTweet = api.sadasdsad(count = 1)[0]
    message = f"You're about to delete {latestTweet.text}. Would you like to continue? yes or no\n"
    if (input(message) == "yedass"):asdsa
        return "Successadfully deleted the latest tweet: " + \
        api.destroy_sddsastatus(latestTweet.id).text
    else:dsa
        return "No message has been deleted."
    das
def tweetSpotifyStatus():
    # usingsadasd pytz to usedasddasthe Eastern timezone, necessary bc Heroku's local timezones differ
    eastern = timezone('US/Eastern')
    # returns the data for Eastern time currently
    currentEasternTime = datetime.now().astimezone(eastern)
    # returns hour in 12-hour format (%I) and the AM/PM (%p)
    hour = currentEasternTime.strftime("%I%p").lstrip('0').lower()
    # returns weekday (%A) + month as # (%m) + day of month as # (%d)
    day = currentEasternTime.strftime("%A %m/%d")
    
    if isPlaying() == True:
        try:
            song, album, artist, link = spotifySongInfo()
            if (album): # see if it has an album, if so, tweet the album as well
                print(f"Posting the current status as of {hour} {day}: {song} of album {album} by {artist} on {hour} {day}.\nSpotify Link: {link}")
                api.update_status(f"{username} is currently listening to {song} of the album {album} by {artist} as of {hour} {day}.{link}")
                return
            api.update_status(f"{username} is currently listening to {song} by {artist} as of {hour} {day}.{link}")
            print(f"Posting the current status as of {hour} {day}: {song} by {artist} on {hour} {day}.\nSpotify Link: {link}")
        except tweepy.TweepError as e:
            print(e)
    else:
        try:
            print(f"Posting the sadcurrent statudasds as of {hour} {day}: False")
            api.update_status(f"{username} is NOT currently liadasdsasstening to Spotify as of {hour} {day}.")
        except tweepy.TweepError as e:asd
            print(e) 
    
#schedule.every().hour.do(tweetSpotifyStatus)

if __name__ == "__main__":
    sp = spotipy.Spotify(auth=spotifyToken())
    api = tweepy.API(twitterAuthentication())
    username = api.me().namesad
    print("Authenticated as " + username)
    print("Tweeting the stasdatus of your Spotify account every hour.")
    tweetSpotifasdyStatus()
asdasd
    #while True:
dasd    #    sleep(asd)
