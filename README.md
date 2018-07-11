# Reddit Notifications by Slack Channel

This handy program allows for a Slack bot to send a message to a
channel when a specified keyword is contained in the title of new posts in a subreddit.
I run this program 24/7 on a Raspberry Pi.

### Requirements
A Reddit application and Slack bot in a channel are required.
You can register a Reddit applcation [here](https://www.reddit.com/prefs/apps/)

### How it works

Every two seconds, a subreddit's five most recent posts are retrieved and stored by their titles and links.

They are scanned for the keywords. If no keywords are found, the program continues retrieving titles every two seconds.

The program compares these subsequent titles to the previously stored titles and stores the new ones only if they have changed.

If any title contains a keyword, a message is sent to the Slack channel specified at the beginning of the program. 
The message contains the title of the post and a link to the post.

## Upcoming updates

- Multi-subreddit search
- Clean up code and organize in to functions
- Twilio integration (to allow for text message notification)
- Email integration
