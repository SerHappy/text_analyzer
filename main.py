import re
import pymorphy2


def read_text(filename: str) -> str:
    text = ""
    with open(filename, encoding="utf-8") as infile:
        for line in infile:
            text += line.strip() + " "
    return text


def get_words(text: str) -> list:
    return text.split()


def _delete_punctuation_marks(list_of_words: list) -> list:
    words_without_punc_marks = []
    for word in list_of_words:
        word = word.lower().strip('.,;:!«»?—()-"_/')
        if word != "":
            words_without_punc_marks.append(word)
    return words_without_punc_marks


def _delete_stopwords(list_of_words: list) -> list:
    stopwords = [
        "Джордж",
        "тер",
        "кл",
        "ту",
        "-",
        "нам",
        "нашей",
        "тому",
        "и",
        "в",
        "во",
        "не",
        "что",
        "он",
        "на",
        "я",
        "с",
        "со",
        "как",
        "а",
        "то",
        "все",
        "она",
        "так",
        "его",
        "но",
        "да",
        "ты",
        "к",
        "у",
        "же",
        "вы",
        "за",
        "бы",
        "по",
        "только",
        "ее",
        "мне",
        "было",
        "вот",
        "от",
        "меня",
        "еще",
        "нет",
        "о",
        "из",
        "ему",
        "теперь",
        "когда",
        "даже",
        "ну",
        "вдруг",
        "ли",
        "если",
        "уже",
        "или",
        "ни",
        "быть",
        "был",
        "него",
        "до",
        "вас",
        "нибудь",
        "опять",
        "уж",
        "вам",
        "ведь",
        "там",
        "потом",
        "себя",
        "ничего",
        "ей",
        "может",
        "они",
        "тут",
        "где",
        "есть",
        "надо",
        "ней",
        "для",
        "мы",
        "тебя",
        "их",
        "чем",
        "была",
        "сам",
        "чтоб",
        "без",
        "будто",
        "чего",
        "раз",
        "тоже",
        "себе",
        "под",
        "будет",
        "ж",
        "тогда",
        "кто",
        "этот",
        "того",
        "потому",
        "этого",
        "какой",
        "совсем",
        "ним",
        "здесь",
        "этом",
        "один",
        "почти",
        "мой",
        "тем",
        "чтобы",
        "нее",
        "сейчас",
        "были",
        "куда",
        "зачем",
        "всех",
        "никогда",
        "можно",
        "при",
        "наконец",
        "два",
        "об",
        "другой",
        "хоть",
        "после",
        "над",
        "больше",
        "тот",
        "через",
        "эти",
        "нас",
        "про",
        "всего",
        "них",
        "какая",
        "много",
        "разве",
        "три",
        "эту",
        "моя",
        "впрочем",
        "хорошо",
        "свою",
        "этой",
        "перед",
        "иногда",
        "лучше",
        "чуть",
        "том",
        "нельзя",
        "такой",
        "им",
        "более",
        "всегда",
        "конечно",
        "всю",
        "между",
        "сказал",
        "это",
        "сказала",
    ]
    words_without_stopwords = []
    for word in list_of_words:
        if word not in stopwords:
            words_without_stopwords.append(word)
    return words_without_stopwords


def clear_words(dirty_words: list) -> list:
    clear_words = _delete_punctuation_marks(dirty_words)
    clear_words = _delete_stopwords(clear_words)
    return clear_words


def create_freq_dict(list_of_words: list) -> dict:
    dictionary = {}
    for word in list_of_words:
        dictionary[word] = dictionary.setdefault(word, 0) + 1
    return dictionary


def sort_dict_by_value(dictionary: dict, reversed_order: bool) -> dict:
    return dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=reversed_order)
    )


def get_sentences(text) -> list:
    return re.split(r' *[\.\?!][\'"\)\]]* *', text)


def get_all_length_sentences(text):
    list_of_sentences = get_sentences(text)
    length = 0
    for sentence in list_of_sentences:
        length += len(sentence)
    return length


def average_sentence_length(text):
    return get_all_length_sentences(text) / get_number_of_sentences(text)


def get_number_of_sentences(text: str) -> int:
    return len(re.split(r' *[\.\?!][\'"\)\]]* *', text))


def get_number_of_punctuation_marks(text):
    punctuation_marks = ".,;:!«»?—()-\"'"
    amount_of_punc_marks = 0
    for i in text:
        if i in punctuation_marks:
            amount_of_punc_marks += 1

    return amount_of_punc_marks


def get_all_length(amount_words):
    length = 0
    for word in amount_words:
        length += len(word)
    return length


def average_word_length(amount_words):
    return get_all_length(amount_words) / len(amount_words)


def print_dict(
    dictionary: dict, start_index: int, end_index: int, indent: str = ""
) -> None:
    for key, value in dictionary.items():
        if start_index > end_index:
            break
        start_index += 1
        print(f"{indent}{key} - {value}")


def get_clear_text(clear_words):
    return " ".join(clear_words)


def write_to_file(dict):
    with open("output.txt", "w") as outfile:
        for key, value in dict.items():
            outfile.write(f"{key} - {value}\n")


def normalize_words(morph, words):
    list_of_nomalized_words = []
    for word in words:
        p = morph.parse(word)[0]
        list_of_nomalized_words.append(p.normal_form)
    return list_of_nomalized_words


def print_word_parse(morph, dict, start, end):
    for key, value in dict.items():
        if start > end:
            break
        start += 1
        p = morph.parse(key)[0]
        print(f"Слово: {key}\nЧасть речи: {p.tag.POS}\nОдушевленность: {p.tag.animacy}")


def print_statistic(text):
    dirty_words = get_words(text)
    amount_words = clear_words(dirty_words)
    print("Статистика по тексту:")
    print(f"\tКоличество символов в тексте: {len(get_clear_text(amount_words))}")
    print(f"\tКоличество слов в тексте: {len(amount_words)}")
    print(
        f"\tСредняя длина слова составляет {round(average_word_length(amount_words), 2)} символов"
    )
    print(f"\tКоличество предложений в тексте: {get_number_of_sentences(text)}")
    print(
        f"\tСредняя длина предложения составляет {round(average_sentence_length(text),2)} символов"
    )
    print(f"\tКоличество знаков препинания: {get_number_of_punctuation_marks(text)}")
    freq_dict = create_freq_dict(amount_words)
    sorted_freq_dict = sort_dict_by_value(freq_dict, True)
    print(f"\tСамые частотные слова:")
    print_dict(sorted_freq_dict, 0, 10, "\t\t")


def main():
    morph = pymorphy2.MorphAnalyzer()
    text = read_text("text_sem9.txt")
    print_statistic(text)
    dirty_words = get_words(text)
    amount_words = clear_words(dirty_words)
    freq_dict = create_freq_dict(amount_words)
    sorted_dict = sort_dict_by_value(freq_dict, False)
    write_to_file(sorted_dict)
    nomalized_words = normalize_words(morph, amount_words)
    print("Статистика по нормализованному тексту:")
    print(f"\tКоличество слов в тексте: {len(nomalized_words)}")
    print(
        f"\tСредняя длина слова составляет {round(average_word_length(nomalized_words), 2)} символов"
    )
    freq_dict = create_freq_dict(nomalized_words)
    sorted_freq_dict = sort_dict_by_value(freq_dict, True)
    print(f"\tСамые частотные слова:")
    print_dict(sorted_freq_dict, 0, 10, "\t\t")
    print_word_parse(morph, sorted_freq_dict, 0, 10)


if __name__ == "__main__":
    main()
