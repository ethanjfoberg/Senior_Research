import json
import random

# Load the dataset from file (adjust path as needed)
with open("news_dataset.json", "r", encoding="utf-8") as f:
    data = json.load()  # use json.load() if it's a full list in a JSON file

# Sample 50 unique articles
sampled_articles = random.sample(data, 50)

# Save to new file
with open("sampled_articles.json", "w", encoding="utf-8") as out_file:
    json.dump(sampled_articles, out_file, ensure_ascii=False, indent=2)

print("50 random articles saved to 'sampled_articles.json'")
