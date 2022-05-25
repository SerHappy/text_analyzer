import re
import pymorphy2
import nltk


def read_text(filename: str) -> str:
    """Читает текст из файла filename и возвращает строку с предложениями"""
    text = ""
    with open(filename, encoding="utf-8") as infile:
        for line in infile:
            if line.strip() != "":
                text += line.strip() + " "
    return text


def delete_punc_marks_and_artif(text: str) -> list:
    """Удаляет знаки препинания и артефакты из списка слов. Возвращает преобразованный список"""
    chars = '.,;:!«»?—()–-"_/©'
    for i in chars:
        text = text.replace(i, " ")
    return text.split()


def delete_stopwords(list_of_words: list) -> list:
    """Удаляет стоп слова из списка слов. Возвращает преобразованный список"""
    stopwords = [
        "джордж",
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


def get_words(text: str) -> list:
    """Возвращает список слов из строки text"""
    temp_list = delete_punc_marks_and_artif(text)
    lower_temp_list = list((map(lambda x: x.lower(), temp_list)))
    return delete_stopwords(lower_temp_list)


def create_freq_dict(list_of_words: list) -> dict:
    """Возвращает словарь, в котором ключ - слово, а значение - кол-во его повторений."""
    dictionary = {}
    for word in list_of_words:
        dictionary[word] = dictionary.setdefault(word, 0) + 1
    return dictionary


def sort_dict_by_value(dictionary: dict, reversed_order: bool) -> dict:
    """Сортирует словарь либо по возростанию, либо по убыванию. Возвращает отсортированный словарь"""
    return dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=reversed_order)
    )


def get_sentences(text: str) -> list:
    """Возвращает список предложений"""
    return re.split(r' *[\.\?!][\'"\)\]]* *', text)


def get_sentences_with_nltk(text: str) -> list:
    """Возвращает список предложений с помощью библиотеки nltk"""
    return nltk.tokenize.sent_tokenize(text)


def total_sentence_length(text: str) -> int:
    """Возвращает общую длину всех предложений"""
    list_of_sentences = get_sentences_with_nltk(text)
    length = 0
    for sentence in list_of_sentences:
        length += len(sentence)
    return length


def average_sentence_length(text: str) -> float:
    """Возвращает среднюю длину предложения"""
    return total_sentence_length(text) / len(get_sentences_with_nltk(text))


def get_number_of_punctuation_marks(text: str) -> int:
    """Возвращает количество знаков препинания в text"""
    punctuation_marks = ".,;:!«»?—()-\"'"
    amount_of_punc_marks = 0
    for i in text:
        if i in punctuation_marks:
            amount_of_punc_marks += 1
    return amount_of_punc_marks


def total_word_length(list_of_words: list) -> int:
    """Возвращает общую длину всех слов"""
    length = 0
    for word in list_of_words:
        length += len(word)
    return length


def average_word_length(list_of_words: list) -> float:
    """Возвращает среднюю длину слова"""
    return total_word_length(list_of_words) / len(list_of_words)


def print_dict(
    dictionary: dict, start_index: int, end_index: int, indent: str = ""
) -> None:
    """Выводит в консоль пары ключ:значение из словаря dict с индекса start_index до end_index. Принимает необязательный параметр отступ indent"""
    for key, value in dictionary.items():
        if start_index > end_index:
            break
        start_index += 1
        print(f"{indent}{key} - {value}")


def concatenate_words(list_of_words: list) -> str:
    """Возвращает строку, состоящюю из list_of_words, разделенных пробелами"""
    return " ".join(list_of_words)


def write_to_file(dict: dict, filename: str) -> None:
    """Записывает пары ключ:значение из словаря dict в файл filename"""
    with open(filename, "w") as outfile:
        for key, value in dict.items():
            outfile.write(f"{key} - {value}\n")


def normalize_words(morph: pymorphy2.MorphAnalyzer, list_of_words: list) -> list:
    """Приводит слова list_of_words к нормальному виду. Возвращает список преобразованных слов"""
    list_of_nomalized_words = []
    for word in list_of_words:
        p = morph.parse(word)[0]
        list_of_nomalized_words.append(p.normal_form)
    return list_of_nomalized_words


