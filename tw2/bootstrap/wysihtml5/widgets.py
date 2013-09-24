'''
Created on May 14, 2013

@author: moschlar
'''

import tw2.core as twc
import tw2.jquery as twj
import tw2.bootstrap.forms as twbf

from tw2.wysihtml5.widgets import wysihtml5_js, parsers

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

    parser = twc.Param(
        'The set of parser rules to use. '
        'The simple parser contains only basic html5 tags, while the '
        'advanced parser contains more html5 tags and preserves some '
        'css classes. If you use the simple parser, the editor css is '
        'not strictly needed. '
        'If you set the parser to False, you completely disable parsing, '
        'which is potentially unsafe, but a lot more convenient.',
        default=True)

    # TODO: Color support
    # Explicitly disable stylesheets, because wysiwyg-color.css is fetched otherwise
    stylesheets = twc.Param(default=list())
    wysihtml5_args = twc.Param(default=dict())

    def prepare(self):
        super(Wysihtml5, self).prepare()
        wysihtml5_args = self.wysihtml5_args.copy()
        wysihtml5_args.update(stylesheets=self.stylesheets)
        if self.parser and self.parser in parsers:
            self.safe_modify('resources')
            self.resources.append(parsers[self.parser])
            wysihtml5_args.update(parserRules=twc.js_symbol('wysihtml5ParserRules'))
        if self.parser is False:
            wysihtml5_args.update(parser=twc.js_symbol('function(elementOrHtml, rules, context, cleanUp) { return elementOrHtml; }'))
        self.add_call(twj.jQuery(self.selector).wysihtml5(wysihtml5_args))
