# github: nicknazari
# may,june,july 2018

# specify all values in config.py

import time
import praw
from slackclient import SlackClient
import config

# all of the sent titles and links are stored here and checked before sending mail to avoid multiple messages of the same post. iterations int is increased by 1 every search process
doneTitles = []
doneLinks = []
iterations = 1

# define search keyword and subreddit here, these are the essential parts of the program
keywords = config.keywords
subToSearch = config.subToSearch
channelToSendMessage = config.channelToSendMessage

# other things to define like tokens and client information
# token can be found at https://api.slack.com/custom-integrations/legacy-tokens
# reddit information can be found at https://www.reddit.com/prefs/apps/ 
slackToken = config.slackToken
reddit_client_id = config.reddit_client_id
reddit_client_secret = config.reddit_client_secret
reddit_user_agent = 'redditNotify bot by u/InsideAnalysis, github: nicknazari'
slackbot_username = config.slackbot_username

# this func creates the chat function for slack
def slack_message(message, channelToSend):

	sc = SlackClient(slackToken)

	sc.api_call('chat.postMessage', channel=channelToSend,
			    text=message, username=slackbot_username,
				icon_emoji=':robot_face:')

# this connects to the reddit app to interact and use API
reddit = praw.Reddit(client_id = reddit_client_id,
					 client_secret = reddit_client_secret,
					 user_agent = reddit_user_agent)

# infinitely check the subreddit every two seconds
while True:
	# initializes each search
	sent = False
	titles = []
	sendQueue = []
	links = []
	sendQueueL = []
	# for each submission in the 5 newest posts on buildapcsales, print out their title and url

	for submission in reddit.subreddit(subToSearch).new(limit=5):
		# every 15 iterations (30 sec), print the posts found
		if iterations % 15 == 0:
			print('\nPOST')
			print(submission.title)
			print(submission.url)

		# then add each title to the titles list and each link to the links list
		titles.append(submission.title)
		links.append(submission.url)

	# check for the keywords in every title, add it to the sendQueue (titles) and sendQueueL (links) ONLY IF IT CONTAINS THE KEYWORD
	for title in titles:
		for keyword in keywords:
			if keyword in title:
				sendQueue.append(title)
				sendQueueL.append(links[titles.index(title)])
	
	# for every entry in sendQueue list, check if its been sent already. if it hasnt then call the slack message func and send that title and link to the channel
	for queueNum in range(0,len(sendQueue)):
		if sendQueue[queueNum] not in doneTitles:

			slack_message(sendQueue[queueNum] + '\n' + sendQueueL[queueNum], channelToSendMessage)
			sent = True
			print('Notification sent. ITERATION: ' + str(iterations))

			# add the title and link to doneTitles and doneLinks so that we can check for already sent titles next time and don't send multiple messages for the same post
			doneTitles.append(sendQueue[queueNum])
			doneLinks.append(sendQueueL[queueNum])

	# every 15 iterations print a new Iterations: after each post is displayed
	if iterations %15 == 0:
		print('\nIterations: ' + str(iterations) + ', ', end='')

	# every iteration except every 15th, print the iteration. Add an 's' after it if that iteration's result sent a notification
	if iterations % 15 != 0:
		print(str(iterations), end='')
		if sent:
			print('s', end='')
		print(', ', end='')

	iterations += 1

	time.sleep(2)