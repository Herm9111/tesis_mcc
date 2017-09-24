from tweepy import OAuthHandler
from tweepy import Stream
from .stdOutListener import StdOutListener

# Variables that contains the user credentials to access Twitter API
access_token = "105399556-iROaVZI1Itp285HQn3fAkAAUjb1VTL3hIZgAPzNE"
access_token_secret = "5doVPBxh9zkSILjXe8QH6BQsFbLfdNHEm4aNBQFXCkhHz"
consumer_key = "YwOp5ZA0muvHg2DUU7KJEvp2a"
consumer_secret = "LB0l8mORAcqHoJOEejeg5dR1y6lF4oo2PwWjcNM9sjcuhgrA2p"


print('WelcomeToMain')

# This handles Twitter authetification and
# the connection to Twitter Streaming API

listener = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)

# This line filter Twitter Streams to capture data
# by the keywords: 'python', 'javascript', 'ruby'
# stream.filter(locations=[-122.75, 36.8, -121.75, 37.8])
stream.filter(locations=[-103.542343, 20.522558, -103.202453, 20.809738])

# 20.522558, -103.542343
# 20.809738, -103.202453
# -103.3969037,20.6894966
