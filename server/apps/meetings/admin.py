# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from core import utils

from . import models

utils.site_register(models.Room, editable=False, addable=False, changeable=False)
utils.site_register(models.Meeting, editable=False, addable=False, changeable=False)
