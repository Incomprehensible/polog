import time
import pytest
from polog.handlers.vkapi.sender import VK_sender
from polog import log, config
import sys
from my_config import MY_TOKEN, MY_ID

lst = []

config.add_handlers(VK_sender(MY_TOKEN, MY_ID))


def test_send_normal():
    log('kek')
    time.sleep(0.05)
