import unittest

from markdown.test_tools import TestCase

from pelican.plugins.md_math import MathExtension


class TestMathExtension(TestCase):
    def test_math_inline(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                r"""
                Foo \( bar _baz_ qux \),
                this\(a\)no space around
                lorem $a_b$ ipsum $4.00 $5.00,
                `do $not$ parse`
                """
            ),
            # The expected HTML output
            self.dedent(
                r"""
                <p>Foo <script type="math/tex"> bar _baz_ qux </script>,
                this<script type="math/tex">a</script>no space around
                lorem <script type="math/tex">a_b</script> ipsum $4.00 $5.00,
                <code>do $not$ parse</code></p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
            extensions=['pelican.plugins.md_math'],
        )

    def test_math_inline_newline(self):
        """Check that paren-style inline math is processed even if contains a newline"""
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                r"""
                Foo \( bar _baz_
                qux \),
                lorem ipsum $do
                not$.
                """
            ),
            # The expected HTML output
            self.dedent(
                r"""
                <p>Foo <script type="math/tex"> bar _baz_
                qux </script>,
                lorem ipsum $do
                not$.</p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html',
            extensions=[MathExtension()],
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
            extensions=[MathExtension()],
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
            extensions=[MathExtension()],
        )

    @unittest.expectedFailure
    def test_math_header_only(self):
        """If meta plugin is enabled, then math is parsed only if latex:true in header"""
        for header in ['', 'Title: Lorem ipsum', 'latex: false']:
            with self.subTest(header=header):
                self.assertMarkdownRenders(
                    # The Markdown source text used as input
                    self.dedent(
                        rf"""
                        {header}

                        Foo \( bar _baz_ qux \)

                        \[
                        bar _baz_ qux
                        \]
                        """
                    ),
                    # The expected HTML output
                    self.dedent(
                        r"""
                        <p>Foo ( bar <em>baz</em> qux )</p>
                        <p>[
                        bar <em>baz</em> qux
                        ]</p>
                        """
                    ),
                    # Other keyword arguments to pass to `markdown.markdown`
                    output_format='html',
                    extensions=['pelican.plugins.md_math', 'meta'],
                )
