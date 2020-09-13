"""Transcribe speech from a video stored on GCS."""
"""API key is needed for authentication"""

# Path should be of form "gs://quiz-videos/<video name>"


# Import libraries for text preprocessing

# You only need to download these resources once. After you run this
# the first time--or if you know you already have these installed--
# you can comment these two lines out (with a #)
from google.cloud import videointelligence
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import re
nltk.download('stopwords')
nltk.download('wordnet')


def transcribe(path):
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]

    config = videointelligence.types.SpeechTranscriptionConfig(
        language_code="en-US", enable_automatic_punctuation=True
    )
    video_context = videointelligence.types.VideoContext(
        speech_transcription_config=config
    )

    operation = video_client.annotate_video(
        input_uri=path, features=features, video_context=video_context
    )

    print("\nProcessing video for speech transcription.")

    result = operation.result(timeout=600)

    content = ""

    # There is only one annotation_result since only
    # one video is processed.
    annotation_results = result.annotation_results[0]

    # The number of alternatives for each transcription is limited by
    # SpeechTranscriptionConfig.max_alternatives.
    # Each alternative is a different possible transcription
    # and has its own confidence score.

    # for alternative in speech_transcription.alternatives:
    #     content += alternative.transcript

    # Returns whole transcript
    return "".join(annotation_results.speech_transcriptions)


"""Returns top num_keywords words and num_keywords bigrams of a given text"""


def top_keywords(content, num_keywords):
    # Creates stop words
    stop_words = set(stopwords.words("english"))

    # Pre-process dataset to get a cleaned and normalised text corpus
    # Remove punctuation
    text = re.sub('[^a-zA-Z]', ' ', content)

    # Convert to lowercase
    text = text.lower()

    # Remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # Remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)

    # Convert to list from string
    text = text.split()

    # Stemming
    ps = PorterStemmer()

    # Lemmatisation
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if not word in
            stop_words]
    text = " ".join(text)

    # Needed for it to work properly
    input = [text]

    cv = CountVectorizer(max_df=1, stop_words=stop_words,
                         max_features=10000, ngram_range=(1, 3))
    X = cv.fit_transform(input)

    # Get most frequently occuring keywords
    vec = CountVectorizer().fit(input)
    bag_of_words = vec.transform(input)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in
                  vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1],
                        reverse=True)
    top_words = words_freq[:num_keywords]

    vec1 = CountVectorizer(ngram_range=(2, 2),
                           max_features=2000).fit(input)
    bag_of_words = vec1.transform(input)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in
                  vec1.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1],
                        reverse=True)
    top2_words = words_freq[:num_keywords]

    return (top_words, top2_words)
