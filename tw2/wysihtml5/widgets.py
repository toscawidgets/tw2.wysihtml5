import tw2.core as twc


class Wysihtml5(twc.Widget):
    template = "genshi:tw2.wysihtml5.templates.wysihtml5"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/wysihtml5.js'),
        twc.CSSLink(modname=__name__, filename='static/wysihtml5.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Wysihtml5, self).prepare()
        # put code here to run just before the widget is displayed
