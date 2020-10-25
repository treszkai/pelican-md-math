import sys

from pelican import signals

try:
    from .convert_math_extension import PelicanMathExtension
except ImportError:
    PelicanMathExtension = None


def math_for_markdown(pelicanobj):
    """Instantiates a customized markdown extension for handling mathjax
    related content"""

    try:
        pelicanobj.settings["MARKDOWN"].setdefault("extensions", []).append(
            PelicanMathExtension()
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
    if PelicanMathExtension:
        math_for_markdown(pelicanobj)

def register():
    """Plugin registration"""
    signals.initialized.connect(pelican_init)
