#!/usr/bin/env python

"""Tests for `feel_it` package."""
from feel_it import EmotionClassifier, SentimentClassifier

def test_classifiers_basic_functionality():

    emotion_classifier = EmotionClassifier()

    prediction = emotion_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    assert prediction == ['joy', 'anger', 'sadness']

    sentiment_classifier = SentimentClassifier()

    prediction = sentiment_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    assert prediction == ['positive', 'negative', 'negative']
