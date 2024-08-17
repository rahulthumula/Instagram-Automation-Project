# Instagram DM Automation

This project automates the process of sending a Direct Message (DM) on Instagram to all users who have commented on a specific Instagram post. The script is written in Python and utilizes the `instagrapi` library to interact with Instagram's API.

## Features

- Automatically sends a predefined DM to all commenters on a specific Instagram post.
- Ensures that each user receives the DM only once, even if they have commented multiple times.
- Logs both successful and failed DM attempts for reference.
- Includes error handling for issues such as invalid credentials, API rate limits, and other potential errors.

## Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)
- **Instagram account** with credentials
- **instagrapi** library
- **python-dotenv** library

## Installation

1. **Clone the repository** (or download the script files):

   ```bash
   git clone https://github.com/yourusername/instagram-dm-automation.git
   cd instagram-dm-automation
