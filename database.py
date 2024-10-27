import requests
import matplotlib.pyplot as plt

# Function to fetch data from an API
def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/posts' # what exactly does this do??
    response = requests.get(url)
    data = response.json()
    return data

# Function to create a chart
def create_chart(data):
    # Prepare data for the chart
    labels = [item['title'][:10] for item in data]  # First 10 characters of the title
    values = [item['id'] for item in data]  # Using IDs as data points

    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='lightblue')
    plt.xlabel('Post Titles')
    plt.ylabel('Post IDs')
    plt.title('Post ID Chart')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()