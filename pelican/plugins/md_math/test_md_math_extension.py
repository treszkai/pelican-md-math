from markdown.test_tools import TestCase

from pelican.plugins.md_math import MarkdownMathExtension


class TestMathExtension(TestCase):
    def test_math_inline(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                r"""
                Foo \( bar _baz_ qux \),
                lorem $a_b$ ipsum $4.00 $5.00,
                `do $not$ parse`
                """
            ),
            # The expected HTML output
            self.dedent(
                r"""
                <p>Foo <script type="math/tex"> bar _baz_ qux </script>,
                lorem <script type="math/tex">a_b</script> ipsum $4.00 $5.00,
                <code>do $not$ parse</code></p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
            extensions=['pelican.plugins.md_math'],
        )

    def test_math_display_square(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                r"""
                \[Foo _bar_ baz;
                `even this is copy-paste`
                \]
                """
            ),
            # The expected HTML output
            self.dedent(
                r"""
                <script type="math/tex; mode=display">% <![CDATA[
                Foo _bar_ baz;
                `even this is copy-paste` %]]></script>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
            extensions=[MarkdownMathExtension()],
        )

    def test_math_display_dollars(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                r"""
                $$Foo _bar_ baz;
                `even this is copy-paste`
                $$
                """
            ),
            # The expected HTML output
            self.dedent(
                r"""
                <script type="math/tex; mode=display">% <![CDATA[
                Foo _bar_ baz;
                `even this is copy-paste` %]]></script>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
            extensions=[MarkdownMathExtension()],
        )
