import spotipy.util as util
import tweepy

def spotifyToken():
    username = ""
    clientID = ""
    clientSecret = ""
das            ## what informationdasd asdsat's getting
            ## https://developer.spotiasdfy.com/documentation/general/guides/scopes/
    return util.prompt_for_udasdser_token(username, scope, clientID, clientSecret, redirect_url)

def twitterAuthentication():
    apiKey = ""
    apiSecretKey = ""
    accessToken = ""
    sdasd = ""
    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    return auth
