# -*- coding: utf-8 -*-
from collective.iptvusp import _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class IIPTVUSPSettings(Interface):
    """ Interface for the control panel form.
    """

    update_metadata = schema.Bool(
        title=_(u"Update metadata (from IPTV site)"),
        required=False,
    )


class IPTVUSPSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IIPTVUSPSettings
    label = _(u'IPTV USP Settings')
    description = _(u'Settings for the collective.iptvusp package')


class IPTVUSPSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = IPTVUSPSettingsEditForm
