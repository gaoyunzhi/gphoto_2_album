#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'gphoto_2_album'

import cached_url
from bs4 import BeautifulSoup
from telegram_util import AlbumResult as Result
	
def getImages(content):
	

def get(url):
	r = Result()
	content = cached_url.get(url, force_cache=True)
	soup = BeautifulSoup(content, 'html.parser')
	r.title = soup.get('meta', {'property': 'og:title'})['content']
	r.cap_html = r.title
	r.imgs = getImages(content)
