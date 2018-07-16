# below is the configuration of the various keys and authentication tokens necessary to use the multiple APIs involved
# you will also find the necessary keyword definition section that lets you define which subreddits to search for which keywords and what slack channel to notify

# other things to define like tokens and client information
# token can be found at https://api.slack.com/custom-integrations/legacy-tokens
# reddit information can be found at https://www.reddit.com/prefs/apps/ 
slackToken = ''
reddit_client_id = ''
reddit_client_secret = ''
reddit_user_agent = 'redditNotify bot by u/InsideAnalysis, github: nicknazari'
slackbot_username = ''

# define search keyword and subreddit here, these are the essential parts of the program
keywords = ['add any keywords here, you can insert multiple']
# add '+' between each subreddit to search multiple
subToSearch = 'subreddit+anothersubreddit'
channelToSendMessage = 'channel to send messages to'