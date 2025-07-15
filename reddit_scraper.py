import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username(url):
    return url.rstrip("/").split("/")[-1]

def scrape_user_data(username, max_items=50):
    user = reddit.redditor(username)
    comments, posts = [], []

    try:
        for c in user.comments.new(limit=max_items):
            comments.append({"text": c.body, "subreddit": c.subreddit.display_name, "url": f"https://reddit.com{c.permalink}"})
        for p in user.submissions.new(limit=max_items):
            posts.append({"title": p.title, "selftext": p.selftext, "subreddit": p.subreddit.display_name, "url": p.url})
    except Exception as e:
        print(f"Error fetching user data: {e}")

    return {"comments": comments, "posts": posts}
