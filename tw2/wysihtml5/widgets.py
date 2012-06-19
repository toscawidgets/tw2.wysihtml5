import tw2.core as twc
import tw2.forms as twf

wysihtml5_js = twc.JSLink(
    filename='static/wysihtml5-0.3.0.js')
wysihtml5_parser_simple = twc.JSLink(
    filename='static/simple.js')
wysihtml5_parser_advanced = twc.JSLink(
    filename='static/advanced.js')


class Wysihtml5(twf.TextArea):
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
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Wysihtml5, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError('WYSIHTML5 must be supplied an id')

        self.resources.append(self.parser_rules)
        self.toolbar_id = self.compound_id + '-toolbar'
        self.resources.append(twc.JSSource(src="""
var editor = new wysihtml5.Editor("%s", { toolbar:  "%s", parserRules:  wysihtml5ParserRules });
""" % (self.compound_id, self.toolbar_id)))
