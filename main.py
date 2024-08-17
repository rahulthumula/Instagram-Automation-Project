from instagrapi import Client
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_dm_to_commenters(post_url, message):
    cl = Client()
    username = os.getenv('IG_USERNAME')
    password = os.getenv('IG_PASSWORD')
    
    if not username or not password:
        raise ValueError("Both IG_USERNAME and IG_PASSWORD environment variables must be set.")
    
    try:
        cl.login(username, password)
    except Exception as e:
        raise ValueError(f"Failed to log in with the provided credentials: {e}")

    try:
        media_id = cl.media_pk_from_url(post_url)
    except Exception as e:
        print(f"Failed to retrieve the post: {e}")
        return

    if not media_id:
        print("The post does not exist or the URL is invalid.")
        return

    comments = cl.media_comments(media_id)
    dm_sent_users = set()

    for comment in comments:
        user_id = comment.user.pk
        
        if user_id not in dm_sent_users:
            try:
                cl.direct_send(message, [user_id])
                print(f"DM sent to {comment.user.username}")
                dm_sent_users.add(user_id)
                
                with open("dm_log.txt", "a") as log_file:
                    log_file.write(f"DM sent to {comment.user.username}\n")
                
                time.sleep(2)  # Adjust sleep time based on Instagram's rate limits

            except Exception as e:
                print(f"Failed to send DM to {comment.user.username}: {e}")
                with open("dm_log.txt", "a") as log_file:
                    log_file.write(f"Failed to send DM to {comment.user.username}: {e}\n")
                
    print("DM sending completed.")

if __name__ == "__main__":
    post_url = "https://www.instagram.com/p/CRO6ZSCtsdD/"
    message = "Thank you for commenting on our post! We appreciate your support."
    send_dm_to_commenters(post_url, message)
