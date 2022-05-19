import tweepy
import json

auth = tweepy.OAuth1UserHandler(
   "pSG04mSEnFVLnotD0fr2swzjk", "DQRchFKScPlG7BJ8v7OQxbOp1MhRgGRZj2Jc5nAXuMNHPd1Q7M",
   "1524105428174528518-0c7n4zWKMJpWbHjujHXJv77jKgr97v", "CIZcQYchG6khxuSZOf2pF2f0nQVDpGiZzXLOhW8ZqZr5H"
)


api = tweepy.API(auth)
print(api.home_timeline())

find = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAIvxcQEAAAAAtoluJJRwQ%2B7as0P10nDd17w9lfA%3DDGdwjW2Idu7Hib6ZLDTu6ChYAfubOsRKpnZ6C5VTXTMRTmDcMt")
res = find.search_recent_tweets(query="covid")
print(res[0])







