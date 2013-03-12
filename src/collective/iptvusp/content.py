# -*- coding: utf-8 -*-
from five import grok
from plone.directives import dexterity, form
from plone.z3cform.fieldsets.utils import move
from collective.iptvusp.config import BASE_EMBED
from collective.iptvusp.config import BASE_URL
from collective.iptvusp.config import EMBED

from collective.iptvusp.interfaces import IIPTVUSPLayer


grok.templatedir('templates')

label_related = u'Material relacionado'

desc_related = (u'Notícias, textos, vídeos e outros conteúdos ligados '
                u'ao evento ou à sua temática.')


class IUSPVideo(form.Schema):
    """
    A video from the IPTV USP Service
    """
    form.model("models/uspvideo.xml")


# FIXME: we must inherit from dexterity.Item but we have to fix issue #48
class USPVideo(dexterity.Item):
    """
    """
    grok.implements(IUSPVideo)


class View(grok.View):
    grok.context(IUSPVideo)
    grok.require('zope2.View')
    grok.name('view')

    @property
    def width(self):
        return self.context.width

    @property
    def height(self):
        return self.context.height

    def cooked_source(self):
        url = self.context.remote_url
        return url.replace(BASE_URL, BASE_EMBED)

    def embed(self):
        ''' Return the code to be embedded '''
        params = {}
        params['width'] = self.width
        params['height'] = self.height
        params['src'] = self.cooked_source()
        return EMBED % params


class AddForm(dexterity.AddForm):
    """ Change Add View to move fields to default tab.
    """
    grok.name('iptvusp.uspvideo')
    grok.context(IUSPVideo)
    grok.layer(IIPTVUSPLayer)

    def update(self):
        super(AddForm, self).update()
        move(self, 'IRelatedItems.relatedItems', after='duracao')
        super(AddForm, self).update()
        self.widgets['IRelatedItems.relatedItems'].label = label_related
        self.widgets['IRelatedItems.relatedItems'].description = desc_related

    def updateWidgets(self):
        super(AddForm, self).updateWidgets()
        self.widgets['IDublinCore.description'].label = u'Sinopse'
        self.widgets['IDublinCore.description'].rows = 4
        self.widgets['IDublinCore.description'].style = u'width: 100%;'
        self.widgets['IDublinCore.contributors'].rows = 4
        self.widgets['IDublinCore.contributors'].style = u'width: 50%;'


class EditForm(dexterity.EditForm):
    """ Change Edit View to move fields to default tab.
    """
    grok.name('iptvusp.uspvideo')
    grok.context(IUSPVideo)
    grok.layer(IIPTVUSPLayer)

    def update(self):
        super(EditForm, self).update()
        move(self, 'IRelatedItems.relatedItems', after='duracao')
        super(EditForm, self).update()
        self.widgets['IRelatedItems.relatedItems'].label = label_related
        self.widgets['IRelatedItems.relatedItems'].description = desc_related

    def updateWidgets(self):
        super(EditForm, self).updateWidgets()
        self.widgets['IDublinCore.description'].label = u'Sinopse'
        self.widgets['IDublinCore.description'].rows = 4
        self.widgets['IDublinCore.description'].style = u'width: 100%;'
        self.widgets['IDublinCore.contributors'].rows = 4
        self.widgets['IDublinCore.contributors'].style = u'width: 50%;'
