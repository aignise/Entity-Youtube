import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your YouTube Data API key here
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_videos(query):
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=5,  # You can adjust this as per your requirement
            order="viewCount",  # You can change the order as per your requirement
        )
        response = request.execute()
        
        return response['items']

def fetch_video_statistics(video_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()
    
    items = response.get('items', [])
    if items:
        statistics = items[0].get('statistics', {})
        view_count = statistics.get('viewCount', 'N/A')
        like_count = statistics.get('likeCount', 'N/A')
        dislike_count = statistics.get('dislikeCount', 'N/A')
        return view_count, like_count, dislike_count
    else:
        return 'N/A', 'N/A', 'N/A'


def fetch_videos(query):
        videos = search_videos(query)
        for video in videos:
            video_id = video['id']['videoId']
            view_count, like_count, dislike_count = fetch_video_statistics(video_id)
            video['statistics'] = {
                'viewCount': view_count,
                'likeCount': like_count,
                'dislikeCount': dislike_count
            }
        return videos
