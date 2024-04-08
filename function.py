import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your YouTube Data API key here
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

class YouTubeAPI:
    @staticmethod
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

    @staticmethod
    def fetch_video_statistics(video_id):
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        
        request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        response = request.execute()
        
        if 'items' in response:
            statistics = response['items'][0]['statistics']
            view_count = statistics.get('viewCount', 'N/A')
            like_count = statistics.get('likeCount', 'N/A')
            dislike_count = statistics.get('dislikeCount', 'N/A')
            return view_count, like_count, dislike_count
        else:
            return 'N/A', 'N/A', 'N/A'

    @staticmethod
    def fetch_videos(query):
        videos = YouTubeAPI.search_videos(query)
        for video in videos:
            video_id = video['id']['videoId']
            view_count, like_count, dislike_count = YouTubeAPI.fetch_video_statistics(video_id)
            video['statistics'] = {
                'viewCount': view_count,
                'likeCount': like_count,
                'dislikeCount': dislike_count
            }
        return videos
