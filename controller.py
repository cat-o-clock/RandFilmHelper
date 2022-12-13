import textwrap
from pilmoji import Pilmoji
import kg_top100
import random
import streamlit as st
from streamlit_agraph import agraph, Config, Node
from PIL import Image, ImageDraw, ImageFont
import urllib.request

ans = []
output_n = Node(id='temp', image = "", link = "")

# фото-отзыв
def get_post(name, smile, review):
    st.balloons()

    #logo
    new_img = Image.new('RGB', (1080, 1920), '#fffafa')
    logo = Image.open("logo.png")
    logo = logo.resize((logo.width // 2, logo.height // 2))
    new_img.paste(logo,(330,5),logo)
    #title
    font = ImageFont.truetype("arial.ttf", size =36)
    pencil = ImageDraw.Draw(new_img)
    pencil.text((50, 150), str(get_title()), font=font, fill='black')
    #poster
    print(get_image())
    urllib.request.urlretrieve(get_image(),"poster.png")
    poster = Image.open("poster.png")
    #poster = Image.open(requests.get(get_image(), stream=True).raw)
    poster = poster.resize((290,420))
    new_img.paste(poster, (50,200))

    #краткое описание
    font_18 = ImageFont.truetype("arial.ttf", size=18)
    place = str("Место в рейтинге: " + get_place())
    pencil.text((350,200), place, font=font_18, fill='black')
    year = str("Год выпуска: " + get_year())
    pencil.text((350, 220), year, font=font_18, fill='black')
    country = str("Страна: " + get_country())
    pencil.text((350, 240), country, font=font_18, fill='black')
    duration = str("Продолжительность: " + get_duration())
    pencil.text((350, 260), duration, font=font_18, fill='black')
    language = str("Оригинальный язык: " + get_language())
    pencil.text((350, 280), language, font=font_18, fill='black')
    genre = str("Жанры: " + ','.join(get_genres()))
    pencil.text((350, 300), genre, font=font_18, fill='black')

    #tags and review
    tag = str("Тэги: " + ','.join(get_tags()))
    pencil.rectangle(((350, 320), (1050, 350)), fill="#FFC7C7")
    pencil.text((350, 320), tag, font=font_18, fill='black')

    reviews = str(get_text())
    textwrapped = textwrap.wrap(reviews, width=75)
    pencil.text((350, 360), '\n'.join(textwrapped), font=font_18, fill="black")

    #отзыв
    with Pilmoji(new_img) as pilmoji:
        pilmoji.text((450, 700), str(name + " " + smile), font=font, fill='black')

    text = textwrap.wrap(review, width=75)
    font_24 = ImageFont.truetype("arial.ttf", size=24)
    pencil.text((50, 750), '\n'.join(text), font=font_24, fill='black')

    st.image(new_img, width=500)

# Выбор конкретного фильма из списка подходящих по критерии
def output_node(tags_checkbox,tags):
    global output_n
    kol = len(ans)
    if kol==0:
        output_n = kg_top100.kg_nodes_film[0]
    else:
        if (tags_checkbox) and (tags!=[]):
            output_n = ans[0]
        else:
            output_n = ans[random.randint(0,kol-1)]
    #agraph(nodes=[output_n],edges=[],config=Config())


# Поиск списка подходящих фильмов.
def answer(year_of_issue_checkbox,year_of_issue,duration_checkbox, duration,country_checkbox, country,
           language_checkbox, language, type_checkbox, type, place_checkbox, place, genre_checkbox, genre, tags_checkbox, tags):
    global ans
    ans = []
    a = []

    for i in kg_top100.kg_nodes_film:
        ans.append(i)

    if year_of_issue_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_year_of_issue:
                if (i.label == j.source) and (int(year_of_issue[0])<=int(j.to)) and (int(year_of_issue[1])>=int(j.to)):
                   a.append(i)
        ans = a
        a = []


    if duration_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_duration:
                if (i.label == j.source) and (int(duration[0]) <= int(j.to)) and (int(duration[1]) >= int(j.to)):
                    a.append(i)
        ans = a
        a = []

    if country_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_country:
                if (i.label == j.source) and (str(country) == str(j.to)):
                    a.append(i)
        ans = a
        a = []

    if language_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_original_language:
                if (i.label == j.source) and (str(language) == str(j.to)):
                    a.append(i)
        ans = a
        a = []

    if type_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_type:
                if (i.label == j.source) and (str(type) == str(j.to)):
                    a.append(i)
        ans = a
        a = []

    if place_checkbox:
        for i in ans:
            for j in kg_top100.kg_edges_place:
                if (i.label == j.source) and (int(place[0]) <= int(j.to)) and (int(place[1]) >= int(j.to)):
                #if (i.label == j.source) and (str(place) == str(j.to)):
                    a.append(i)
        ans = a
        a = []

    if (genre_checkbox) and (genre != []):
        for i in ans:
            for j in kg_top100.kg_edges_genre:
                if (i.label == j.source) and (j.to in genre):
                    a.append(i)
        b = a
        a = []
        for i in b:
            if i not in a:
                a.append(i)
        ans = a
        a = []

    if (tags_checkbox) and (tags != []):
       for i in ans:
           ii = ""
           for j in kg_top100.kg_edges_tag:
               if (i.label == j.source): ii = j.to
           for j in kg_top100.kg_edges_tags:
               if (ii == j.source) and (j.to in tags):
                   a.append(i)
       b = sorted(a,key=lambda x:a.count(x))
       a = []
       for i in b:
           if i not in a:
               a.append(i)

       ans = a
       a = []

    #agraph(nodes=ans,edges=[],config=Config())
    output_node(tags_checkbox,tags)


#Вывод полей.
def get_image():
    image = output_n.__dict__["image"]
    return image

def get_title():
    title = output_n.label
    return title

def get_tags():
    tags = []
    for i in kg_top100.kg_edges_tag:
        if (i.source == output_n.label):
            ii = i.to
            for j in kg_top100.kg_edges_tags:
                if (ii == j.source):
                    tags.append(j.to)
    return tags

def get_genres():
    genres = []
    for i in kg_top100.kg_edges_genre:
        if (i.source == output_n.label):
            genres.append(i.to)
    return genres

def get_link():
    link = output_n.__dict__["link"]
    return link

def get_duration():
    for i in kg_top100.kg_edges_duration:
        if (i.source == output_n.label):
            duration = i.to
            return duration

def get_year():
    for i in kg_top100.kg_edges_year_of_issue:
        if (i.source == output_n.label):
            year = i.to
            return year

def get_country():
    for i in kg_top100.kg_edges_country:
        if (i.source == output_n.label):
            country = i.to
            return country

def get_language():
    for i in kg_top100.kg_edges_original_language:
        if (i.source == output_n.label):
            language = i.to
            return language

def get_place():
    for i in kg_top100.kg_edges_place:
        if (i.source == output_n.label):
            place = i.to
            return place

def get_text():
    text = output_n.title
    return text

# Вывод графа.
def graph_answer():
    graph = []
    graphe = []

    for i in kg_top100.kg_edges:
        if i.source == output_n.label:
            graphe.append(i)
            for j in kg_top100.kg_nodes:
                if (j.label == i.to) or (j.label == i.source):
                    graph.append(j)

    for i in kg_top100.kg_edges_tag:
        if (i.source == output_n.label):
            ii = i.to
            graphe.append(i)
            for j in kg_top100.kg_nodes_tag:
                if (j.title == ii):
                    graph.append(j)


            for j in kg_top100.kg_edges_tags:
                if (ii == j.source):
                    graphe.append(j)
                    for x in kg_top100.kg_nodes_tags:
                        if x.label == j.to:
                            graph.append(x)


    graph = set(graph)
    graphe = set(graphe)

    config = Config(width=500, height=300)
    agraph(nodes=graph, edges=graphe, config=config)