#!/usr/bin/env python
"""
Simple example of a syntax-highlighted HTML input line.
"""
from __future__ import unicode_literals
from pygments.lexers import HtmlLexer
from prompt_toolkit.shortcuts import get_input


def main():
    text = get_input('Enter HTML: ', lexer=HtmlLexer)
    print('You said: %s' % text)


if __name__ == '__main__':
    main()
