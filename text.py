import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(raw_text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(raw_text)  # ✅ corrected here

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            word_text = word.text.lower()
            word_freq[word_text] = word_freq.get(word_text, 0) + 1

    max_freq = max(word_freq.values(), default=1)
    for word in word_freq.keys():
        word_freq[word] /= max_freq

    sent_tokens = [sent for sent in doc.sents]
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            word_text = word.text.lower()
            if word_text in word_freq:
                sent_scores[sent] = sent_scores.get(sent, 0) + word_freq[word_text]

    len_sent_scores = max(1, int(len(sent_scores) * 0.2))  # ensure at least one sentence
    summary_sents = nlargest(len_sent_scores, sent_scores, key=sent_scores.get)
    final_summary = [sent.text for sent in summary_sents]
    summary = " ".join(final_summary)

    print("Original Length: ", len(raw_text.split()))
    print("Summary Length: ", len(summary.split()))
    return summary, doc, len(raw_text.split()), len(summary.split())
