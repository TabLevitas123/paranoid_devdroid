
import requests

class SocialMediaController:
    def __init__(self, platform, api_key):
        self.platform = platform
        self.api_key = api_key

    def post_update(self, message):
        if self.platform == 'twitter':
            return self.post_to_twitter(message)
        elif self.platform == 'discord':
            return self.post_to_discord(message)
        elif self.platform == 'facebook':
            return self.post_to_facebook(message)
        # Add other platforms here...

    def post_to_twitter(self, message):
        # Example logic for posting to Twitter (requires Twitter API setup)
        url = "https://api.twitter.com/2/tweets"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"text": message}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print(f"Posted to Twitter: {message}")
            return True
        else:
            print(f"Failed to post to Twitter: {response.status_code}")
            return False

    def post_to_discord(self, message):
        # Example logic for posting to Discord (requires Discord webhook setup)
        webhook_url = "https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
        data = {"content": message}
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"Posted to Discord: {message}")
            return True
        else:
            print(f"Failed to post to Discord: {response.status_code}")
            return False

    def post_to_facebook(self, message):
        # Example logic for posting to Facebook (requires Facebook API setup)
        url = "https://graph.facebook.com/v12.0/me/feed"
        params = {"message": message, "access_token": self.api_key}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print(f"Posted to Facebook: {message}")
            return True
        else:
            print(f"Failed to post to Facebook: {response.status_code}")
            return False

# Example Usage
if __name__ == "__main__":
    sm_controller = SocialMediaController('twitter', 'your_twitter_api_key_here')
    sm_controller.post_update("Hello, this is a test message for Twitter.")
