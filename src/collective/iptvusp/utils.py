# -*- coding:utf-8 -*-
from collective.iptvusp.config import BASE_URL
from collective.iptvusp.config import VIDEO_IDENTIFIER


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
