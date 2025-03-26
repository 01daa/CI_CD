import re

def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Считаем количество слов (по пробелам и разделителям)
    words = re.findall(r'\w+', text)
    word_count = len(words)

    # Считаем количество предложений (по знакам окончания)
    # Добавим проверку на конец текста
    text = text.strip()  # Убираем пробелы в начале и в конце
    if text and not re.search(r'[.!?]$', text):
        text += '.'  # Добавляем точку, если её нет в конце текста

    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s])  # Игнорируем пустые элементы

    return word_count, sentence_count

