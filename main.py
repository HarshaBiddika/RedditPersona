import sys
import os
from reddit_scraper import extract_username, scrape_user_data
from persona_generator_groq import generate_persona

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    url = sys.argv[1]
    username = extract_username(url)
    print(f"Scraping data for user: {username} ...")

    data = scrape_user_data(username)
    print("Generating user persona using GPT...")

    persona = generate_persona(data)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {output_dir}/{username}_persona.txt")

if __name__ == "__main__":
    main()
