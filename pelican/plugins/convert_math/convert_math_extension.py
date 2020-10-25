import xml.etree.ElementTree as etree
import re
import markdown

class MathBlockProcessor(markdown.blockprocessors.BlockProcessor):
    RE_DISPLAY_BLOCK = r'\\\[(.*)\\\]'
    ELEM_TEXT_BEGIN = '% <![CDATA[\n'
    ELEM_TEXT_END = ' %]]>'

    def test(self, parent, block):
        return re.fullmatch(self.RE_DISPLAY_BLOCK, block, re.DOTALL)

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = re.fullmatch(self.RE_DISPLAY_BLOCK, block, re.DOTALL)

        e = etree.SubElement(parent, 'script')
        e.set('type', 'math/tex; mode=display')
        e.text = self.ELEM_TEXT_BEGIN + m.group(1).strip('\n') + self.ELEM_TEXT_END

        return True

class PelicanMathExtension(markdown.Extension):

    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(MathBlockProcessor(md.parser), 'box', 175)
