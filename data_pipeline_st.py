def preprocessed_data(dict_order):
    
    """ 
    Функция предобработки входного словаря для подачи в модель. На вход получаем полный набор спецификаций. Далее
    разделяем его на словарь для подачи в модель и словарь, который будет добавлен к предсказанию модели для 
    расчёта косинусного сходства. В этих словарях мы заменим названия полей заказов на аналогичные поля из описания фабрик.
    Далее преобразуем словари в строки для подачи на предсказание модели.
    """
    
    import re
    columns1 = ["Вид изделия", "Тип одежды", "Назначение", "По полу и возрасту","Сезон", "Ценовой сегмент", 
                "Заказчик предоставит", "Конструирование", "Виды нанесения",
                "Дополнительные услуги","Требования к оборудованию"]
    columns2 = ["Регионы производства", "Образец", "Пробная партия", "Плановый бюджет", "Требование к штату",
                "Обеспечение сырьем", "Условия оплаты","Дополнительные услуги","Сертификация", 
                "Наличие в реестре Минпромторга","Комментарий к заказу"]
    input_dict = {key: dict_order[key] for key in columns1 if key in dict_order}
    add_dict = {key: dict_order[key] for key in columns2 if key in dict_order}
    
    new_columns1 = ["Вид изделий", "Тип одежды", "Сфера применения", "По полу/возрасту","По сезону", "Ценовые сегменты", 
                    "Заказчик должен предоставить","Конструирование", "Нанесение","Дополнительные услуги", "Оборудование"]
    new_columns2 = ["Регион производства", "Пошив образцов", "Минимальная партия","Минимальная сумма заказа","Штат",
                    "Сырье","Условия оплаты","Дополнительные услуги","Сертификация","Наличие в реестре Минпромторга", 
                    "Комментарий к заказу"]
    def newdict(dict_order, columns, new_columns):
        if len(columns) != len(new_columns):
            raise ValueError("Списки старых и новых ключей должны быть одинаковой длины.")
        mapping = dict(zip(columns, new_columns))
        new_dict = {mapping.get(key, key): value for key, value in dict_order.items()}
        return new_dict

    def dict_to_string(input_dict):
        import re
        def re_sub_string(item):
            item = re.sub(r"http[s]?://S+", " ", item)  # заменяем URL-ссылки
            item = re.sub(r'[.,;:?!"()%/]', " ", item)  # заменяем знаки препинания
            item = re.sub(r"bd+b", " ", item)  # убираем отдельно стоящие цифры
            item = re.sub(r's+', ' ', item).strip()  # удаляем лишние пробелы
            return item  # возвращаем результат
        list_of_tuples = list(input_dict.items())
        # Применяем функцию к каждой записи словаря и создаем список
        cleaned_items = [f"{re_sub_string(str(key))} {re_sub_string(str(value))}" for key, value in list_of_tuples]

    
        # Объединяем все элементы в одну строку
        result_string = ' '.join(cleaned_items)
        return result_string.lower()    
        
   
    new_input_dict = newdict(input_dict, columns1, new_columns1)
    new_add_dict = newdict(add_dict, columns2, new_columns2)
    input_text = dict_to_string(new_input_dict)
    add_text = dict_to_string(new_add_dict)
    return input_text, add_text

if __name__ == '__main__':
    dict_order = {"Вид изделия": "Одежда", 
                "Тип одежды": "Трикотажная одежда, Домашняя одежда",
                "Назначение": "Повседневная одежда",
                "По полу и возрасту": "Женская одежда",
                "Сезон": "Всесезон",
                "Ценовой сегмент": "Средний, Средний Плюс", 
                "Заказчик предоставит": "Лекала, Фото изделия",
                "Конструирование": "Требуется разработка лекал",
                "Виды нанесения": "Бирка, Штамп",
                "Требования к оборудованию": "Пуговичная машина с приспособлением для пуговиц на ножке",
                "Комментарий к заказу": "Просим изготовить домашние костюмы для женщин от 50 лет и старше. Размерный ряд от 48 до 60",
                "Регионы производства": "ЦФО", "Образец":"Да", "Пробная партия":"50 единиц",
                "Плановый бюджет":"350000",
                "Наличие в реестре Минпромторга": "Да", 
                "Требование к штату":"Не менее 8 человек в бригаде. Технолог швейного производства в штате",
                "Упаковка":"Лейблы и бирки",
                "Условия оплаты":"Аванс 50%",
                "Дополнительные услуги": "ВТО, упаковка",
                "Сертификация":"Обычная одежда, не требует обязательной сертификации",
                "Обеспечение сырьем":"Закупает фабрика"
                }
    input_data, add_data = preprocessed_data(dict_order)
    print(input_data)
    print(add_data)

import gdown
def _get_file_from_google_drive(url:str, name = None ) -> str:  #скрипт скачивает файл из google drive и возвращает путь к скачанному файлу (str)
    # Извлечение идентификатора файла из ссылки
    file_id = url.split('/')[-2]
    # Загрузка файла из Google Drive в Google Colab
    output_file = gdown.download(f"https://drive.google.com/uc?id={file_id}", output=name, quiet=True)
    # возвращает путь к файлу
    return f'/content/{output_file}


