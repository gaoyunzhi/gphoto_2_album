#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gphoto_2_album
import yaml
from telegram.ext import Updater
import album_sender
import os

with open('credentials') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)
# chat = tele.bot.get_chat('@web_record')

def test(url, rotate=False):
	r = gphoto_2_album.get(url)
	print(r.imgs)
	album_sender.send(chat, url, r, rotate = rotate)
	
if __name__=='__main__':
	test('https://photos.google.com/share/AF1QipOtOHHWLLtS9RV6yMuIpT9qpUSnoAv2tRg9OpEH27wkf39qU-cRTpn9uJGOd_FTpw?key=a0k1NHNoYmdvY256Y2oyVWd3aXV1TlNJOUk4Wjl3')