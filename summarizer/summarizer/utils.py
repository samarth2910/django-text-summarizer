import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(raw_text):
    stopwords = list(STOP_WORDS)

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(raw_text)  # Process the input text

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text.lower() not in word_freq:
                word_freq[word.text.lower()] = 1
            else:
                word_freq[word.text.lower()] += 1

    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq

    sent_tokens = [sent for sent in doc.sents]
    sent_scores = {}

    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in word_freq:
                if sent not in sent_scores:
                    sent_scores[sent] = word_freq[word.text.lower()]
                else:
                    sent_scores[sent] += word_freq[word.text.lower()]

    len_sent_scores = int(len(sent_scores) * 0.2)  # Top 20% of sentences
    summary = nlargest(len_sent_scores, sent_scores, key=sent_scores.get)
    final_summary = [sent.text for sent in summary]
    summary = " ".join(final_summary)
    
    return summary, doc, len(raw_text.split()), len(summary.split())
