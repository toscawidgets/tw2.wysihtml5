'''
Created on May 14, 2013

@author: moschlar
'''

import tw2.core as twc
import tw2.jquery as twj
import tw2.bootstrap.forms as twbf

from tw2.wysihtml5.widgets import wysihtml5_js

__all__ = ['Wysihtml5']


bootstrap_wysihtml5_js = twc.JSLink(
    filename='static/bootstrap-wysihtml5.js',
    resources=[twj.jquery_js, twbf.bootstrap_js, wysihtml5_js],
    location='headbottom')

bootstrap_wysihtml5_css = twc.CSSLink(
    filename='static/bootstrap-wysihtml5.css',
    resources=[twbf.bootstrap_css])


class Wysihtml5(twbf.TextArea):
    resources = [bootstrap_wysihtml5_js, bootstrap_wysihtml5_css]

    wysihtml5_args = twc.Param(default=dict())

    def prepare(self):
        super(Wysihtml5, self).prepare()
        self.add_call(twj.jQuery(self.selector).wysihtml5(self.wysihtml5_args))
