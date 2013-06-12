import tw2.core as twc
import tw2.forms as twf


__all__ = [
    'Wysihtml5'
]

wysihtml5_js = twc.JSLink(
    filename='static/wysihtml5.js',
    location='headbottom')
wysihtml5_editor_css = twc.CSSLink(
    filename='static/editor.css')

wysihtml5_parser_simple = twc.JSLink(
    filename='static/simple.js',
    location='headbottom')
wysihtml5_parser_advanced = twc.JSLink(
    filename='static/advanced.js',
    location='headbottom')
parsers = dict(simple=wysihtml5_parser_simple,
    advanced=wysihtml5_parser_advanced)


class Wysihtml5(twf.TextArea):
    template = "mako:tw2.wysihtml5.templates.wysihtml5"

    resources = [
        wysihtml5_js
    ]

    parser = twc.Param(
        'The set of parser rules to use. '
        'The simple parser contains only basic html5 tags, while the '
        'advanced parser contains more html5 tags and preserves some '
        'css classes. If you use the simple parser, the editor css is '
        'not strictly needed.',
        default='advanced')
    toolbar_id = twc.Variable(
        default='wysihtml5-toolbar')

    def prepare(self):
        super(Wysihtml5, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError('WYSIHTML5 must be supplied an id')

        self.resources.append(parsers[self.parser])
        self.toolbar_id = self.compound_id + '-toolbar'
        self.resources.append(twc.JSSource(src="""
var editor = new wysihtml5.Editor("%s", {
    toolbar:  "%s",
    parserRules:  wysihtml5ParserRules,
    stylesheets: ["/resources/%s/%s"]
});
""" % (self.compound_id, self.toolbar_id,
        wysihtml5_editor_css.guess_modname(), wysihtml5_editor_css.filename)))
