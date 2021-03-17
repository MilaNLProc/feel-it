======================================================================
FEEL-IT: Emotion and Sentiment Classification for the Italian Language
======================================================================


.. image:: https://img.shields.io/pypi/v/feel_it.svg
        :target: https://pypi.python.org/pypi/feel_it

.. image:: https://github.com/MilaNLProc/feel-it/workflows/Python%20package/badge.svg
        :target: https://github.com/MilaNLProc/feel-it/actions

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
        :target: https://lbesson.mit-license.org/
        :alt: License



Abstract
--------

Sentiment analysis is a common task to understand people's reactions online. Still, we often need more nuanced information: is the post negative because the user is angry or because they are sad?

An abundance of approaches has been introduced for tackling both tasks. However, at least for Italian, they all treat only one of the tasks at a time. We introduce FEEL-IT, a novel benchmark corpus of Italian Twitter posts annotated with four basic emotions: anger, fear, joy, sadness. By collapsing them, we can also do sentiment analysis. We evaluate our corpus on benchmark datasets for both emotion and sentiment classification, obtaining competitive results.

We release an open-source Python library, so researchers can use a model trained on FEEL-IT for inferring both sentiments and emotions from Italian text.


* Free software: MIT license
* Documentation: https://feel-it.readthedocs.io.


Features
--------

* Emotion Classification (fear, joy, sadness, anger) in Italian
* Sentiment Classification (positive, negative) in Italian

Installing
----------

.. code-block:: bash

    pip install -U feel-it

How To Use
----------

The two classifiers are very easy to use.

.. code-block:: python

    from feel_it import EmotionClassifier, SentimentClassifier
    emotion_classifier = EmotionClassifier()

    emotion_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    >> ['joy', 'anger', 'sadness']

    sentiment_classifier = SentimentClassifier()

    sentiment_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    >> ['positive', 'negative', 'negative']

HuggingFace Models
------------------

You can find our HF Models here:


+---------------------------------------------------+--------------------+
| Name                                              | Link               |
+===================================================+====================+
| MilaNLProc/feel-it-italian-emotion                | `Emotion Model`_   |
+---------------------------------------------------+--------------------+
| MilaNLProc/feel-it-italian-sentiment              | `Sentiment Model`_ |
+---------------------------------------------------+--------------------+


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Sentiment Model`: https://huggingface.co/MilaNLProc/feel-it-italian-sentiment
.. _`Emotion Model`: https://huggingface.co/MilaNLProc/feel-it-italian-emotion
