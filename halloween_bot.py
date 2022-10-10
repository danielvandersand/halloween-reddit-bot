import praw
import config
import time
import os

def bot_login():
	print("Currently loogging in for a good time :)...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "The Reddit Commenter v1.0")
	print("Logged in!")

	return r

def run_bot(r, comments_replied_to):
	print("Searching last 500 comments")

	for comment in r.subreddit('memes').comments(limit=500):
		if "boo" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("String with \"boo\" found in comment " + comment.id)
			comment.reply("*starts screaming*")
			print("Replied to comment " + comment.id)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print("Search Completed.")

	print(comments_replied_to)

	#rest for 15 seconds
	print("Resting for 15 seconds...")
	time.sleep(15)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)