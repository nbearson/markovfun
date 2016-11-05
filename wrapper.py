#!/usr/bin/env python
"""
simple fun wrappers around https://github.com/jsvine/markovify
"""

import markovify


def load(textfile):
    with open(textfile) as f:
        text = f.read()
    text_model = markovify.Text(text)
    text_model.length = len(text)
    return text_model


def sentences(model, n=5):
    print(model.make_sentence())


def tweets(model, n=10):
    for i in range(n):
        print(model.make_short_sentence(140))


def combine(models):
    total_length = sum([m.length for m in models])
    # weights are inversely proportional to size, so a large text doesn't drown out a small one
    weights = [((total_length - m.length) / total_length) for m in models]
    return markovify.combine(models, weights)


def tweet_these(files):
    models = [load(f) for f in files]
    tweets(combine(models))
