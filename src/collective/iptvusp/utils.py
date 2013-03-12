# -*- coding:utf-8 -*-
from collective.iptvusp.config import BASE_URL
from collective.iptvusp.config import VIDEO_IDENTIFIER
from collective.iptvusp.config import IMAGE_URL
from urllib2 import urlopen
from plone.namedfile.file import NamedImage


def get_video_id(url):
    ''' '''
    if url:
        params = url.replace(BASE_URL, '')
        params = params.split('&')
        for param in params:
            if VIDEO_IDENTIFIER in param:
                param = param.split('=')
                return param[1]
    return ''


def update_image(obj):
    ''' Return image data '''
    if not obj.image:
        video_address = obj.remote_url
        video_id = get_video_id(video_address)
        image_address = (IMAGE_URL % video_id).replace('..', '.')
        data = urlopen(image_address).read()
        obj.image = NamedImage(data, 'image/jpeg', u'%s.jpg' % video_id)