def print_morph_parsing(
    morph: pymorphy2.MorphAnalyzer,
    dict: dict,
    start_index: int,
    end_index: int,
    intent="",
) -> None:
    """Выводит подробную статистику по словам из словаря dict с индекса start_index до end_index"""
    print(f"\tПодробная статистика по словам с индекса {start_index} по {end_index}:")
    for key, value in dict.items():
        if start_index > end_index:
            break
        start_index += 1
        p = morph.parse(key)[0]
        print(f"{intent}Слово: {key}. Встречается {value} раз/раза")
        print(f"{intent*2}Часть речи: {morph.lat2cyr(p.tag.POS)}")
        if p.tag.animacy is not None:
            print(f"{intent*2}Одушевленность: {morph.lat2cyr(p.tag.animacy)}")
        if p.tag.case is not None:
            print(f"{intent*2}Падеж: {morph.lat2cyr(p.tag.case)}")
        if p.tag.gender is not None:
            print(
                f"{intent*2}Род (мужской, женский, средний): {morph.lat2cyr(p.tag.gender)}"
            )
        if p.tag.number is not None:
            print(
                f"{intent*2}Число (единственное, множественное): {morph.lat2cyr(p.tag.number)}"
            )
        if p.tag.aspect is not None:
            print(
                f"{intent*2}Вид (совершенный или несовершенный): {morph.lat2cyr(p.tag.aspect)}"
            )
        if p.tag.mood is not None:
            print(
                f"{intent*2}tНаклонение (повелительное, изъявительное): {morph.lat2cyr(p.tag.mood)}"
            )
        if p.tag.person is not None:
            print(f"{intent*2}Лицо (1, 2, 3): {morph.lat2cyr(p.tag.person)}")
        if p.tag.tense is not None:
            print(
                f"{intent*2}Время (настоящее, прошедшее, будущее): {morph.lat2cyr(p.tag.tense)}"
            )
        if p.tag.transitivity is not None:
            print(
                f"{intent*2}Переходность (переходный, непереходный): {morph.lat2cyr(p.tag.transitivity)}"
            )
        if p.tag.voice is not None:
            print(
                f"{intent*2}Залог (действительный, страдательный): {morph(p.tag.voice)}"
            )


def print_statistic(text: str) -> None:
    """Выводит общую статистику по тексту"""
    clear_words = get_words(text)
    print("Статистика по тексту:")
    print(
        f"\tКоличество слов в тексте (до преобразования): {len(delete_punc_marks_and_artif(text))}"
    )
    print(
        f"\tКоличество знаков препинания (до преобразования): {get_number_of_punctuation_marks(text)}"
    )
    print(f"\tКоличество символов в тексте: {len(concatenate_words(clear_words))}")
    print(f"\tКоличество слов в тексте: {len(clear_words)}")
    print(
        f"\tСредняя длина слова составляет {round(average_word_length(clear_words), 2)} символов"
    )
    print(f"\tКоличество предложений в тексте: {len(get_sentences(text))}")
    print(
        f"\tСредняя длина предложения составляет {round(average_sentence_length(text), 2)} символов"
    )
    freq_dict = create_freq_dict(clear_words)
    print(f"\tКоличество различных слов в тексте: {len(freq_dict)}")
    print(f"\tСамые частотные слова (топ 10):")
    sorted_freq_dict = sort_dict_by_value(freq_dict, True)
    print_dict(sorted_freq_dict, 0, 10, "\t\t")


def write_freq_words(text: str, filename: str) -> None:
    """Составляет словарь частотности и вызывает функцию для записи статистики в файл filename"""
    clear_words = get_words(text)
    freq_dict = create_freq_dict(clear_words)
    sorted_freq_dict = sort_dict_by_value(freq_dict, True)
    write_to_file(sorted_freq_dict, filename)


def print_morphy_statistic(text: str) -> None:
    """Выводит статистику по нормализованному тексту"""
    morph = pymorphy2.MorphAnalyzer()
    clear_words = get_words(text)
    nomalized_words = normalize_words(morph, clear_words)
    print("Статистика по нормализованному тексту:")
    print(f"\tКоличество слов в тексте: {len(nomalized_words)}")
    print(
        f"\tСредняя длина слова составляет {round(average_word_length(nomalized_words), 2)} символов"
    )
    freq_dict = create_freq_dict(nomalized_words)
    print(f"\tКоличество различных слов в нормализованном тексте: {len(freq_dict)}")
    print(f"\tСамые частотные слова (топ 10):")
    sorted_freq_dict = sort_dict_by_value(freq_dict, True)
    print_dict(sorted_freq_dict, 0, 10, "\t\t")
    print_morph_parsing(morph, sorted_freq_dict, 0, 10, "\t\t")


def main() -> None:
    """Главный метод программы"""
    nltk.download("popular")
    filename = "crime_and_punishment"
    text = read_text(f"texts/{filename}.txt")
    print_statistic(text)
    write_freq_words(text, f"freq/{filename}_freq.txt")
    print_morphy_statistic(text)


if __name__ == "__main__":
    main()
