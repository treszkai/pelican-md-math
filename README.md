# Convert math content: A Plugin for Pelican

Extension for Python-Markdown to convert math tags to math scripts, plus a plugin for the [Pelican static site generator](https://github.com/getpelican/pelican).

Usage
-----

1. [Install package](#Installation).
2. For Pelican: set up KaTeX header.
3. For Pelican (optionally): [set up shortcuts](#Adding-LaTeX-macros-for-Pelican) for your favorite symbols or macros.
4. For Pelican: define `latex: true` at the header of each article that should include KaTeX.
4. Write an inline math tag either by:
   - enclosing text between `\(` and `\)`, e.g. `\(foo _bar_ baz\)`, or
   - between two `$` symbols if the text contains no space, e.g. `$a_b^c$`.
5. Write a display math by surrounding an entire paragraph either with '\[' and `\]`, or with two `$$` tags. Example:

```latex
\[
    % For a visual proof, see https://link.springer.com/article/10.1007/s00283-018-9816-4
    \pi ^ e < e ^ \pi
\]
```


Installation
------------

For the Pelican plugin, you just need to install the package:

```
python -m pip install git+https://github.com/treszkai/pelican-md-math.git
```

For Markdown usage, you also need to specify the path or instance of the extension:

```python
import markdown
md = markdown.Markdown(extensions=['pelican.plugins.md_math'])
```

```python
import markdown
from pelican.plugins.md_math import MarkdownMathExtension

md = markdown.Markdown(extensions=[MarkdownMathExtension()])
```

Setting up KaTeX headers for Pelican
====================================

Two steps are required:
 - Copy the supplied [katex.html] file to your theme's templates directory.
 - Modify the necessary templates (e.g. `article.html` for the article pages) with adding the following in the `{% block head %}` block, before the `{% endblock %}` tag. (An _example_ [article.html] is supplied.)

```html
  {% if (article.latex is defined and article.latex) or article.latex_macros is defined %}
    {% include 'katex.html' %}
  {% endif %}
```

Adding LaTeX macros for Pelican
-------------------------------

Site-level macros
=================

Define a `LATEX_MACROS` dictionary in `pelicanconf.py`:

```python
LATEX_MACROS = {
    r'\RR': r'\mathbb{R}',
    r'\EE': r'\mathbb{E}',
    r'\indep': r'\perp\!\!\!\perp',
    r'\emptyset': r'\varnothing',
    r'\Godel': r'\ulcorner #1 \urcorner',
}
```

These can be used as ordinary LaTeX macros, e.g. `\RR` or `\Godel{\phi}`.
The latter example demonstrates a parametric macro.

Article-level macros
====================

You can define `latex_macros` in the article header as follows:

```
latex: true
latex_macros:
    "\D": "\mathcal{D}"
    "\N": "\mathcal{N}"
    "\Godel": "\ulcorner #1 \urcorner"
```

(In the presence of `latex_macros`, you don't need the `latex: true` line.)

Known limitations
-----------------

- Doesn’t create a display block if it contains an empty line
- Doesn’t ignore an escaping backslash before the `\(` or `$` tags.
- `]]>` in the math input will probably mess up the HTML output.
- All files are parsed, regardless of whether latex is enabled.

Contributing
------------

[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

If you find an issue in this extension, then please open a pull request.
