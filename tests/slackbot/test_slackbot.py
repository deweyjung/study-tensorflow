import os
import time
import re
from slackclient import SlackClient
from slacker import Slacker
import websocket

token = ''
slack = Slacker(token)
slack.chat.post_message('#study-tensorflow', 'test message for new channel')



# instantiate Slack client
# slack_client = SlackClient('xoxb-470902892800-471037595441-Ym2bPtmNOnd6CJCgE9gsufzv')
# # starterbot's user ID in Slack: value is assigned after the bot starts up
# starterbot_id = None
#
# # constants
# RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
# EXAMPLE_COMMAND = "do"
# MENTION_REGEX = "^<@(|[WU].+?)>(.*)"