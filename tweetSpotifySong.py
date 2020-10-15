import spotipy
import spotipy.util as util
import tweepy
#import schedule
import pytz
from pytz import timezone ## ??
from datetime import datetime
from time import sleep
from secret import *

def isPlaying():
    sp = spotipy.Spotify(auth=spotifyToken())
    if sp.currently_playing() != None:
        return True
    else:
        return False
    
    #currentSongInformation = sp.currently_playing()
    # song name, album name, song artist, album cover picture
    #return currentSongInformation['item']['name'], currentSongInformation['item']['album']['name'], \
    #       currentSongInformation['item']['artists'][0]['name'], currentSongInformation['item']['album']['images'][0]['url']

def tweetSpotifyStatus():
    api = tweepy.API(twitterAuthentication())
    username = api.me().name

    # using pytz to use Eastern timezone since heroku's local timezone is different
    # find a way to change timezone w/o pytz
    
    eastern = timezone('US/Eastern')
    # returns the data for Eastern time currently
    currentEasternTime = datetime.now().astimezone(eastern)
    # returns hour in 12-hour format (%I) and the AM/PM (%p)
    hour = currentEasternTime.strftime("%I%p").lstrip('0').lower()
    # returns weekday (%A) + month as # (%m) + day of month as # (%d)
    day = currentEasternTime.strftime("%A %m/%d")
    
    
    if isPlaying() == True:
        try:
            print(f"Posting the current status as of {hour} {day}: True")
            api.update_status(f"{username} is currently listening to Spotify as of {hour} {day}.")
        except tweepy.TweepError as e:
            print(e)
    else:
        try:
            print(f"Posting the current status as of {hour} {day}: False")
            api.update_status(f"{username} is NOT currently listening to Spotify as of {hour} {day}.")
        except tweepy.TweepError as e:
            print(e) 
	
#schedule.every().minute.do(tweetSpotifyStatus)

if __name__ == "__main__":
    print("Tweeting the status of your Spotify account every hour.")
    tweetSpotifyStatus()
    #while True:
    #    schedule.run_pending()
    #    sleep(1)

## fun to-dos
## if there's an error in twitter api with code, 
## look up the reason for the error in twitter documentation 
## https://developer.twitter.com/en/support/twitter-api/error-troubleshooting