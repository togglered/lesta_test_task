import re
import math

from .models import File


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zа-яё\s]', '', text)
    return text.split()


def calculate_tf_idf(text):
    words = preprocess_text(text)
    all_files = File.objects.all()
    total_files = len(all_files)
    word_file_count = {}
    results = []
    results = []
    idf = {}

    if not words:
        return []
    
    tf = {}
    for word in words:
        tf[word] = 0
    for word in words:
        tf[word] += 1

    if total_files > 1:
        for file in list(all_files):
            text_file = file.file.read().decode('utf-8')
            temp_file_words = preprocess_text(text_file)
            for word in temp_file_words:
                if word in word_file_count:
                    word_file_count[word] += 1
                else:
                    word_file_count[word] = 0
        for word in words:
            files_with_word = word_file_count.get(word, 0)
            idf[word] = math.log((total_files + 1) / (files_with_word + 1)) + 1

    for word in set(words):
        results.append({
            'word': word,
            'tf': tf[word],
            'idf': idf[word] if word in idf else 0,
        })
    return results
