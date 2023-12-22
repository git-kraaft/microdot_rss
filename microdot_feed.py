#!/usr/bin/env python

import time
import microdotphat             
import feedparser

def display_header(header):
    microdotphat.clear()
    microdotphat.scroll_to(position_x=0, position_y=0)
    microdotphat.write_string(header, offset_y = 7, kerning=False)
    for x in range(7):
        microdotphat.scroll_vertical()
        microdotphat.show()
        time.sleep(0.02)

def cleanup_text(text):
    text = text.replace("«", "\"")
    text = text.replace("»", "\"")
    text = text.replace("–", "-")
    text = text.replace(" ", "-")   # Four-Per-Em Space &#x2005
    print(text)
    for string in text:
        print(ord(string))

    return text

nzz_rss_url = "https://www.nzz.ch/startseite.rss"

feed = feedparser.parse( nzz_rss_url )

for post in feed.entries:
    display_header("NZZ")
    feed_title = cleanup_text(post.title)
    microdotphat.clear()
    microdotphat.scroll_to(position_x=0, position_y=0)
    microdotphat.write_string(feed_title, offset_x=0, kerning=False)
    microdotphat.show()
    time.sleep(1.5)

    for i in feed_title[6:]:
        microdotphat.scroll(amount_x=8)
        microdotphat.show()
        time.sleep(0.2)

    time.sleep(1.5)

