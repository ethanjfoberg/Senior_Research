import openai
import json
import time
import random

# openai.api_key = "hidden for lab 2"

# Define varied prompts to make the articles diverse
topics = [
    "technology", "health", "environment", "politics", "education",
    "sports", "entertainment", "finance", "science", "world news"
]

styles = [
    "objective reporting", "investigative journalism", "breaking news",
    "opinion piece", "human interest story"
]

def generate_prompt():
    topic = random.choice(topics)
    style = random.choice(styles)
    return (
        f"Write a short news article (300–500 words) on a current issue in {topic}. "
        f"Use the tone and structure of a {style}. The article should appear realistic, "
        f"include quotes, and simulate a real journalistic piece."
    )

def generate_article(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional news journalist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=700
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating article: {e}")
        return None

def main():
    articles = []
    for i in range(50):
        prompt = generate_prompt()
        print(f"Generating article {i+1}/50...")
        article = generate_article(prompt)
        if article:
            articles.append({
                "id": i + 1,
                "prompt": prompt,
                "article": article
            })
        time.sleep(1)  # Optional: be respectful to API rate limits

    # Optional: save to file
    with open("fake_news_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
