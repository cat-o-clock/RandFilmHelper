import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_agraph import agraph, Config, Node, Edge

import time
import requests

import kg_top100
import controller

# Основная информация главной страницы
st.set_page_config(
    layout="wide",
    page_icon="🍿",
    page_title="RandFilm challenge app"
    )

about_app = '''Hello everyone 👋, I am Senia, the owner of this cinema. It works on the basis of knowledge graph. In this cinema you can pick up a movie for a cold evening with a cup of hot tea. 
            \\
            Meanwile, take part in my challenge and watch 100 best movies by IMDb. Choose the filters for your perfect movie 🥰 and enjoy it. Share your feedback on social media with #RandFilm!        

            With love, your S.
            '''
cinema_info = "<i>Select options for movie selection:<i>"


# добавление анимации через сервис lottie
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lotte_popcorn = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_CTaizi.json")
lotte_girl = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_bb9bkg1h.json")


# Функции получения списков возможных критериев из графа знаний
def set_country():
    set_country = set()
    for node in kg_top100.kg_nodes_country:
        set_country.add(node.label)
    return sorted(set_country)

def set_lang():
    set_languages = set()
    for node in kg_top100.kg_nodes_original_language:
        set_languages.add(node.label)
    return sorted(set_languages)

def set_genres():
    set_genres = set()
    for node in kg_top100.kg_nodes_genre:
        set_genres.add(node.label)
    return sorted(set_genres)

def set_tags():
    set_tags = set()
    for node in kg_top100.kg_nodes_tags:
        set_tags.add(str(node.label))
    set_tags = sorted(set_tags)
    return set_tags


# Для кнопки в кнопке
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def f():
    st.session_state.button_clicked = False

def callback(year_of_issue_checkbox,year_of_issue,duration_checkbox, duration, country_checkbox, country,
             language_checkbox, language, type_checkbox, type, place_checkbox, place, genre_checkbox, genre, tags_checkbox, tags):

    st.session_state.button_clicked = True
    controller.answer(year_of_issue_checkbox,year_of_issue,duration_checkbox, duration, country_checkbox, country,
                      language_checkbox, language, type_checkbox, type, place_checkbox, place, genre_checkbox, genre, tags_checkbox, tags)


# Колонка с логотипом и информацией о приложении, графом знаний.
col1, col2 = st.columns([3, 7])
with col1:
    st.image("logo.jpg")
    st_lottie(lotte_girl, key='girl', height=300)
    with st.expander("About RandFilm Challenge cinema:", expanded=True):
        st.markdown(about_app, unsafe_allow_html=True)

    #show all knowledge graph
    config = Config(height=500)
    with st.expander("Knowledge graph:", expanded=False):
        return_value = agraph(nodes=kg_top100.kg_nodes, edges=kg_top100.kg_edges, config=config)

