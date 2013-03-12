# -*- coding: utf-8 -*-
from collective.iptvusp.content import IUSPVideo
from collective.iptvusp.utils import update_image
from five import grok
from zope.app.container.interfaces import IObjectAddedEvent


@grok.subscribe(IUSPVideo, IObjectAddedEvent)
def set_image(obj, event):
    ''' Set an image to be used in content listings '''
    if not obj.image:
        update_image(obj)
