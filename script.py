# #!/usr/bin/env python3
# """
# Generates README.md for a GitHub profile repo and updates it daily.
# """

# import os
# import sys
# import requests
# from datetime import datetime
# import pytz
# import random

# # -------- Config (edit these to customize your profile) --------
# DISPLAY_NAME = "Suyash Singh"          
# BIO_LINE = "B.Tech CSE • ML & Web Dev • Building cool projects."  
# WHAT_IM_UP_TO = "Working on exciting ML + Web projects. Ask me about DS/ML!"  

# QUOTES = [
#     "Ship early. Ship often.",
#     "Code is like humor. When you have to explain it, it’s bad.",
#     "Strive for progress, not perfection.",
#     "Make it work, make it right, make it fast.",
#     "Keep learning — the moment you stop is the moment you fall behind."
# ]
# # ----------------------------------------------------------------

# # FIXED USERNAME
# username = "suyXcode"

# # Use GitHub API token (available in GitHub Actions)
# GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# # Helper: fetch basic user info via GitHub API
# def fetch_user_info(user, token=None):
#     url = f"https://api.github.com/users/{user}"
#     headers = {}
#     if token:
#         headers["Authorization"] = f"token {token}"
#     resp = requests.get(url, headers=headers, timeout=20)
#     if resp.status_code == 200:
#         return resp.json()
#     else:
#         print(f"Warning: Failed to fetch GitHub user info ({resp.status_code})", file=sys.stderr)
#         return {}

# # Get IST datetime string
# def now_ist_iso():
#     tz = pytz.timezone("Asia/Kolkata")
#     return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")

# user_info = fetch_user_info(username, GITHUB_TOKEN)
# public_repos = user_info.get("public_repos", "—")
# followers = user_info.get("followers", "—")
# following = user_info.get("following", "—")
# profile_html_url = user_info.get("html_url", f"https://github.com/{username}")

# selected_quote = random.choice(QUOTES)

# # Build README content
# readme = f"""# Hi, I'm {DISPLAY_NAME} 👋

# **{BIO_LINE}**

# [![Profile views](https://komarev.com/ghpvc/?username={username}&color=brightgreen)](https://github.com/{username})

# ---

# ### 🔭 What I'm working on
# {WHAT_IM_UP_TO}

# ---

# ### 📊 GitHub stats
# - Public repos: **{public_repos}**
# - Followers: **{followers}**
# - Following: **{following}**
# - Profile: [{username}]({profile_html_url})

# ---

# ### 📅 Daily note (IST)
# **{now_ist_iso()}**

# > _"{selected_quote}"_

# ---

# *This README is automatically updated daily using GitHub Actions.*  
# """

# # Write README.md only if changed
# path = "README.md"
# old = None
# if os.path.exists(path):
#     with open(path, "r", encoding="utf-8") as f:
#         old = f.read()

# if old != readme:
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(readme)
#     print("README.md updated.")
# else:
#     print("README.md already up-to-date; no changes made.")
