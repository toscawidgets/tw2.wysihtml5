import tw2.core as twc
import tw2.forms as twf

try:
    import tw2.bootstrap as twb
    TextArea = twb.TextArea
except ImportError:
    twb = None
    TextArea = twf.TextArea

wysihtml5_js = twc.JSLink(
    filename='static/wysihtml5-0.3.0.js')
wysihtml5_editor_css = twc.CSSLink(
    filename='static/editor.css')

wysihtml5_parser_simple = twc.JSLink(
    filename='static/simple.js')
wysihtml5_parser_advanced = twc.JSLink(
    filename='static/advanced.js')


class Wysihtml5(TextArea):
    template = "mako:tw2.wysihtml5.templates.wysihtml5"

    resources = [
        wysihtml5_js
    ]

    parser_rules = twc.Param(
        'The set of parser rules to use. Has to be a twc.JSLink.',
        default=wysihtml5_parser_simple)
    toolbar_id = twc.Variable(
        default='wysihtml5-toolbar')

    @classmethod
    def post_define(cls):
        if twb:
            cls.template = "mako:tw2.wysihtml5.templates.wysihtml5-bootstrap"

    def prepare(self):
        super(Wysihtml5, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError('WYSIHTML5 must be supplied an id')

        self.resources.append(self.parser_rules)
        self.toolbar_id = self.compound_id + '-toolbar'
        self.resources.append(twc.JSSource(src="""
var editor = new wysihtml5.Editor("%s", {
    toolbar:  "%s",
    parserRules:  wysihtml5ParserRules,
    stylesheets: ["/resources/%s/%s"]
});
""" % (self.compound_id, self.toolbar_id,
        wysihtml5_editor_css.guess_modname(), wysihtml5_editor_css.filename)))
