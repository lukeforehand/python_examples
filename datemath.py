#! /usr/bin/python

# date math seems to really suck
# this script demonstrates correct transform of a datetime object
# to a timestamp or a string

from datetime import datetime, timedelta
import calendar
now = datetime.utcnow()
now_timestamp = calendar.timegm(now.utctimetuple())
now_string = now.strftime('%Y-%m-%dT%H:%M:%SZ')
yesterday = now - timedelta(days=1)
print now
print now_timestamp
print now_string
print yesterday
