# -*- coding: utf-8 -*-

from textblob import TextBlob
from textblob_de import TextBlobDE


text = TextBlob("Markus is angry because he never gets the biggest chocolate.")
print(text.tags)
print(text.sentiment.polarity)
print(text.sentiment)

text = TextBlobDE("Markus ist wütend weil er nie die grösste Schokolade erhält.".decode('utf-8'))
print(text.tags)
print(text.sentiment.polarity)
print(text.sentiment)

text = TextBlobDE("Markus ist glücklich weil er immer die grösste Schokolade erhält.".decode('utf-8'))
print(text.tags)
print(text.sentiment.polarity)
print(text.sentiment)