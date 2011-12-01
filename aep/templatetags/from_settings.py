from django.template import TemplateSyntaxError, Variable, Node, Variable, Library
from django.conf import settings

register = Library()

class FromSettings(Node):
    def __init__(self, settingsvar, asvar):
        self.arg = Variable(settingsvar)
        self.asvar = asvar
    def render(self, context):
        ret_val = getattr(settings, str(self.arg))
        if self.asvar:
            context[self.asvar] = ret_val
            return ''
        else:
            return ret_val

@register.tag
def from_settings(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one " \
                                  "argument (settings constant to retrieve)" % bits[0])
    settingsvar = bits[1]
    settingsvar = settingsvar[1:-1] if settingsvar[0] == '"' else settingsvar
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]
    if len(bits):
        raise TemplateSyntaxError("'value_from_settings' didn't recognise " \
                                  "the arguments '%s'" % ", ".join(bits))
    return FromSettings(settingsvar, asvar)

