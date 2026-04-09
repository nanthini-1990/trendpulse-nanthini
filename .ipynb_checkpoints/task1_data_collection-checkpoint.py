# task1_data_collection.py

import requests
import time
import json
import os
from datetime import datetime

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories with keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Fetch top story IDs
def fetch_top_story_ids():
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:500]
    except Exception as e:
        print("Error fetching top stories:", e)
        return []

# Fetch single story
def fetch_story(story_id):
    try:
        url = ITEM_URL.format(story_id)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")
        return None

# Assign category based on keywords
def assign_category(title):
    if not title:
        return None

    title = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return None

# Main function
def main():
    story_ids = fetch_top_story_ids()

    collected_data = []
    category_counts = {cat: 0 for cat in categories}

    # Loop category-wise
    for category in categories:
        print(f"\nCollecting {category} stories...")

        for story_id in story_ids:
            # Stop if 25 reached
            if category_counts[category] >= 25:
                break

            story = fetch_story(story_id)

            if not story:
                continue

            title = story.get("title", "")
            assigned_category = assign_category(title)

            # Only take matching category
            if assigned_category == category:
                data = {
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                collected_data.append(data)
                category_counts[category] += 1

                print(f"{category_counts[category]} collected for {category}")

        # Sleep after each category
        time.sleep(2)

    # Create data folder
    if not os.path.exists("data"):
        os.makedirs("data")

    # File name
    file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    # Save JSON
    with open(file_name, "w") as file:
        json.dump(collected_data, file, indent=4)

    print("\n✅ Completed!")
    print(f"Total records: {len(collected_data)}")
    print(f"Saved to: {file_name}")


# Run script
if __name__ == "__main__":
    main()