# Колонка с выбором критериев
with col2:
    f1 = ""
    f2 = ""
    f3 = ""
    f4 = ""
    f5 = ""
    f6 = ""
    f7 = ""
    f8 = ""
    st.header("Welcome to our lovely cinema!")
    st.markdown(cinema_info, unsafe_allow_html=True)

    year_of_issue_checkbox = st.checkbox('Year of issue', on_change=f)
    if year_of_issue_checkbox:
        year_of_issue = st.slider("Choose year of issue:", 1921, 2022, ((1980), (2000)),on_change=f)
        f1 = year_of_issue
        #st.write("Your choice:", year_of_issue)

    duration_checkbox = st.checkbox('Duration',on_change=f)
    if duration_checkbox:
        duration = st.slider("Choose duration (in minutes)", 60, 300, ((100), (120)),on_change=f)
        f2 = duration
        #st.write("Your choice:", duration)

    country_checkbox = st.checkbox('Country',on_change=f)
    if country_checkbox:
        country = st.selectbox('Choose country', set_country(),on_change=f)
        f3 = country
        #st.write("Your choice:", country)

    language_checkbox = st.checkbox('Language',on_change=f)
    if language_checkbox:
        language = st.selectbox('Choose original language', set_lang(),on_change=f)
        f4 = language
        #st.write("Your choice:", language)

    type_checkbox = st.checkbox('Type',on_change=f)
    if type_checkbox:
        type = st.selectbox('Choose type', ['фильм', 'мультфильм'],on_change=f)
        f5 = type
        #st.write("Your choice:", type)

    place_checkbox = st.checkbox('Place',on_change=f)
    if place_checkbox:
        place = st.slider('Choose place', 1, 100, ((1), (10)), on_change=f)
        #place = st.selectbox('Choose place', range(1, 101),on_change=f)
        f6 = place
        #st.write("Your choice:", place)

    genre_checkbox = st.checkbox('Genre',on_change=f)
    if genre_checkbox:
        genre = st.multiselect('Choose genre', set_genres(),on_change=f)
        f7 = genre
        #st.write("Your choice:", genre)

    tags_checkbox = st.checkbox('Tags/Keywords',on_change=f)
    if tags_checkbox:
        tags = st.multiselect('Choose genre', set_tags(),on_change=f)
        f8 = tags
        #st.write("Your choice:", tags)

    button_get_film = st.button("Get film!",on_click=lambda:callback(year_of_issue_checkbox,f1, duration_checkbox, f2, country_checkbox, f3,
                                                                     language_checkbox, f4, type_checkbox, f5, place_checkbox, f6,
                                                                     genre_checkbox, f7, tags_checkbox, f8))

# Кнопка вывода информации о фильме. И генерации боковой панели с отзывом и графом. button_get_film or
if st.session_state.button_clicked:
    with st.spinner("Generating film..."):
        time.sleep(1)

    st.image("link.png",width=1750)
    a_image = controller.get_image()
    a_title = controller.get_title()
    a_tags = controller.get_tags()
    a_genres = controller.get_genres()
    a_link = controller.get_link()
    a_duration = controller.get_duration()
    a_year = controller.get_year()
    a_country = controller.get_country()
    a_language = controller.get_language()
    a_place = controller.get_place()
    a_text = controller.get_text()


    r1, r2, r3 = st.columns([3,2,5])
    row1, row2 = st.columns([3, 7])
    # Название и постер
    with r2:
        if (a_image != ""):
            st.image(a_image)
    # Основная информация о фильме
    with r3:
        st.subheader(a_title)
        st.write("Место в рейтинге:", a_place)
        st.write("Год выпуска:", a_year)
        st.write("Страна:", a_country)
        st.write("Продолжительность:", a_duration)
        st.write("Оригинальный язык:", a_language)
        st.write(
            " ".join([
                "</div>",
                "Жанр:",
                " ".join([f'{item}' for item in a_genres]),
                "<br>","<br>",
                "</div>"
            ]),
            unsafe_allow_html=True
        )
    # Графа с отзывом
    with r1:
        with st.form(key="form", clear_on_submit=True):
            user_name = st.text_input('What is your name?')
            user_emoji = st.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱', '🤨', '😢', '🥱'])
            user_reviews = st.text_area('Your reviews:',height=280,max_chars=2500)

            if st.form_submit_button('Get my review!'):
                with row1:
                    controller.get_post(user_name,user_emoji,user_reviews)

                # Описание фильма, ключевые слова и видеоплеер
    with row2:
        st.write(a_text)
        st.write(
            " ".join([
                "</div>",
                '''<blockquote style="background-color: #ffc7c7">''',
                "Ключевые слова:",
                " ".join([f'{item},' for item in a_tags]),
                "</blockquote >",
                "</div>"
            ]),
            unsafe_allow_html=True
        )
        if (a_link != ""):
            st.video(a_link)
    # Вывод графа фильма на боковую панель
    with row1:
        controller.graph_answer()

n1,n2,n3 = st.columns([4,2,4])
with n2:
    st.write(" ".join([
            "</div>",
            '''Created by <a href="https://github.com/cat-o-clock">Cat o'clock</a> in 2022''',
            "</div>"
            ]),
    unsafe_allow_html=True
    )