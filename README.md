\# Reddit User Persona Generator (CLI Version)



This script takes a Reddit user's profile URL, scrapes their recent posts and comments, and uses an LLM (via Groq API) to generate a detailed user persona with citations to specific content.



---



\## 📦 Requirements



\- Python 3.8+

\- Groq API key

\- Reddit developer credentials (client ID, secret, user agent)



---



\## Setup Instructions



\### 1. Clone the Repo



```bash

git clone https://github.com/yourusername/reddit-user-persona.git

cd reddit-user-persona

2\. Install Python Dependencies

bash

Copy

Edit

pip install -r requirements.txt

3\. Configure Environment Variables

Create a .env file in the root directory:



init

Copy

Edit

GROQ\_API\_KEY=your\_groq\_api\_key\_here

REDDIT\_CLIENT\_ID=your\_client\_id\_here

REDDIT\_CLIENT\_SECRET=your\_client\_secret\_here

REDDIT\_USER\_AGENT=RedditPersonaApp/1.0 by your\_username

&nbsp;You can use the .env.example file as a template.



&nbsp;How to Use

Generate a Persona from Any Reddit Profile

bash

Copy

Edit

python main.py https://www.reddit.com/user/kojied/

This will scrape recent activity from the Reddit user kojied



It will generate a persona using Groq’s LLM (e.g., LLaMA 3)



Output will be saved as:



bash

Copy

Edit

output/kojied\_persona.txt

You can repeat this with any Reddit profile by changing the URL:



bash

Copy

Edit

python main.py https://www.reddit.com/user/Hungry-Move-6603/

&nbsp;Output

Generated personas are saved in the output/ folder as:



kojied\_persona.txt



Hungry-Move-6603\_persona.txt



new\_username\_persona.txt (for future runs)



&nbsp;Submission Checklist

&nbsp;Executable Python script



&nbsp;Instructions for setup and execution



&nbsp;Sample outputs for two users



&nbsp;PEP-8 style compliant



&nbsp;Tech Used

Python 3.8+



praw for Reddit scraping



requests for calling Groq API



dotenv for config

