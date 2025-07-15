import os
import requests
import json

def generate_persona(data):
    prompt = (
        "You're an AI trained to create detailed user personas from Reddit activity.\n"
        "Given the following posts and comments, extract a persona with:\n"
        "1. Name (if available)\n"
        "2. Age group\n"
        "3. Gender (if known or guessable)\n"
        "4. Interests\n"
        "5. Beliefs/opinions\n"
        "6. Online behavior\n"
        "7. Favorite subreddits\n"
        "8. Writing style\n"
        "9. Any identifiable occupation/hobbies\n"
        "For each characteristic, cite the post or comment (by including the URL) you based it on.\n\n"
        "Here is the user's data:\n"
    )

    for post in data['posts']:
        prompt += f"[POST] {post['title']} - {post['selftext'][:300]}... (Subreddit: {post['subreddit']}) [URL: {post['url']}]\n"
    for comment in data['comments']:
        prompt += f"[COMMENT] {comment['text'][:300]}... (Subreddit: {comment['subreddit']}) [URL: {comment['url']}]\n"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama3-70b-8192",  # or "mixtral-8x7b-32768"
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1500
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print("❌ Error:", response.status_code, response.text)
        return "Error generating persona"
