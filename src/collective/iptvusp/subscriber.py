# -*- coding: utf-8 -*-
from collective.iptvusp.config import IMAGE_URL
from collective.iptvusp.utils import get_video_id
from collective.iptvusp.content import IUSPVideo
from plone.namedfile.file import NamedImage
from five import grok
from zope.app.container.interfaces import IObjectAddedEvent
from urllib2 import urlopen


@grok.subscribe(IUSPVideo, IObjectAddedEvent)
def set_image(obj, event):
    ''' Set an image to be used in content listings '''
    if not obj.image:
        video_address = obj.remote_url
        video_id = get_video_id(video_address)
        image_address = (IMAGE_URL % video_id).replace('..', '.')
        data = urlopen(image_address).read()
        obj.image = NamedImage(data, 'image/jpeg', u'%s.jpg' % video_id)