def run_neural_network(input_data, add_data,topon = 10) #model = 'model_best_120_23_05.keras', 
                    #tokenizer = 'tokenizer_final.pickle', max_length=162, 
                    #table_for_predict = 'fabrics_st.xlsx', ):
    """ Функция обрабатывает запрос и выдаёт перечень фабрик наиболее релевантных под указанные спецификации.
    Расчёт идет на основе модели encoder-decoder, а также с использованием функции косинусного расстояни
    """
    
    tokenizer = _get_file_from_google_drive('https://drive.google.com/file/d/16XqQof5tYbUJad536Bc6w98qk9H77Vu5/view?usp=drive_link')
    model = _get_file_from_google_drive('https://drive.google.com/file/d/1IvPghE7fEedX42mBxJAuhzPCDtYeNW7k/view?usp=drive_link')
    table_for_predict = _get_file_from_google_drive('https://docs.google.com/spreadsheets/d/16yIeT5l_ETUrt0VW5JAzBbED852MPKs-/edit?usp=sharing&ouid=101638033870317209731&rtpof=true&sd=true')

    import numpy as np
    import pandas as pd
    import pickle
    from keras.models import load_model
    from keras.preprocessing.sequence import pad_sequences
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
            
    with open(tokenizer, 'rb') as handle:
        tokenizer = pickle.load(handle)
            
    
    model = load_model(model)
    
    def strToTokens(sentence, tokenizer, max_length):
        words = sentence.lower().split()  # приводит предложение к нижнему регистру и разбирает на слова
        tokensList = []
    
        for word in words:  # для каждого слова в предложении
            # проверяем наличие слова в словаре токенизатора
            if word in tokenizer.word_index:
                tokensList.append(tokenizer.word_index[word])

        return pad_sequences([tokensList], maxlen=max_length, padding='post')
        
        
    def generate_sequence(model, tokenizer, seed_text, max_length = max_length):
        import numpy as np
        from keras.preprocessing.sequence import pad_sequences

        # Начальное состояние для ввода в декодер
        encoder_input = pad_sequences(tokenizer.texts_to_sequences([seed_text]), maxlen=max_length, truncating='pre')
        # начальный ввод в декодер - символ начала предложения, например "<start>"
        decoder_input = np.zeros(shape=(len(encoder_input), max_length))
        decoder_input[:,0] = tokenizer.word_index['start']  # предполагается, что у вас есть токен начала последовательности в tokenizer

        for i in range(1, max_length):
            predictions = model.predict([encoder_input, decoder_input]).argmax(axis=-1)
            decoder_input[:,i] = predictions[:,i-1]
            if tokenizer.word_index['end'] in predictions[:,i-1]:
                break

        decoded_sequence = ' '.join([tokenizer.index_word[token] for token in decoder_input[0] if token > 0])
        return decoded_sequence
    
    input_seq = strToTokens(input_data, tokenizer, max_length)
    generated_sequence = generate_sequence(model, tokenizer, input_data, max_length)
    
    joined_order = generated_sequence[6:-3] + ' ' + add_data
    
    fabrics = pd.read_excel(table_for_predict, header=0)
    text = fabrics['Описание фабрики'].values
    ID = fabrics['ID Фабрики'].values
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
    df = pd.DataFrame({'ID Фабрики': ID,'Описание фабрики': text})
   
    find_nearest_to = joined_order
    print('---'*40)
    tfidf = TfidfVectorizer()
    mx_tf = tfidf.fit_transform(text)
    new_entry = tfidf.transform([find_nearest_to])

    cosine_similarities = linear_kernel(new_entry,mx_tf).flatten()
    df['cosine_similarities'] = cosine_similarities
    df = df.sort_values(by=['cosine_similarities'], ascending=[False]).reset_index()
    df['Степень соответствия с запросом'] = df['cosine_similarities'].apply(lambda x: f"{x*100:.2f}%")
    
    #def row_to_dict(df, i):
        #return df.iloc[i].to_dict()

    #def print_dict_columnwise(a_dict):
        #for key, value in a_dict.items():
            #print(f"{key}: {value}, Степень подобия {round(row['cosine_similarities'],2)}")
    #for index, row in df.head(topon).iterrows():
        #row_dictionary = row_to_dict(fabrics, index)
        #print('---'*40)
        #print_dict_columnwise(row_dictionary)
        
    result = df[['ID Фабрики','Описание фабрики','Степень соответствия с запросом']].head(topon).to_dict(orient='records')
    
    return result

if __name__ == '__main__':
    input_text = 'вид изделий одежда тип одежды трикотажная одежда  домашняя одежда сфера применения повседневная одежда по полу возрасту женская одежда по сезону всесезон ценовые сегменты средний  средний плюс заказчик должен предоставить лекала  фото изделия конструирование требуется разработка лекал нанесение бирка  штамп дополнительные услуги вто  упаковка оборудование пуговичная машина с приспособлением для пуговиц на ножке'
    add_text = 'регион производства цфо пошив образцов да минимальная партия 50 единиц минимальная сумма заказа 350000 штат не менее 8 человек в бригаде  технолог швейного производства в штате сырье закупает фабрика условия оплаты аванс 50 дополнительные услуги вто  упаковка сертификация обычная одежда  не требует обязательной сертификации наличие в реестре минпромторга да комментарий к заказу просим изготовить домашние костюмы для женщин от 50 лет и старше  размерный ряд от 48 до 60'
    run_neural_network(input_text, add_text)    






