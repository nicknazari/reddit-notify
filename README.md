# Reddit Notifications by Slack Channel

This handy program allows for a Slack bot to send a message to a
channel when a specified keyword is contained in the title of new posts in a subreddit.

### Requirements:
A Reddit application and Slack bot in a channel are required.

### How it works

Every two seconds, a subreddit's five most recent posts are retrieved and stored by their titles and links.

Then, they are scanned for the keyword. If the keyword is not found, the program continues retrieving titles every two seconds.

The program compares these subsequent titles to the previously stores titles, and stores the new ones only if they have changed.

If a title contains a keyword, a message is sent to the Slack channel specified at the beginning of the program. 
The message contains the title of the post and a link to the post.
