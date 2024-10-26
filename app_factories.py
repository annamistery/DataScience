# -*- coding: utf-8 -*-
"""app_factories.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d7_jbwOrhMWg3PcvP0OE16kFwYM4U2dU
"""

import subprocess

subprocess.run(["pip", "install", "-r", "https://raw.githubusercontent.com/annamistery/DataScience/main/requirements.txt"])



import streamlit as st
import pandas as pd
# Title
#st.markdown('Добро пожаловать на платформу LEGPROM!')
st.title("Добро пожаловать на платформу LEGPROM!!!")
st.header("Приложение по подбору фабрик")

image_url = 'https://github.com/annamistery/DataScience/blob/main/image_legprom.jpg'

# Display the image using the URL
st.image(image_url, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.subheader("Введите необходимые спецификации вашего заказа")

# Selection fields
vid_izdeliya = st.selectbox("Выберите вид изделия: ", [
    "Одежда",
    "Аксессуары",
    "Текстиль для дома и бизнеса",
    "Обувь",
    "Сумки",
    "Одежда и текстиль для животных",
    "Мягкие игрушки"
    ])

tip_odezhdy = st.multiselect("Выберите тип одежды: ", [
    "Верхняя демисезонная одежда",
    "Легкая одежда",
    "Верхняя зимняя одежда",
    "Трикотажная одежда",
    "Домашняя одежда",
    "Головные уборы",
    "Платочно шарфовые изделия",
    "Вязаная одежда",
    "Нательное белье",
    "Головные уборы",
    "Чулочно носочные изделия"
])
naznachenie = st.multiselect("Выберите назначение: ", [
    "Рабочая одежда",
    "Униформа для сферы услуг и торговли",
    "Пищевое производство",
    "Охранные предприятия",
    "Медицинская одежда",
    "Одежда специального назначения и СИЗ",
    "Повседневная городская одежда",
    "Пищевое производство",
    "Спортивная одежда",
    "Офисная деловая одежда",
    "Охота рыбалка туризм",
    "Фирменная одежда мерч промо",
    "Образовательные учреждения",
    "Форменная одежда обмундирование",
    "Униформа для HoReCa",
    "Образовательные учреждения",
    "Национальная одежда",
    "Рекламная индустрия",
    "Торжественная одежда"

])
pol_i_vozrast = st.multiselect ("Выберите пол и возраст: ", [
    "Большие размеры",
    "Детская одежда",
    "Для беременных",
    "Для новорожденных",
    "Женская одежда",
    "Мужская одежда",
    "Подростковая одежда",
    "Унисекс"

])

sezon = st.selectbox ("Выберите сезон: ", ['Всесезон', 'Весна/Осень', 'Зима', 'Лето'
                                        ])

cenovoi_segment = st.multiselect ("Выберите ценовой сегмент: ", [
    'Средний', 'Средний Плюс', 'Эконом', 'Премиум'
])

zakazchik_predostavit = st.multiselect ("Заказчик предоставит:", [
    "Фото рисунок изделия в любом виде",
    "Технический рисунок",
    "Технологическое описание со схемами узлов",
    "Полное ТУ изделия или ГОСТ",
    "Лекала баз  размера в бумажном варианте",
    "Лекала на все размеры в бумажном варианте",
    "Лекала в эл  виде в формате  aama",
    "Раскладки Спецификация применяемых материалов",
    "Табель мер Полный комплект материалов и фурнитур",
    "Образец изделий",
    "Требования к таре упаковке",
    "Технический рисунок",
    "Фото рисунок изделия в любом виде",
    "Требования к таре упаковке",
    "Технологическое описание со схемами узлов",
    "Лекала на все размеры в бумажном варианте",
    "Полный комплект материалов и фурнитуры",
    "Образец изделий",
    "Лекала на все размеры в бумажном варианте",
    "Лекала в эл.виде в формате aama",
    "Раскладки",
    "Спецификация применяемых материалов",
    "Образец изделий",
    "Спецификация применяемых материалов",
    "Табель мер",
    "Полный комплект материалов и фурнитуры",
    "Образец изделий",
    "Технологическое описание со схемами узлов",
    "Лекала баз  размера в бумажном варианте",
    "Лекала на все размеры в бумажном варианте",
    "Образец изделий Требования к таре упаковке"
])

konstruirovanie = st.multiselect ("Конструирование: ", [
    "Изготовление и спецификация комплекта градированных лекал",
    "Конструирование комплекта рабочих лекал базового размера без макета",
    "Конструирование комплекта рабочих лекал базового размера с макетом",
    "Подготовка раскладки лекал для массового производства",
    "Спецификация прикладных материалов и фурнитуры по размерам ростам",
    "Табель мер",
    "Печать лекал на плоттере",
    "Оцифровка ручных лекал",
    "Печать лекал на плоттере",
    "Печать раскладок на плоттере",
    "Подготовка раскладки лекал для массового производства",
    "Изготовление и спецификация комплекта градированных лекал",
    "Разработка ТУ",
    "Отрисовка технического рисунка",
    "Разработка конфекционной карты"
])

vidy_naneseniya = st.multiselect ("Выберите виды нанесения:", [
    'Вышивка', 'Шелкография', 'Лента', 'Бирка', 'Штамп', 'Рисунки и печать',
    'Тиснение', 'ДТФ', 'Шелкография', 'Шевроны'
])

trebovaniya_k_oborudovaniyu = st.multiselect ("Выберите требования к оборудованию:", [
    'Станки для проклеивания швов', 'Раскройный комплекс', 'Пятинитка', 'Петельная машина с прямой петлёй',
    'Пуговичная машина с приспособлением для пуговиц на ножке', 'Закрепочная машинка',
    'Двухиголка', 'Автоматический обрез липучки', 'Машинка для венгерки', 'Четырехниточный оверлок',
    'Распошивалка', 'Прямострочка', 'Прямая петля', 'Пуговичная машина', 'Вышивальная машина','Вязальная машина', 'Флэтлог'
])

regiony_proizvodstva = st.multiselect ("Выберите регионы производства:", [
'Москва и МО ',
"Ивановская область",
"Санкт-Петербург и ЛО",
"Новосибирская область",
"Краснодарский край",
"Нижегородская область",
"Алтайский край",
"Кировская область",
"Липецкая область",
"Пермский край",
"Ростовская область",
"Саратовская область",
"Республика Марий Эл",
"Омская область",
"Пензенская область",
"Свердловская область",
"Самарская область",
"Волгоградская область",
"Тульская область",
"Красноярский край",
"Воронежская область",
"Республика Башкортостан",
"Республика Татарстан",
"Орловская область",
"Кемеровская область",
"Иркутская область",
"Оренбургская область",
"Республика Чувашия",
"Владимирская область",
"Ярославская область",
"Республика Коми",
"Республика Удмуртия",
"Брянская область",
"Астраханская область",
"Тамбовская область",
"Кыргызстан",
"Курская область",
"Костромская область",
"Челябинская область",
"Смоленская область",
"Приморский край",
"Псковская область",
"Ставропольский край",
"Республика Бурятия",
"Калининградская область",
"Республика Крым и Севастополь",
"Новгородская область",
"Тюменская область",
"Рязанская область",
"Курганская область",
"Республика Мордовия",
"Еврейская автономная область",
"Томская область",
"Узбекистан",
"Белгородская область",
"Республика Карелия",
"Ульяновская область"

])
budjet = st.selectbox ("Укажите минимальный бюджет:", ["50000",
"100000",
"30000",
"20000",
"15000",
"10000",
"150000",
"200000",
"125000",
"3000",
"5000",
"1000000",
"300000"])

dopuslugi = st.multiselect ("Дополнительные услуги:",["Подбор материалов", "Подбор расцветки", "ВТО", "Честный знак", "Подбор поставщика",
            "Подбор ткани", "ОТК", "Маркировка", "Ремонт одежды", "Аренда одежды", "Сертификация"])

sertificaciya = st.selectbox("Сертификация:", ["Обычная одежда, не требует обязательной сертификации",
"Спецодежда и СИЗ, требующие обязательную сертификацию"])

upakovka = st.selectbox ("Требуется ли упаковка:", ['Да', 'Нет'])

obrazec = st.selectbox ("Требуется ли отшить образцы:", ['Да', 'Нет'])

probnaya_partiya = st.selectbox("Пробная партия. Укажите количество единиц товара:", ["1", "5", "300",
"500",
"20",
"50",
"250",
"3000",
"30",
"180",
"150",
"10-15",
"от 10",
"1000",
"от 500",
"350",
"100 ед. на давальческом сырье",
"от 300 ед. своей тканью",
"Футболки 50 шт, худи/свитшот 40 шт, банданы 50 шт, плательная группа 10 шт., шопер 10 шт"
])

oplata = st.multiselect("Условия оплаты:", ["100% предоплата", "Аванс 30%", "Аванс 50%", "Аванс 70%",
                                        "Безналичная оплата", "Счёт без НДС",'Счет с НДС',
                                        "Наличная оплата", "По факту получения 100%",
                                        'Отсрочка платежа до 10 дней', 'Отсрочка платежа до 30 дней',
                                        "Отсрочка платежа до 60 дней"
                                        ])


nalichie_v_reestre = st.multiselect ("Наличие в реестре Минпромторга:", ['Да', 'Нет'])

shtat = st.selectbox("Укажите требования к штату:",
    ["Конструктор на аутсорсинге 10 швей",
    "Конструктор на аутсорсе 30 швей",
    "Конструктор в штате 50 швей",
    "Конструктор в штате 5 швей"
    ])


syrie = st.selectbox("Обеспечение сырьем:", ['Давальческое', 'Закупает фабрика', 'Частично давальческое/фабрики'])

komentariy = st.text_area("Комментарий к заказу:")
# Other specifications that user might have to fill
# For example, material, quantity, sizes etc. can be added here similarly
# ...
# A button to confirm the order
#if st.button('Собрать заказ'):
order_details = {
        "Вид изделия": vid_izdeliya if vid_izdeliya else "",
        "Тип одежды": ', '.join(tip_odezhdy) if tip_odezhdy else "", # check if any type is selected
        "Назначение": ', '.join(naznachenie) if naznachenie else "",
        "По полу и возрасту": ', '.join(pol_i_vozrast) if pol_i_vozrast else "",
        "Сезон": sezon if sezon else "",
        "Ценовой сегмент": ', '.join(cenovoi_segment) if cenovoi_segment else "",
        "Виды нанесения": ', '.join(vidy_naneseniya) if vidy_naneseniya else "",
        "Заказчик предоставит": ', '.join(zakazchik_predostavit) if zakazchik_predostavit else "",
        "Конструирование": ', '.join(konstruirovanie) if konstruirovanie else "",
        "Требования к оборудованию": ', '.join(trebovaniya_k_oborudovaniyu) if trebovaniya_k_oborudovaniyu else "",
        "Регионы производства": ', '.join(regiony_proizvodstva) if regiony_proizvodstva else "",
        "Плановый бюджет": budjet if budjet else "",
        "Дополнительные услуги": ', '.join(dopuslugi) if dopuslugi else "",
        "Сертификация": sertificaciya if sertificaciya else "",
        "Упаковка": upakovka if upakovka else "",
        "Образец": obrazec if obrazec else "",
        "Пробная партия":  probnaya_partiya if probnaya_partiya else "",
        "Условия оплаты":', '.join (oplata) if oplata else "",
        "Наличие в реестре Минпромторга":  ', '.join(nalichie_v_reestre) if nalichie_v_reestre else "",
        "Требование к штату": shtat if shtat else "",
        "Обеспечение сырьем": syrie if syrie else "",
        "Комментарий к заказу": komentariy if komentariy else ""}

st.session_state['order_details'] = order_details
#if 'order_details' in st.session_state:
    #st.write("Содержимое order_details:")
    #st.write(st.session_state['order_details'])

    #st.write("Ваш заказ:")
#for key, value in order_details.items():
    #st.write(f"{key}: {value}")
# Ниже вашего кода, на верхнем уровне (без отступов) должен находиться импорт
from data_pipeline_st import preprocessed_data, run_neural_network
def display_fabric_table(df_predictions):
    result_df = pd.DataFrame(df_predictions)
    # Предполагаем, что в df_predictions уже есть все нужные столбцы, включая 'Степень соответствия'
    st.table(result_df)

if st.button('Обработать данные'):
    if 'order_details' in st.session_state:
        # Используем сохраненные данные для обработки
        result_input, result_add = preprocessed_data(st.session_state['order_details'])

        #st.write("Результат предобработки для входа в модель:", result_input, result_add)

        # Перед вызовом модели
        #st.write (f"Входные данные для модели: {result_input}")

        #st.write (f"Входные данные для добавления к выходному результату: {result_add}")
        # Выполняем обработку данных и получение предсказания модели
        prediction = run_neural_network(result_input, result_add)

        # Сохраняем результаты предсказания для использования в дальнейшем
        st.session_state['prediction'] = prediction

        # Выводим результат обработки данных и результат предсказания в виде таблицы
        st.write("Результат обработки данных:")

        # Выводим данные в Streamlit
        st.table(prediction)


        #display_fabric_table(prediction)  # Передаем прямо список словарей
    else:
        # Выводим предупреждение, что заказ еще не подтвержден
        st.warning("Пожалуйста, сначала подтвердите детали заказа.")



    # Теперь словарь order_details можно использовать для дальнейших действий, например, для отправки в модель.