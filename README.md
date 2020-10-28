# Convert math content: A Plugin for Pelican

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/md-math/build)](https://github.com/treszkai/pelican-md-math/actions) [![PyPI Version](https://img.shields.io/pypi/v/pelican-md-math)](https://pypi.org/project/pelican-md-math/)

Extension for Python-Markdown to convert math tags to math scripts, plus an extension for the [Pelican static site generator](https://github.com/getpelican/pelican).

Usage
-----

1. Install package (see [below](#Installation))
2. For Pelican: set up KaTeX header.
3. For Pelican (optionally): set up shortcuts for your favorite symbols or macros.
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

For Pelican, you just need to install the package:

```
python -m pip install git+https://github.com/treszkai/pelican-md-math.git
```

For Markdown usage, you also need to specify:

```python
import markdown
md = markdown.Markdown(extensions=['pelican.plugins.md_math'])
```

Known limitations
-----------------

- Doesn’t create a display block if it contains an empty line
- Doesn’t ignore an escaping backslash before the `\(` or `$` tags.
- `]]>` in the math input will probably mess up the HTML output.


Contributing
------------

[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

If you find an issue in this extension, then please open a pull request.
