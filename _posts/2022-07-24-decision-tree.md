---
layout: default
title: Blog title
---

## Blog title

Here is a Jupyter Notebook on Blog using a string literal:

{::nomarkdown}
{% jupyter_notebook "/notebooks/decision_tree.ipynb" %}
{:/nomarkdown}

Here is the same Jupyter Notebook on Blog using a variable:

{::nomarkdown}
{% assign notebook_path = "/notebooks/decision_tree.ipynb" %}
{% jupyter_notebook notebook_path %}
{:/nomarkdown}
