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

.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/drive/1e8h__sK73r4uwknxRJfsCMC36dLuZBa8?usp=sharing
    :alt: Colab Tutorial
    
.. image:: https://raw.githubusercontent.com/aleen42/badges/master/src/medium.svg
    :target: https://towardsdatascience.com/sentiment-analysis-and-emotion-recognition-in-italian-using-bert-92f5c8fe8a2
    :alt: Medium Blog Post

Abstract
--------

Sentiment analysis is a common task to understand people's reactions online. Still, we often need more nuanced information: is the post negative because the user is angry or because they are sad?

An abundance of approaches has been introduced for tackling both tasks. However, at least for Italian, they all treat only one of the tasks at a time. We introduce FEEL-IT, a novel benchmark corpus of Italian Twitter posts annotated with four basic emotions: anger, fear, joy, sadness. By collapsing them, we can also do sentiment analysis. We evaluate our corpus on benchmark datasets for both emotion and sentiment classification, obtaining competitive results.

We release an open-source Python library, so researchers can use a model trained on FEEL-IT for inferring both sentiments and emotions from Italian text.

License
-------

Code comes from HuggingFace and thus our License is an MIT license.

For models restrictions may apply on the data (which are derived from existing datasets) or Twitter (main data source). We refer users to the original licenses accompanying each dataset and Twitter regulations.

Data Access
-----------

Send us an email :)

Features
--------

* Emotion Classification (fear, joy, sadness, anger) in Italian
* Sentiment Classification (positive, negative) in Italian

Installing
----------

.. code-block:: bash

    pip install -U feel-it

Jump start Tutorials
--------------------

.. |colab1| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/drive/1e8h__sK73r4uwknxRJfsCMC36dLuZBa8?usp=sharing
    :alt: Colab Tutorial


+--------------------------------------------------------------------------------+------------------+
| Name                                                                           | Link             |
+================================================================================+==================+
| Sentiment and Emotion Classification (stable **v1.0.2**)                       | |colab1|         |
+--------------------------------------------------------------------------------+------------------+

How To Use
----------

The two classifiers are very easy to use. You can also directly use our colab tutorial!

.. code-block:: python

    from feel_it import EmotionClassifier, SentimentClassifier
    
    emotion_classifier = EmotionClassifier()

    emotion_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    >> ['joy', 'anger', 'sadness']

    sentiment_classifier = SentimentClassifier()

    sentiment_classifier.predict(["sono molto felice", "ma che cazzo vuoi", "sono molto triste"])
    >> ['positive', 'negative', 'negative']


Citation
--------

Please use the following bibtex entry if you use this model in your project:

::

  @inproceedings{bianchi2021feel,
    title = {{"FEEL-IT: Emotion and Sentiment Classification for the Italian Language"}},
    author = "Bianchi, Federico and Nozza, Debora and Hovy, Dirk",
    booktitle = "Proceedings of the 11th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis",
    year = "2021",
    publisher = "Association for Computational Linguistics",
  }


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


Development Team
----------------

* `Federico Bianchi`_ <f.bianchi@unibocconi.it> Bocconi University
* `Debora Nozza`_ <debora.nozza@unibocconi.it> Bocconi University
* `Dirk Hovy`_ <dirk.hovy@unibocconi.it> Bocconi University

Note
----

Remember that this is a research tool :)


Other Resources
---------------

+ https://github.com/RacheleSprugnoli/Esercitazioni_SA (very nice dataset for emotion analysis)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Sentiment Model`: https://huggingface.co/MilaNLProc/feel-it-italian-sentiment
.. _`Emotion Model`: https://huggingface.co/MilaNLProc/feel-it-italian-emotion
.. _Federico Bianchi: https://federicobianchi.io
.. _Debora Nozza: https://dnozza.github.io/
.. _Dirk Hovy: https://dirkhovy.com/
