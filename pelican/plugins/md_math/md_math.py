import sys

from pelican import signals

try:
    from .md_math_extension import MarkdownMathExtension
except ImportError:
    MarkdownMathExtension = None


def math_for_markdown(pelicanobj):
    """Registers a custom markdown extension for handling math tags"""

    try:
        pelicanobj.settings["MARKDOWN"].setdefault("extensions", []).append(
            MarkdownMathExtension()
        )
    except Exception:
        sys.excepthook(*sys.exc_info())
        sys.stderr.write(
            "\nError - the pelican mathjax markdown extension failed to configure. MathJax is non-functional.\n"
        )
        sys.stderr.flush()


def pelican_init(pelicanobj):
    """
    Loads the mathjax script according to the settings.
    Instantiate the Python markdown extension, passing in the mathjax
    script as config parameter.
    """
    if MarkdownMathExtension:
        math_for_markdown(pelicanobj)


def register():
    """Plugin registration"""
    signals.initialized.connect(pelican_init)
