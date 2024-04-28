import requests
import matplotlib.pyplot as plt

# Make an API call
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
top_story_ids = response.json()

# Get story details by the ID
def get_story_details(story_id):
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_response = requests.get(story_url)
    return story_response.json()

# Get the details of the top 10
top_stories = [get_story_details(story_id) for story_id in top_story_ids[:10]]

# Get titles and number of comments for each story.
titles = [story["title"] for story in top_stories]
comments = [story["descendants"] for story in top_stories]

# Make the bar chart
plt.figure(figsize=(10, 6))
plt.barh(titles, comments, color='hotpink')
plt.xlabel('Number of Comments')
plt.ylabel('Title')
plt.title('Most Active Discussions on Hacker News')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest activity at the top
plt.tight_layout()
plt.show()
