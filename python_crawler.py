# Purpose: this is a demo webcrawler that reads RSS Feeder information
#          from the target website, filter to the desired content
#          and save to a local file.
#
# Demo Input: deal website https://slickdeals.net trending deal RSS Feeds
# Demo Output: csv file 'deal_filter.csv' with deal content and links
# Author: F. W.
# June 14, 2018
#
# Ref: https://www.idiotinside.com/2017/06/08/parse-rss-feed-with-python/
#
# Prerequisite:
# * 'pip install feedparser'

import feedparser
import pandas as pd

# The 'trending deal' RSS Feeds page
feed = feedparser.parse("http://feeds.feedburner.com/SlickdealsnetUP")

# Create a data frame to store the filtered data
feed_entries = feed.entries
nDeal = len(feed_entries)
filter_data = pd.DataFrame(index=range(nDeal), columns=['Title', 'Link', 'OriginalLink'])

# Assign each filtered entry into one data frame record
rec = 0
for entry in feed_entries:

    deal_link = entry.link
    feedburner_origlink = entry.feedburner_origlink
    deal_title = entry.title_detail.value

    filter_data.loc[rec, 'Title'] = deal_title
    filter_data.loc[rec, 'Link'] = deal_link
    filter_data.loc[rec, 'OriginalLink'] = feedburner_origlink

    rec = rec + 1

# Save the filtered data to a csv file
filter_data.to_csv('deal_filter.csv', sep=',', encoding='utf-8')