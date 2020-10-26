from markdown.test_tools import TestCase


class TestHr(TestCase):
    def test_hr_before_paragraph(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                ***
                An HR followed by a paragraph with no blank line.
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <hr>
                <p>An HR followed by a paragraph with no blank line.</p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
        )
