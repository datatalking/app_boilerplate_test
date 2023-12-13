"""
===============================================
Creating a timeline with lines, dates, and text
===============================================

How to create a simple timeline using Matplotlib release dates.

Timelines can be created with a collection of dates and text. In this example,
we show how to create a simple timeline using the dates for recent releases
of Matplotlib. First, we'll pull the data from GitHub.
"""

import json
import urllib.request
from datetime import datetime
import os
from pathlib import Path
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import yaml

# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# GitHub token for API access
github_token = os.getenv("GITHUB_TOKEN", "your_token_here")

# Load data from YAML file or GitHub API
data_path = "./data/timeline_data.yml"
if os.path.exists(data_path):
    with open(data_path, "r") as file:
        data = yaml.safe_load(file)
else:
    try:
        url = f'https://api.github.com/repos/matplotlib/matplotlib/releases?per_page=100&access_token={github_token}'
        data = json.loads(urllib.request.urlopen(url, timeout=1).read().decode())
        with open(data_path, "w") as file:
            yaml.dump(data, file)
    except Exception:
        # Fallback data in case of failure
        data = []

# Extract relevant information
dates = [datetime.strptime(item["published_at"].split("T")[0], "%Y-%m-%d") for item in data if
         'rc' not in item['tag_name'] and 'b' not in item['tag_name']]
names = [item["tag_name"] for item in data if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']]

# Create a figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Matplotlib release dates")

# a range of levels
levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates) / 6)))[:len(dates)]

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points",
                horizontalalignment="right", verticalalignment="bottom" if l > 0 else "top")

# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)

# Save figure
save_path = Path("output")
save_path.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
fig.savefig(save_path / f'timeline_matplotlib_{timestamp}.png')
fig.savefig(save_path / f'timeline_matplotlib_{timestamp}.pdf')
plt.show()
