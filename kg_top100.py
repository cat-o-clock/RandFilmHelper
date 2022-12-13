# This KnowledgeGraph consists of the top 100 movies by IMDb.

# Movie ratings are calculated based on the true Bayesian score using the following formula:
# W=(RV+CM)/(V+M), where
# W - final rating;
# V is the number of votes cast for the film;
# M is the minimum number of votes to be included in the rating; M = 25,000;
# R - the average rating of the film (on a ten-point scale);
# C is the average rating among all films.

# DBNodes consists of:
# top 100 film - фильм + постер + краткое описание + cсылка на просмотр
# year_of_issue - год выпуска фильма (1957, 1994, 1974, 1972, 2008)
# duration - продолжительность кинокартины (96, 142, 152, 175, 202)
# country - страна производства (США,)
# original_language - оригинальный язык (английский,)
# genre - жанр (драма, детектив, боевик)
# place - место в рейтинге (1-100)
# type - тип (мультфильм/фильм).
# tags/keywords - ключевые слова (мотивирующий, тюрьма, убийство, мошенничество, банды, ограбления, мафия, супергерои)

# DBEdges consists of:
# year_of_issue - год выпуска
# duration - продолжительность
# country - страна производства
# original_language - оригинальный язык
# genre - жанр
# place - место в рейтинге
# type - тип
# tags - ключевые слова

# about streamlit_agraph https://blog.streamlit.io/the-streamlit-agraph-component/#you-can-run-this-without-triplestore
from streamlit_agraph import agraph, Node, Edge, Config

kg_nodes_original_language = []
kg_nodes_film = []
kg_nodes_year_of_issue = []
kg_nodes_duration = []
kg_nodes_country = []
kg_nodes_genre = []
kg_nodes_place = []
kg_nodes_type = []
kg_nodes_tag = []
kg_nodes_tags = []

kg_edges_year_of_issue = []
kg_edges_duration = []
kg_edges_country = []
kg_edges_original_language = []
kg_edges_genre = []
kg_edges_place = []
kg_edges_type = []
kg_edges_tags = []
kg_edges_tag = []

# 1 - Побег из Шоушенка
text = """Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме под названием Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки. Каждый, кто попадает в эти стены, становится их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой, находит подход как к заключённым, так и к охранникам, добиваясь их особого к себе расположения."""
kg_nodes_film.append(Node(id="Побег из Шоушенка",
                          label="Побег из Шоушенка",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=--5y4Noh8JU",
                          shape="image",
                          image="https://upload.wikimedia.org/wikipedia/ru/d/de/Movie_poster_the_shawshank_redemption.jpg"))

kg_nodes_year_of_issue.append(Node(id="1994", label="1994", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Побег из Шоушенка", label="год выпуска", target="1994"))

kg_nodes_duration.append(Node(id="142", label="142 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Побег из Шоушенка", label="продолжительность", target="142"))

kg_nodes_country.append(Node(id="США", label="США", color="#b0a9ab", size=10, shape="dot"))

kg_edges_country.append(Edge(source="Побег из Шоушенка", label="страна производства", target="США"))
kg_nodes_original_language.append(Node(id="английский", label="английский", color="#b0a9ab", size=10, shape="dot"))

kg_edges_original_language.append(Edge(source="Побег из Шоушенка", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="драма", label="драма", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Побег из Шоушенка", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="1", label="1", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Побег из Шоушенка", label="место в рейтинге", target="1",))

kg_nodes_type.append(Node(id="фильм", label="фильм", color="#b0a9ab", size=10, shape="dot"))
kg_edges_type.append(Edge(source="Побег из Шоушенка", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Побег из Шоушенка", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Побег из Шоушенка", label="тэг", target="тэги Побег из Шоушенка"))

kg_nodes_tags.append(Node(id="мотивирующий", label="мотивирующий", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Побег из Шоушенка", label="тэг", target="мотивирующий"))

kg_nodes_tags.append(Node(id="тюрьма", label="тюрьма", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Побег из Шоушенка", label="тэг", target="тюрьма"))

kg_nodes_tags.append(Node(id="убийство", label="убийство", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Побег из Шоушенка", label="тэг", target="убийство"))


# 2 - Крёстный отец
text = """Криминальная сага, повествующая о нью-йоркской сицилийской мафиозной семье Корлеоне. Фильм охватывает период 1945-1955 годов.

Глава семьи, Дон Вито Корлеоне, выдаёт замуж свою дочь. В это время со Второй мировой войны возвращается его любимый сын Майкл. Майкл, герой войны, гордость семьи, не выражает желания заняться жестоким семейным бизнесом. Дон Корлеоне ведёт дела по старым правилам, но наступают иные времена, и появляются люди, желающие изменить сложившиеся порядки. На Дона Корлеоне совершается покушение."""
kg_nodes_film.append(Node(id="Крёстный отец",
                          label="Крёстный отец",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=5WxW7p4HBKU",
                          shape="image",
                          image="https://upload.wikimedia.org/wikipedia/ru/c/c4/Godfather_vhs.jpg"))

kg_nodes_year_of_issue.append(Node(id="1972", label="1972", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Крёстный отец", label="год выпуска", target="1972"))

kg_nodes_duration.append(Node(id="175", label="175 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Крёстный отец", label="продолжительность", target="175"))

kg_edges_country.append(Edge(source="Крёстный отец", label="страна производства", target="США"))

kg_edges_original_language.append(Edge(source="Крёстный отец", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="детектив", label="детектив", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Крёстный отец", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Крёстный отец", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="2", label="2", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Крёстный отец", label="место в рейтинге", target="2"))

kg_edges_type.append(Edge(source="Крёстный отец", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Крёстный отец", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Крёстный отец", label="тэг", target="тэги Крёстный отец"))

kg_nodes_tags.append(Node(id="ограбления", label="ограбления", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец", label="тэг", target="ограбления"))

kg_nodes_tags.append(Node(id="банды", label="банды", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец", label="тэг", target="банды"))

kg_nodes_tags.append(Node(id="мошенничество", label="мошенничество", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец", label="тэг", target="мошенничество"))

kg_nodes_tags.append(Node(id="мафия", label="мафия", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец", label="тэг", target="мафия"))

# 3 - Тёмный рыцарь
text = """Бэтмен поднимает ставки в войне с криминалом. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от преступности. Сотрудничество оказывается эффективным, но скоро они обнаружат себя посреди хаоса, развязанного восходящим криминальным гением, известным напуганным горожанам под именем Джокер."""
kg_nodes_film.append(Node(id="Тёмный рыцарь",
                          label="Тёмный рыцарь",
                          title=text,
                          size=25,
                          link="https://youtu.be/sVJRsiBwr70",
                          shape="image",
                          #image="https://upload.wikimedia.org/wikipedia/ru/f/f4/Тёмный_рыцарь_%282008%29_постер.jpg"
                          image = "https://clck.ru/32o6f2"))

kg_nodes_year_of_issue.append(Node(id="2008", label="2008", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Тёмный рыцарь", label="год выпуска", target="2008"))

kg_nodes_duration.append(Node(id="152", label="152 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Тёмный рыцарь", label="продолжительность", target="152"))

kg_edges_country.append(Edge(source="Тёмный рыцарь", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Тёмный рыцарь", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="боевик", label="боевик", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Тёмный рыцарь", label="жанр", target="боевик"))
kg_edges_genre.append(Edge(source="Тёмный рыцарь", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Тёмный рыцарь", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="3", label="3", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Тёмный рыцарь", label="место в рейтинге", target="3"))
kg_edges_type.append(Edge(source="Тёмный рыцарь", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Тёмный рыцарь", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Тёмный рыцарь", label="тэг", target="тэги Тёмный рыцарь"))

kg_nodes_tags.append(Node(id="супергерои", label="супергерои", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Тёмный рыцарь", label="тэг", target="супергерои"))
kg_edges_tags.append(Edge(source="тэги Тёмный рыцарь", label="тэг", target="мафия"))

# 4 - Крёстный отец 2
text = '''В центре драмы представители нового поколения гангстерского клана — дона Корлеоне и его сына, для которых не существует моральных преград на пути достижения поставленных целей. Они превращают мафию, построенную по патриархальным, еще сицилийским законам, в весьма прагматичную, жесткую корпорацию, плавно интегрирующуюся в большой бизнес Америки.'''
kg_nodes_film.append(Node(id="Крёстный отец 2",
                          label="Крёстный отец 2",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=ZlQeWiti4MU",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/a/a1/Godfather_2.jpg"))

kg_nodes_year_of_issue.append(Node(id="1974", label="1974", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Крёстный отец 2", label="год выпуска", target="1974"))

kg_nodes_duration.append(Node(id="202", label="202 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Крёстный отец 2", label="продолжительность", target="202"))

kg_edges_country.append(Edge(source="Крёстный отец 2", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Крёстный отец 2", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Крёстный отец 2", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Крёстный отец 2", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="4", label="4", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Крёстный отец 2", label="место в рейтинге", target="4"))
kg_edges_type.append(Edge(source="Крёстный отец 2", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Крёстный отец 2", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Крёстный отец 2", label="тэг", target="тэги Крёстный отец 2"))

kg_edges_tags.append(Edge(source="тэги Крёстный отец 2", label="тэг", target="ограбления"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец 2", label="тэг", target="мошенничество"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец 2", label="тэг", target="банды"))
kg_edges_tags.append(Edge(source="тэги Крёстный отец 2", label="тэг", target="мафия"))

# 5 - 12 разгневанных мужчин
text = '''Юношу обвиняют в убийстве собственного отца, ему грозит электрический стул. Двенадцать присяжных собираются, чтобы вынести вердикт: виновен или нет. С начала заседания почти все считают подсудимого виновным, и лишь только один из двенадцати позволил себе усомниться. И он решает убедить остальных в своей правоте.'''
kg_nodes_film.append(Node(id="12 разгневанных мужчин",
                          label="12 разгневанных мужчин",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=o5OhDVmDA0s",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/commons/b/b5/12_Angry_Men_%281957_film_poster%29.jpg"))

kg_nodes_year_of_issue.append(Node(id="1957", label="1957", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="12 разгневанных мужчин", label="год выпуска", target="1957"))

kg_nodes_duration.append(Node(id="97", label="97 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="12 разгневанных мужчин", label="продолжительность", target="97"))

kg_edges_country.append(Edge(source="12 разгневанных мужчин", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="12 разгневанных мужчин", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="12 разгневанных мужчин", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="12 разгневанных мужчин", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="5", label="5", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="12 разгневанных мужчин", label="место в рейтинге", target="5"))
kg_edges_type.append(Edge(source="12 разгневанных мужчин", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги 12 разгневанных мужчин", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="12 разгневанных мужчин", label="тэг", target="тэги 12 разгневанных мужчин"))

kg_edges_tags.append(Edge(source="тэги 12 разгневанных мужчин", label="тэг", target="ограбления"))
kg_edges_tags.append(Edge(source="тэги 12 разгневанных мужчин", label="тэг", target="мошенничество"))

# 6 - Список Шиндлера
text = '''Фильм рассказывает реальную историю загадочного Оскара Шиндлера, члена нацистской партии, преуспевающего фабриканта, спасшего во время Второй мировой войны почти 1200 евреев.'''
kg_nodes_film.append(Node(id="Список Шиндлера",
                          label="Список Шиндлера",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=7d306gUd0xA",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/3/38/Schindler%27s_List_movie.jpg"))

kg_nodes_year_of_issue.append(Node(id="1953", label="1953", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Список Шиндлера", label="год выпуска", target="1953"))

kg_nodes_duration.append(Node(id="197", label="197 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Список Шиндлера", label="продолжительность", target="197"))

kg_edges_country.append(Edge(source="Список Шиндлера", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Список Шиндлера", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="биография", label="биография", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_genre.append(Node(id="исторический", label="исторический", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Список Шиндлера", label="жанр", target="биография"))
kg_edges_genre.append(Edge(source="Список Шиндлера", label="жанр", target="исторический"))
kg_edges_genre.append(Edge(source="Список Шиндлера", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="6", label="6", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Список Шиндлера", label="место в рейтинге", target="6"))
kg_edges_type.append(Edge(source="Список Шиндлера", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Список Шиндлера", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Список Шиндлера", label="тэг", target="тэги Список Шиндлера"))

kg_nodes_tags.append(Node(id="биографии", label="биографии", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="основан на реальных событиях", label="основан на реальных событиях", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Список Шиндлера", label="тэг", target="биографии"))
kg_edges_tags.append(Edge(source="тэги Список Шиндлера", label="тэг", target="основан на реальных событиях"))

# 7 - Властелин колец: Возвращение короля
text = '''Повелитель сил тьмы Саурон направляет свою бесчисленную армию под стены Минас-Тирита, крепости Последней Надежды. Он предвкушает близкую победу, но именно это мешает ему заметить две крохотные фигурки — хоббитов, приближающихся к Роковой Горе, где им предстоит уничтожить Кольцо Всевластья.'''
kg_nodes_film.append(Node(id="Властелин колец: Возвращение короля",
                          label="Властелин колец: Возвращение короля",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=pzQJHZkVrGs",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/5/53/The_Lord_of_the_Rings._The_Return_of_the_King_—_movie.jpg"))

kg_nodes_year_of_issue.append(Node(id="2003", label="2003", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Властелин колец: Возвращение короля", label="год выпуска", target="2003"))

kg_nodes_duration.append(Node(id="263", label="263 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Властелин колец: Возвращение короля", label="продолжительность", target="263"))

kg_edges_country.append(Edge(source="Властелин колец: Возвращение короля", label="страна производства", target="США"))
kg_nodes_country.append(Node(id="Новая Зеландия", label="Новая Зеландия", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Властелин колец: Возвращение короля", label="страна производства", target="Новая Зеландия"))
kg_edges_original_language.append(Edge(source="Властелин колец: Возвращение короля", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="фэнтэзи", label="фэнтэзи", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_genre.append(Node(id="приключение", label="приключение", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Властелин колец: Возвращение короля", label="жанр", target="фэнтэзи"))
kg_edges_genre.append(Edge(source="Властелин колец: Возвращение короля", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Властелин колец: Возвращение короля", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="7", label="7", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Властелин колец: Возвращение короля", label="место в рейтинге", target="7"))
kg_edges_type.append(Edge(source="Властелин колец: Возвращение короля", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Властелин колец: Возвращение короля", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Властелин колец: Возвращение короля", label="тэг", target="тэги Властелин колец: Возвращение короля"))

kg_nodes_tags.append(Node(id="короли", label="короли", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="сражения", label="сражения", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="колдовство", label="колдовство", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Возвращение короля", label="тэг", target="колдовство"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Возвращение короля", label="тэг", target="короли"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Возвращение короля", label="тэг", target="сражения"))

# 8 - Криминальное чтиво
text = '''Двое бандитов Винсент Вега и Джулс Винфилд ведут философские беседы в перерывах между разборками и решением проблем с должниками криминального босса Марселласа Уоллеса.

В первой истории Винсент проводит незабываемый вечер с женой Марселласа Мией. Во второй рассказывается о боксёре Бутче Кулидже, купленном Уоллесом, чтобы сдать бой. В третьей истории Винсент и Джулс по нелепой случайности попадают в неприятности.'''
kg_nodes_film.append(Node(id="Криминальное чтиво",
                          label="Криминальное чтиво",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=gqRyNjsfFuI",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/9/93/Pulp_Fiction.jpg"))

kg_edges_year_of_issue.append(Edge(source="Криминальное чтиво", label="год выпуска", target="1994"))

kg_nodes_duration.append(Node(id="154", label="154 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Криминальное чтиво", label="продолжительность", target="154"))

kg_edges_country.append(Edge(source="Криминальное чтиво", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Криминальное чтиво", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="черная комедия", label="черная комедия", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Криминальное чтиво", label="жанр", target="черная комедия"))
kg_edges_genre.append(Edge(source="Криминальное чтиво", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="8", label="8", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Криминальное чтиво", label="место в рейтинге", target="8"))
kg_edges_type.append(Edge(source="Криминальное чтиво", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Криминальное чтиво", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Криминальное чтиво", label="тэг", target="тэги Криминальное чтиво"))

kg_nodes_tags.append(Node(id="криминал", label="криминал", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="бандиты", label="бандиты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Криминальное чтиво", label="тэг", target="бандиты"))
kg_edges_tags.append(Edge(source="тэги Криминальное чтиво", label="тэг", target="криминал"))

# 9 - Властелин колец: Братство Кольца
text = '''Сказания о Средиземье — это хроника Великой войны за Кольцо, длившейся не одну тысячу лет. Тот, кто владел Кольцом, получал неограниченную власть, но был обязан служить злу.

Тихая деревня, где живут хоббиты. Придя на 111-й день рождения к своему старому другу Бильбо Бэггинсу, волшебник Гэндальф начинает вести разговор о кольце, которое Бильбо нашел много лет назад. Это кольцо принадлежало когда-то темному властителю Средиземья Саурону, и оно дает большую власть своему обладателю. Теперь Саурон хочет вернуть себе власть над Средиземьем. Бильбо отдает Кольцо племяннику Фродо, чтобы тот отнёс его к Роковой Горе и уничтожил.'''
kg_nodes_film.append(Node(id="Властелин колец: Братство Кольца",
                          label="Властелин колец: Братство Кольца",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=wIQGFjCh81o",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/0/08/The_Lord_of_the_Rings._The_Fellowship_of_the_Ring_—_movie.jpg"))

kg_nodes_year_of_issue.append(Node(id="2001", label="2001", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Властелин колец: Братство Кольца", label="год выпуска", target="2001"))

kg_nodes_duration.append(Node(id="228", label="228 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Властелин колец: Братство Кольца", label="продолжительность", target="228"))

kg_edges_country.append(Edge(source="Властелин колец: Братство Кольца", label="страна производства", target="США"))
kg_edges_country.append(Edge(source="Властелин колец: Братство Кольца", label="страна производства", target="Новая Зеландия"))
kg_edges_original_language.append(Edge(source="Властелин колец: Братство Кольца", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Властелин колец: Братство Кольца", label="жанр", target="фэнтэзи"))
kg_edges_genre.append(Edge(source="Властелин колец: Братство Кольца", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Властелин колец: Братство Кольца", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="9", label="9", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Властелин колец: Братство Кольца", label="место в рейтинге", target="9"))
kg_edges_type.append(Edge(source="Властелин колец: Братство Кольца", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Властелин колец: Братство Кольца", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Властелин колец: Братство Кольца", label="тэг", target="тэги Властелин колец: Братство Кольца"))

kg_nodes_tags.append(Node(id="кольцо", label="кольцо", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Братство Кольца", label="тэг", target="кольцо"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Братство Кольца", label="тэг", target="колдовство"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Братство Кольца", label="тэг", target="короли"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Братство Кольца", label="тэг", target="сражения"))

# 10 - Хороший, плохой, злой
text = '''В разгар гражданской войны таинственный стрелок скитается по просторам Дикого Запада. У него нет ни дома, ни друзей, ни компаньонов, пока он не встречает двоих незнакомцев, таких же безжалостных и циничных.

По воле судьбы трое мужчин вынуждены объединить свои усилия в поисках украденного золота. Но совместная работа - не самое подходящее занятие для таких отъявленных бандитов, как они. Компаньоны вскоре понимают, что в их дерзком и опасном путешествии по разоренной войной стране самое важное - никому не доверять и держать пистолет наготове, если хочешь остаться в живых.'''
kg_nodes_film.append(Node(id="Хороший, плохой, злой",
                          label="Хороший, плохой, злой",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=0Bwxz16-T04",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/f/fd/Goodbadugly.JPG"))

kg_nodes_year_of_issue.append(Node(id="1966", label="1966", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Хороший, плохой, злой", label="год выпуска", target="1966"))

kg_nodes_duration.append(Node(id="178", label="178 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Хороший, плохой, злой", label="продолжительность", target="178"))

kg_nodes_country.append(Node(id="Италия", label="Италия", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Хороший, плохой, злой", label="страна производства", target="Италия"))
kg_nodes_original_language.append(Node(id="итальянский", label="итальянский", color="#b0a9ab", size=10, shape="dot"))
kg_edges_original_language.append(Edge(source="Хороший, плохой, злой", label="оригинальный язык", target="итальянский"))

kg_nodes_genre.append(Node(id="вестерн", label="вестерн", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Хороший, плохой, злой", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Хороший, плохой, злой", label="жанр", target="вестерн"))

kg_nodes_place.append(Node(id="10", label="10", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Хороший, плохой, злой", label="место в рейтинге", target="10"))
kg_edges_type.append(Edge(source="Хороший, плохой, злой", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Хороший, плохой, злой", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Хороший, плохой, злой", label="тэг", target="тэги Хороший, плохой, злой"))

kg_edges_tags.append(Edge(source="тэги Хороший, плохой, злой", label="тэг", target="ограбления"))
kg_edges_tags.append(Edge(source="тэги Хороший, плохой, злой", label="тэг", target="мошенничество"))

# 11 - Форрест Гамп
text = '''Сидя на автобусной остановке, Форрест Гамп — не очень умный, но добрый и открытый парень — рассказывает случайным встречным историю своей необыкновенной жизни.

С самого малолетства парень страдал от заболевания ног, соседские мальчишки дразнили его, но в один прекрасный день Форрест открыл в себе невероятные способности к бегу. Подруга детства Дженни всегда его поддерживала и защищала, но вскоре дороги их разошлись.'''
kg_nodes_film.append(Node(id="Форрест Гамп",
                          label="Форрест Гамп",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=77ij5gCTjYU",
                          shape="image",
                          image = "https://clck.ru/32pDsb"))

kg_edges_year_of_issue.append(Edge(source="Форрест Гамп", label="год выпуска", target="1994"))

kg_edges_duration.append(Edge(source="Форрест Гамп", label="продолжительность", target="142"))

kg_edges_country.append(Edge(source="Форрест Гамп", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Форрест Гамп", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="мелодрама", label="мелодрама", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Форрест Гамп", label="жанр", target="драма"))
kg_edges_genre.append(Edge(source="Форрест Гамп", label="жанр", target="мелодрама"))

kg_nodes_place.append(Node(id="11", label="11", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Форрест Гамп", label="место в рейтинге", target="11"))
kg_edges_type.append(Edge(source="Форрест Гамп", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Форрест Гамп", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Форрест Гамп", label="тэг", target="тэги Форрест Гамп"))

kg_nodes_tags.append(Node(id="про жизнь", label="про жизнь", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="экранизация книги", label="экранизация книги", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Форрест Гамп", label="тэг", target="про жизнь"))
kg_edges_tags.append(Edge(source="тэги Форрест Гамп", label="тэг", target="экранизация книги"))
kg_edges_tags.append(Edge(source="тэги Форрест Гамп", label="тэг", target="мотивирующий"))

# 12 - Бойцовский клуб
text = '''Сотрудник страховой компании страдает хронической бессонницей и отчаянно пытается вырваться из мучительно скучной жизни. Однажды в очередной командировке он встречает некоего Тайлера Дёрдена — харизматического торговца мылом с извращенной философией. Тайлер уверен, что самосовершенствование — удел слабых, а единственное, ради чего стоит жить, — саморазрушение.

Проходит немного времени, и вот уже новые друзья лупят друг друга почем зря на стоянке перед баром, и очищающий мордобой доставляет им высшее блаженство. Приобщая других мужчин к простым радостям физической жестокости, они основывают тайный Бойцовский клуб, который начинает пользоваться невероятной популярностью.'''
kg_nodes_film.append(Node(id="Бойцовский клуб",
                          label="Бойцовский клуб",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=GbS-kM6jb9w",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/8/8a/Fight_club.jpg"))

kg_nodes_year_of_issue.append(Node(id="1999", label="1999", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Бойцовский клуб", label="год выпуска", target="1999"))

kg_nodes_duration.append(Node(id="139", label="139 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Бойцовский клуб", label="продолжительность", target="139"))

kg_edges_country.append(Edge(source="Бойцовский клуб", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Бойцовский клуб", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="триллер", label="триллер", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_genre.append(Node(id="мистический", label="мистический", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Бойцовский клуб", label="жанр", target="драма"))
kg_edges_genre.append(Edge(source="Бойцовский клуб", label="жанр", target="триллер"))
kg_edges_genre.append(Edge(source="Бойцовский клуб", label="жанр", target="мистический"))

kg_nodes_place.append(Node(id="12", label="12", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Бойцовский клуб", label="место в рейтинге", target="12"))
kg_edges_type.append(Edge(source="Бойцовский клуб", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Бойцовский клуб", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Бойцовский клуб", label="тэг", target="тэги Бойцовский клуб"))

kg_nodes_tags.append(Node(id="психологический", label="психологический", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="бои", label="бои", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Бойцовский клуб", label="тэг", target="психологический"))
kg_edges_tags.append(Edge(source="тэги Бойцовский клуб", label="тэг", target="бои"))

# 13 - Начало
text = '''Кобб – талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадет ценные секреты из глубин подсознания во время сна, когда человеческий разум наиболее уязвим. Редкие способности Кобба сделали его ценным игроком в привычном к предательству мире промышленного шпионажа, но они же превратили его в извечного беглеца и лишили всего, что он когда-либо любил.

И вот у Кобба появляется шанс исправить ошибки. Его последнее дело может вернуть все назад, но для этого ему нужно совершить невозможное – инициацию. Вместо идеальной кражи Кобб и его команда спецов должны будут провернуть обратное. Теперь их задача – не украсть идею, а внедрить ее. Если у них получится, это и станет идеальным преступлением.

Но никакое планирование или мастерство не могут подготовить команду к встрече с опасным противником, который, кажется, предугадывает каждый их ход. Врагом, увидеть которого мог бы лишь Кобб.'''
kg_nodes_film.append(Node(id="Начало",
                          label="Начало",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=YaW8x81EGtw",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/b/bc/Poster_Inception_film_2010.jpg"))

kg_nodes_year_of_issue.append(Node(id="2010", label="2010", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Начало", label="год выпуска", target="2010"))

kg_nodes_duration.append(Node(id="148", label="148 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Начало", label="продолжительность", target="148"))

kg_nodes_country.append(Node(id="Великобритания", label="Великобритания", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Начало", label="страна производства", target="Великобритания"))
kg_edges_original_language.append(Edge(source="Начало", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="научная фантастика", label="научная фантастика", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Начало", label="жанр", target="боевик"))
kg_edges_genre.append(Edge(source="Начало", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Начало", label="жанр", target="мистический"))

kg_nodes_place.append(Node(id="13", label="13", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Начало", label="место в рейтинге", target="13"))
kg_edges_type.append(Edge(source="Начало", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Начало", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Начало", label="тэг", target="тэги Начало"))

kg_edges_tags.append(Edge(source="тэги Начало", label="тэг", target="ограбления"))
kg_edges_tags.append(Edge(source="тэги Начало", label="тэг", target="мошенничество"))

# 14 - Властелин колец: Две крепости
text = '''Братство распалось, но Кольцо Всевластья должно быть уничтожено. Фродо и Сэм вынуждены довериться Голлуму, который взялся провести их к вратам Мордора. Громадная армия Сарумана приближается: члены братства и их союзники готовы принять бой. Битва за Средиземье продолжается.'''
kg_nodes_film.append(Node(id="Властелин колец: Две крепости",
                          label="Властелин колец: Две крепости",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=roC_y0KhL-Q",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/f/f0/The_Lord_of_the_Rings._The_Two_Towers_—_movie.jpg"))

kg_nodes_year_of_issue.append(Node(id="2002", label="2002", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Властелин колец: Две крепости", label="год выпуска", target="2002"))

kg_nodes_duration.append(Node(id="179", label="179 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Властелин колец: Две крепости", label="продолжительность", target="179"))

kg_edges_country.append(Edge(source="Властелин колец: Две крепости", label="страна производства", target="США"))
kg_edges_country.append(Edge(source="Властелин колец: Две крепости", label="страна производства", target="Новая Зеландия"))
kg_edges_original_language.append(Edge(source="Властелин колец: Две крепости", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Властелин колец: Две крепости", label="жанр", target="фэнтэзи"))
kg_edges_genre.append(Edge(source="Властелин колец: Две крепости", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Властелин колец: Две крепости", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="14", label="14", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Властелин колец: Две крепости", label="место в рейтинге", target="14"))
kg_edges_type.append(Edge(source="Властелин колец: Две крепости", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Властелин колец: Две крепости", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Властелин колец: Две крепости", label="тэг", target="тэги Властелин колец: Две крепости"))

kg_edges_tags.append(Edge(source="тэги Властелин колец: Две крепости", label="тэг", target="колдовство"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Две крепости", label="тэг", target="короли"))
kg_edges_tags.append(Edge(source="тэги Властелин колец: Две крепости", label="тэг", target="сражения"))

# 15 - Звёздные войны. Эпизод V: Империя наносит ответный удар
text = '''Борьба за Галактику обостряется в пятом эпизоде космической саги. Войска Императора начинают массированную атаку на повстанцев и их союзников.

Хан Соло и принцесса Лейя укрываются в Заоблачном Городе, в котором их и захватывает Дарт Вейдер, в то время как Люк Скайуокер находится на таинственной планете джунглей Дагоба.

Там Мастер - джедай Йода обучает молодого рыцаря навыкам обретения Силы. Люк даже не предполагает, как скоро ему придется воспользоваться знаниями старого Мастера: впереди битва с превосходящими силами Императора и смертельный поединок с Дартом Вейдером.'''
kg_nodes_film.append(Node(id="Звёздные войны. Эпизод V: Империя наносит ответный удар",
                          label="Звёздные войны. Эпизод V: Империя наносит ответный удар",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=NFZH4eb-36E",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/e/e0/Empire20strikes20back_old.jpg"))

kg_nodes_year_of_issue.append(Node(id="1980", label="1980", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="год выпуска", target="1980"))

kg_nodes_duration.append(Node(id="124", label="124 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="продолжительность", target="124"))

kg_edges_country.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="15", label="15", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="место в рейтинге", target="15"))
kg_edges_type.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Звёздные войны. Эпизод V: Империя наносит ответный удар", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Звёздные войны. Эпизод V: Империя наносит ответный удар", label="тэг", target="тэги Звёздные войны. Эпизод V: Империя наносит ответный удар"))

kg_nodes_tags.append(Node(id="про космос", label="про космос", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод V: Империя наносит ответный удар", label="тэг", target="про космос"))
kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод V: Империя наносит ответный удар", label="тэг", target="сражения"))
kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод V: Империя наносит ответный удар", label="тэг", target="короли"))

# 16 - Матрица
text = '''Жизнь Томаса Андерсона разделена на две части: днём он — самый обычный офисный работник, получающий нагоняи от начальства, а ночью превращается в хакера по имени Нео, и нет места в сети, куда он бы не смог проникнуть. Но однажды всё меняется. Томас узнаёт ужасающую правду о реальности.'''
kg_nodes_film.append(Node(id="Матрица",
                          label="Матрица",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=37WZxxAk_Lc",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/9/9d/Matrix-DVD.jpg"))


kg_edges_year_of_issue.append(Edge(source="Матрица", label="год выпуска", target="1999"))

kg_nodes_duration.append(Node(id="136", label="136 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Матрица", label="продолжительность", target="136"))

kg_nodes_country.append(Node(id="Австралия", label="Австралия", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Матрица", label="страна производства", target="Австралия"))
kg_edges_country.append(Edge(source="Матрица", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Матрица", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Матрица", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Матрица", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Матрица", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="16", label="16", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Матрица", label="место в рейтинге", target="16"))
kg_edges_type.append(Edge(source="Матрица", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Матрица", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Матрица", label="тэг", target="тэги Матрица"))

kg_nodes_tags.append(Node(id="антиутопия", label="антиутопия", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="агенты", label="агенты", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="хаккеры и программисты", label="хаккеры и программисты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Матрица", label="тэг", target="антиутопия"))
kg_edges_tags.append(Edge(source="тэги Матрица", label="тэг", target="сражения"))
kg_edges_tags.append(Edge(source="тэги Матрица", label="тэг", target="агенты"))
kg_edges_tags.append(Edge(source="тэги Матрица", label="тэг", target="хаккеры и программисты"))

# 17 - Славные парни
text = '''Что бывает, когда напарником брутального костолома становится субтильный лопух? Наемный охранник Джексон Хили и частный детектив Холланд Марч вынуждены работать в паре, чтобы распутать плевое дело о пропавшей девушке, которое оборачивается преступлением века.

Смогут ли парни разгадать сложный ребус, если у каждого из них – свои, весьма индивидуальные методы.'''
kg_nodes_film.append(Node(id="Славные парни",
                          label="Славные парни",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=w8McpqGVc2A",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/9/99/Goodfellas_Cover.jpg"))

kg_nodes_year_of_issue.append(Node(id="1990", label="1990", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Славные парни", label="год выпуска", target="1990"))

kg_nodes_duration.append(Node(id="146", label="146 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Славные парни", label="продолжительность", target="146"))

kg_edges_country.append(Edge(source="Славные парни", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Славные парни", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Славные парни", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Славные парни", label="жанр", target="триллер"))
kg_edges_genre.append(Edge(source="Славные парни", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="17", label="17", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Славные парни", label="место в рейтинге", target="17"))
kg_edges_type.append(Edge(source="Славные парни", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Славные парни", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Славные парни", label="тэг", target="тэги Славные парни"))

kg_edges_tags.append(Edge(source="тэги Славные парни", label="тэг", target="основан на реальных событиях"))
kg_edges_tags.append(Edge(source="тэги Славные парни", label="тэг", target="мафия"))
kg_edges_tags.append(Edge(source="тэги Славные парни", label="тэг", target="банды"))

# 18 - Пролетая над гнездом кукушки
text = '''Рэндла Патрика Макмёрфи, патологического преступника и бунтаря, переводят из колонии в психиатрическую клинику, чтобы установить, является он душевнобольным или нет. В клинике он обнаруживает, что отделение контролирует хладнокровная, строгая и одержимая распорядком старшая медсестра Милдред Рэтчед. Макмёрфи намерен не подчиняться абсурдным, на его взгляд, правилам и одновременно повеселиться от души. Его бунтарская натура заражает других пациентов, но сестра Рэтчед решительно настроена пресечь это.'''
kg_nodes_film.append(Node(id="Пролетая над гнездом кукушки",
                          label="Пролетая над гнездом кукушки",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=MKTrVgnEois",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg"))

kg_nodes_year_of_issue.append(Node(id="1975", label="1975", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Пролетая над гнездом кукушки", label="год выпуска", target="1975"))

kg_nodes_duration.append(Node(id="133", label="133 минуты", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Пролетая над гнездом кукушки", label="продолжительность", target="133"))

kg_edges_country.append(Edge(source="Пролетая над гнездом кукушки", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Пролетая над гнездом кукушки", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Пролетая над гнездом кукушки", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="18", label="18", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Пролетая над гнездом кукушки", label="место в рейтинге", target="18"))
kg_edges_type.append(Edge(source="Пролетая над гнездом кукушки", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Пролетая над гнездом кукушки", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Пролетая над гнездом кукушки", label="тэг", target="тэги Пролетая над гнездом кукушки"))

kg_edges_tags.append(Edge(source="тэги Пролетая над гнездом кукушки", label="тэг", target="психологический"))
kg_edges_tags.append(Edge(source="тэги Пролетая над гнездом кукушки", label="тэг", target="тюрьма"))

# 19 - Семь
text = '''Детектив Уильям Сомерсет - ветеран уголовного розыска, мечтающий уйти на пенсию и уехать подальше от города и грешных обитателей. За 7 дней до пенсии на Сомерсета сваливаются две неприятности: молодой напарник Миллс и особо изощренное убийство. Острый ум опытного сыщика сразу определяет, что за этим преступлением, скорее всего, последуют другие. Новости подтверждают его догадку. Поняв, что убийца наказывает свои жертвы за совершенные ими смертные грехи, детектив встает перед выбором: вернуться к работе либо уйти и передать дело своему менее опытному напарнику?'''
kg_nodes_film.append(Node(id="Семь",
                          label="Семь",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=MqwDC3buVr4",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/8/83/Se7en_%28poster%29.jpg"))

kg_nodes_year_of_issue.append(Node(id="1995", label="1995", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Семь", label="год выпуска", target="1995"))

kg_nodes_duration.append(Node(id="127", label="127 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Семь", label="продолжительность", target="127"))

kg_edges_country.append(Edge(source="Семь", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Семь", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Семь", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Семь", label="жанр", target="мистический"))
kg_edges_genre.append(Edge(source="Семь", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="19", label="19", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Семь", label="место в рейтинге", target="19"))
kg_edges_type.append(Edge(source="Семь", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Семь", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Семь", label="тэг", target="тэги Семь"))

kg_nodes_tags.append(Node(id="преступление", label="преступление", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Семь", label="тэг", target="психологический"))
kg_edges_tags.append(Edge(source="тэги Семь", label="тэг", target="преступление"))

# 20 - Семь самураев
text = '''Япония, XVI век. В стране полыхает гражданская война, повсюду орудуют банды разбойников и мародеров. Бедные крестьяне нанимают для защиты деревни семерых самураев, которые немного сплачивают раздробленных и малодушных селян в процессе подготовки и укрепления деревни.'''
kg_nodes_film.append(Node(id="Семь самураев",
                          label="Семь самураев",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=hFm3lzTzWR8",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/commons/9/92/Sevensamurai-movieposter1954.jpg"))

kg_nodes_year_of_issue.append(Node(id="1954", label="1954", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Семь самураев", label="год выпуска", target="1954"))

kg_nodes_duration.append(Node(id="207", label="207 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Семь самураев", label="продолжительность", target="207"))

kg_nodes_country.append(Node(id="Япония", label="Япония", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_original_language.append(Node(id="японский", label="японский", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Семь самураев", label="страна производства", target="Япония"))
kg_edges_original_language.append(Edge(source="Семь самураев", label="оригинальный язык", target="японский"))

kg_edges_genre.append(Edge(source="Семь самураев", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Семь самураев", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="20", label="20", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Семь самураев", label="место в рейтинге", target="20"))
kg_edges_type.append(Edge(source="Семь самураев", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Семь самураев", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Семь самураев", label="тэг", target="тэги Семь самураев"))

kg_nodes_tags.append(Node(id="война", label="война", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="самураи", label="самураи", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Семь самураев", label="тэг", target="война"))
kg_edges_tags.append(Edge(source="тэги Семь самураев", label="тэг", target="банды"))
kg_edges_tags.append(Edge(source="тэги Семь самураев", label="тэг", target="про жизнь"))
kg_edges_tags.append(Edge(source="тэги Семь самураев", label="тэг", target="самураи"))

# 21 - Эта замечательная жизнь
text = '''Джордж Бейли, владелец кредитной компании в выдуманном американском городке Бедфорд Фоллс, честный, отзывчивый, любящий муж и отец, подавлен свалившимися на него невзгодами и подумывает о самоубийстве.

Очевидно, что человек, отказывающийся от самого большого дара Бога – жизни – нуждается в помощи ангела-хранителя. И Небеса отправляют ему на выручку Кларенса, единственного свободного на тот момент Ангела Второго Класса, приятного, доброго, но неопытного, еще даже не заслужившего крылья.

Если он сделает свою работу хорошо и сможет отговорить Джорджа от смертного греха, он получит крылья. А времени у него почти не осталось… Кларенс находит единственно правильное решение – показать Джорджу мир, в котором тот не существует.'''
kg_nodes_film.append(Node(id="Эта замечательная жизнь",
                          label="Эта замечательная жизнь",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=tzFLF9XvfTI",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/commons/2/25/It%27s_a_Wonderful_Life_%281946_poster%29.jpeg"))

kg_nodes_year_of_issue.append(Node(id="1946", label="1946", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Эта замечательная жизнь", label="год выпуска", target="1946"))

kg_nodes_duration.append(Node(id="125", label="125 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Эта замечательная жизнь", label="продолжительность", target="125"))

kg_edges_country.append(Edge(source="Эта замечательная жизнь", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Эта замечательная жизнь", label="оригинальный язык", target="английский"))

kg_nodes_genre.append(Node(id="сказка", label="сказка", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_genre.append(Node(id="семейный", label="семейный", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Эта замечательная жизнь", label="жанр", target="сказка"))
kg_edges_genre.append(Edge(source="Эта замечательная жизнь", label="жанр", target="семейный"))
kg_edges_genre.append(Edge(source="Эта замечательная жизнь", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="21", label="21", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Эта замечательная жизнь", label="место в рейтинге", target="21"))
kg_edges_type.append(Edge(source="Эта замечательная жизнь", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Эта замечательная жизнь", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Эта замечательная жизнь", label="тэг", target="тэги Эта замечательная жизнь"))

kg_edges_tags.append(Edge(source="тэги Эта замечательная жизнь", label="тэг", target="экранизация книги"))
kg_edges_tags.append(Edge(source="тэги Эта замечательная жизнь", label="тэг", target="про жизнь"))

# 22 - Молчание ягнят
text = '''Психопат похищает и убивает молодых женщин по всему Среднему Западу. ФБР, уверенное, что все преступления совершены одним и тем же человеком, поручает агенту Клариссе Старлинг встретиться с заключенным-маньяком Ганнибалом Лектером, который мог бы помочь составить психологический портрет убийцы. Сам Лектер отбывает наказание за убийства и каннибализм. Он согласен помочь Клариссе лишь в том случае, если она попотчует его больное воображение подробностями своей личной жизни.'''
kg_nodes_film.append(Node(id="Молчание ягнят ",
                          label="Молчание ягнят ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=sHqrhjNCmTo",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/9/95/The_Silence_Of_The_Lambs.jpg"))

kg_nodes_year_of_issue.append(Node(id="1991", label="1991", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Молчание ягнят ", label="год выпуска", target="1991"))

kg_nodes_duration.append(Node(id="118", label="118 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Молчание ягнят ", label="продолжительность", target="118"))

kg_edges_country.append(Edge(source="Молчание ягнят ", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Молчание ягнят ", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Молчание ягнят ", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Молчание ягнят ", label="жанр", target="мистический"))

kg_nodes_place.append(Node(id="22", label="22", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Молчание ягнят ", label="место в рейтинге", target="22"))
kg_edges_type.append(Edge(source="Молчание ягнят ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Молчание ягнят ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Молчание ягнят ", label="тэг", target="тэги Молчание ягнят "))

kg_edges_tags.append(Edge(source="тэги Молчание ягнят ", label="тэг", target="убийство"))
kg_edges_tags.append(Edge(source="тэги Молчание ягнят ", label="тэг", target="психологический"))

# 23 - Город Бога
text = '''Парень по кличке Ракета, балансирующий между честной жизнью и мелкими правонарушениями, и его знакомый Дадинью, который с восьми лет начал карьеру гангстера, выживают как могут в так называемом Городе бога — трущобах Рио-де-Жанейро.'''
kg_nodes_film.append(Node(id="Город Бога ",
                          label="Город Бога ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=sEjlosZA5Qw",
                          shape="image",
                          image = "https://www.kinopoisk.ru/picture/2976353/"))

kg_edges_year_of_issue.append(Edge(source="Город Бога ", label="год выпуска", target="2002"))

kg_nodes_duration.append(Node(id="130", label="130 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Город Бога ", label="продолжительность", target="130"))

kg_nodes_country.append(Node(id="Бразилия", label="Бразилия", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_original_language.append(Node(id="португальский", label="португальский", color="#b0a9ab", size=10, shape="dot"))
kg_edges_country.append(Edge(source="Город Бога ", label="страна производства", target="Бразилия"))
kg_edges_original_language.append(Edge(source="Город Бога ", label="оригинальный язык", target="португальский"))

kg_edges_genre.append(Edge(source="Город Бога ", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Город Бога ", label="жанр", target="драма"))

kg_nodes_place.append(Node(id="23", label="23", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Город Бога ", label="место в рейтинге", target="23"))
kg_edges_type.append(Edge(source="Город Бога ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Город Бога ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Город Бога ", label="тэг", target="тэги Город Бога "))

kg_edges_tags.append(Edge(source="тэги Город Бога ", label="тэг", target="про жизнь"))
kg_edges_tags.append(Edge(source="тэги Город Бога ", label="тэг", target="мафия"))

# 24 - Спасти рядового Райана
text = '''Вторая мировая. Капитан Джон Миллер получает тяжелое задание. Вместе с отрядом из восьми человек он должен отправиться в тыл врага на поиски рядового Джеймса Райана, три родных брата которого почти одновременно погибли на полях сражений.

Командование приняло решение демобилизовать Райана и отправить его на родину к безутешной матери. Но чтобы найти и спасти солдата, крошечному отряду придется пройти через все круги ада.'''
kg_nodes_film.append(Node(id="Спасти рядового Райана ",
                          label="Спасти рядового Райана ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=_TDNs9Sn3BE",
                          shape="image",
                          image = "https://clck.ru/32pMzM"))

kg_nodes_year_of_issue.append(Node(id="1998", label="1998", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Спасти рядового Райана ", label="год выпуска", target="1998"))

kg_nodes_duration.append(Node(id="169", label="169 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Спасти рядового Райана ", label="продолжительность", target="169"))

kg_edges_country.append(Edge(source="Спасти рядового Райана ", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Спасти рядового Райана ", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Спасти рядового Райана ", label="жанр", target="боевик"))
kg_edges_genre.append(Edge(source="Спасти рядового Райана ", label="жанр", target="драма"))
kg_edges_genre.append(Edge(source="Спасти рядового Райана ", label="жанр", target="исторический"))

kg_nodes_place.append(Node(id="24", label="24", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Спасти рядового Райана ", label="место в рейтинге", target="24"))
kg_edges_type.append(Edge(source="Спасти рядового Райана ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Спасти рядового Райана ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Спасти рядового Райана ", label="тэг", target="тэги Спасти рядового Райана "))

kg_nodes_tags.append(Node(id="танки", label="танки", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Спасти рядового Райана ", label="тэг", target="война"))
kg_edges_tags.append(Edge(source="тэги Спасти рядового Райана ", label="тэг", target="танки"))
kg_edges_tags.append(Edge(source="тэги Спасти рядового Райана ", label="тэг", target="про жизнь"))

# 25 - Жизнь прекрасна
text = '''Во время Второй мировой войны из Италии в концлагерь были отправлены евреи - отец с маленьким сыном. Жена-итальянка добровольно последовала за ними. В лагере отец сказал мальчику, что всё происходящее вокруг является большой интересной игрой за приз в виде настоящего танка. И этот классный приз достанется тому мальчику, который сможет не попасться на глаза надзирателям.'''
kg_nodes_film.append(Node(id="Жизнь прекрасна ",
                          label="Жизнь прекрасна ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=TcjfceqbC4M",
                          shape="image",
                          image = "https://clck.ru/32pNL4"))

kg_nodes_year_of_issue.append(Node(id="1997", label="1997", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Жизнь прекрасна ", label="год выпуска", target="1997"))

kg_nodes_duration.append(Node(id="116", label="116 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Жизнь прекрасна ", label="продолжительность", target="116"))

kg_edges_country.append(Edge(source="Жизнь прекрасна ", label="страна производства", target="Италия"))
kg_edges_original_language.append(Edge(source="Жизнь прекрасна ", label="оригинальный язык", target="итальянский"))

kg_nodes_genre.append(Node(id="военный", label="военный", color="#b0a9ab", size=10, shape="dot"))
kg_edges_genre.append(Edge(source="Жизнь прекрасна ", label="жанр", target="мелодрама"))
kg_edges_genre.append(Edge(source="Жизнь прекрасна ", label="жанр", target="драма"))
kg_edges_genre.append(Edge(source="Жизнь прекрасна ", label="жанр", target="военный"))

kg_nodes_place.append(Node(id="25", label="25", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Жизнь прекрасна ", label="место в рейтинге", target="25"))
kg_edges_type.append(Edge(source="Жизнь прекрасна ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Жизнь прекрасна ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Жизнь прекрасна ", label="тэг", target="тэги Жизнь прекрасна "))

kg_edges_tags.append(Edge(source="тэги Жизнь прекрасна ", label="тэг", target="война"))
kg_edges_tags.append(Edge(source="тэги Жизнь прекрасна ", label="тэг", target="про жизнь"))

# 26 - Зелёная миля
text = '''Пол Эджкомб — начальник блока смертников в тюрьме «Холодная гора», каждый из узников которого однажды проходит «зеленую милю» по пути к месту казни. Пол повидал много заключённых и надзирателей за время работы. Однако гигант Джон Коффи, обвинённый в страшном преступлении, стал одним из самых необычных обитателей блока.'''
kg_nodes_film.append(Node(id="Зелёная миля ",
                          label="Зелёная миля ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=WKKiIRbwLQY",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/b/b0/Green_mile_film.jpg"))

kg_edges_year_of_issue.append(Edge(source="Зелёная миля ", label="год выпуска", target="1999"))

kg_nodes_duration.append(Node(id="189", label="189 минут", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Зелёная миля ", label="продолжительность", target="189"))

kg_edges_country.append(Edge(source="Зелёная миля ", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Зелёная миля ", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Зелёная миля ", label="жанр", target="детектив"))
kg_edges_genre.append(Edge(source="Зелёная миля ", label="жанр", target="драма"))
kg_edges_genre.append(Edge(source="Зелёная миля ", label="жанр", target="фэнтэзи"))

kg_nodes_place.append(Node(id="26", label="26", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Зелёная миля ", label="место в рейтинге", target="26"))
kg_edges_type.append(Edge(source="Зелёная миля ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Зелёная миля ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Зелёная миля ", label="тэг", target="тэги Зелёная миля "))

kg_edges_tags.append(Edge(source="тэги Зелёная миля ", label="тэг", target="тюрьма"))
kg_edges_tags.append(Edge(source="тэги Зелёная миля ", label="тэг", target="психологический"))
kg_edges_tags.append(Edge(source="тэги Зелёная миля ", label="тэг", target="убийство"))
kg_edges_tags.append(Edge(source="тэги Зелёная миля ", label="тэг", target="про жизнь"))

# 27 - Интерстеллар
text = '''Когда засуха, пыльные бури и вымирание растений приводят человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями.'''
kg_nodes_film.append(Node(id="Интерстеллар ",
                          label="Интерстеллар ",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=F6TU69adAzE",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/c/c3/Interstellar_2014.jpg"))

kg_nodes_year_of_issue.append(Node(id="2014", label="2014", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Интерстеллар ", label="год выпуска", target="2014"))

kg_edges_duration.append(Edge(source="Интерстеллар ", label="продолжительность", target="169"))

kg_edges_country.append(Edge(source="Интерстеллар ", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Интерстеллар ", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Интерстеллар ", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Интерстеллар ", label="жанр", target="научная фантастика"))

kg_nodes_place.append(Node(id="27", label="27", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Интерстеллар ", label="место в рейтинге", target="27"))
kg_edges_type.append(Edge(source="Интерстеллар ", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Интерстеллар ", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Интерстеллар ", label="тэг", target="тэги Интерстеллар "))

kg_nodes_tags.append(Node(id="апокалипсис", label="апокалипсис", color="#b0a9ab", size=10, shape="dot"))
kg_nodes_tags.append(Node(id="путешествия во времени", label="путешествия во времени", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Интерстеллар ", label="тэг", target="апокалипсис"))
kg_edges_tags.append(Edge(source="тэги Интерстеллар ", label="тэг", target="путешествия во времени"))
kg_edges_tags.append(Edge(source="тэги Интерстеллар ", label="тэг", target="антиутопия"))
kg_edges_tags.append(Edge(source="тэги Интерстеллар ", label="тэг", target="про космос"))

# 28 - 	Звёздные войны. Эпизод IV: Новая надежда
text = '''Татуин. Планета-пустыня. Уже постаревший рыцарь Джедай Оби Ван Кеноби спасает молодого Люка Скайуокера, когда тот пытается отыскать пропавшего дроида. С этого момента Люк осознает свое истинное назначение: он один из рыцарей Джедай. В то время как гражданская война охватила галактику, а войска повстанцев ведут бои против сил злого Императора, к Люку и Оби Вану присоединяется отчаянный пилот-наемник Хан Соло, и в сопровождении двух дроидов, R2D2 и C-3PO, этот необычный отряд отправляется на поиски предводителя повстанцев – принцессы Леи. Героям предстоит отчаянная схватка с устрашающим Дартом Вейдером – правой рукой Императора и его секретным оружием – «Звездой Смерти».'''
kg_nodes_film.append(Node(id="Звёздные войны. Эпизод IV: Новая надежда",
                          label="Звёздные войны. Эпизод IV: Новая надежда",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=WXgRuLvAMcw",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/8/87/StarWarsMoviePoster1977.jpg"))

kg_nodes_year_of_issue.append(Node(id="1977", label="1977", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="год выпуска", target="1977"))

kg_nodes_duration.append(Node(id="121", label="121 минута", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="продолжительность", target="121"))

kg_edges_country.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="28", label="28", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="место в рейтинге", target="28"))
kg_edges_type.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Звёздные войны. Эпизод IV: Новая надежда", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Звёздные войны. Эпизод IV: Новая надежда", label="тэг", target="тэги Звёздные войны. Эпизод IV: Новая надежда"))

kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод IV: Новая надежда", label="тэг", target="сражения"))
kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод IV: Новая надежда", label="тэг", target="война"))
kg_edges_tags.append(Edge(source="тэги Звёздные войны. Эпизод IV: Новая надежда", label="тэг", target="про космос"))

# 29 - 	Терминатор 2: Судный день
text = '''Прошло более десяти лет с тех пор, как киборг из 2029 года пытался уничтожить Сару Коннор — женщину, чей будущий сын выиграет войну человечества против машин.

Теперь у Сары родился сын Джон и время, когда он поведёт за собой выживших людей на борьбу с машинами, неумолимо приближается. Именно в этот момент из постапокалиптического будущего прибывает новый терминатор — практически неуязвимая модель T-1000, способная принимать любое обличье. Цель нового терминатора уже не Сара, а уничтожение молодого Джона Коннора.

Однако шансы Джона на спасение существенно повышаются, когда на помощь приходит перепрограммированный сопротивлением терминатор предыдущего поколения. Оба киборга вступают в смертельный бой, от исхода которого зависит судьба человечества.'''
kg_nodes_film.append(Node(id="Терминатор 2: Судный день",
                          label="Терминатор 2: Судный день",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=BbHU2X3k7tM",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/8/85/Terminator2poster.jpg"))

kg_edges_year_of_issue.append(Edge(source="Терминатор 2: Судный день", label="год выпуска", target="1991"))

kg_nodes_duration.append(Node(id="156", label="156 минута", color="#b0a9ab", size=10, shape="dot"))
kg_edges_duration.append(Edge(source="Терминатор 2: Судный день", label="продолжительность", target="156"))

kg_edges_country.append(Edge(source="Терминатор 2: Судный день", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Терминатор 2: Судный день", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Терминатор 2: Судный день", label="жанр", target="триллер"))
kg_edges_genre.append(Edge(source="Терминатор 2: Судный день", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Терминатор 2: Судный день", label="жанр", target="боевик"))

kg_nodes_place.append(Node(id="29", label="29", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Терминатор 2: Судный день", label="место в рейтинге", target="29"))
kg_edges_type.append(Edge(source="Терминатор 2: Судный день", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Терминатор 2: Судный день", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Терминатор 2: Судный день", label="тэг", target="тэги Терминатор 2: Судный день"))

kg_nodes_tags.append(Node(id="про роботов", label="про роботов", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tags.append(Edge(source="тэги Терминатор 2: Судный день", label="тэг", target="про роботов"))
kg_edges_tags.append(Edge(source="тэги Терминатор 2: Судный день", label="тэг", target="сражения"))

# 30 - 	Назад в будущее
text = '''Подросток Марти с помощью машины времени, сооружённой его другом-профессором доком Брауном, попадает из 80-х в далекие 50-е. Там он встречается со своими будущими родителями, ещё подростками, и другом-профессором, совсем молодым.'''
kg_nodes_film.append(Node(id="Назад в будущее",
                          label="Назад в будущее",
                          title=text,
                          size=25,
                          link="https://www.youtube.com/watch?v=FXfQYmVzNnc",
                          shape="image",
                          image = "https://upload.wikimedia.org/wikipedia/ru/9/90/BTTF_DVD_rus.jpg"))

kg_nodes_year_of_issue.append(Node(id="1985", label="1985", color="#b0a9ab", size=10, shape="dot"))
kg_edges_year_of_issue.append(Edge(source="Назад в будущее", label="год выпуска", target="1985"))

kg_edges_duration.append(Edge(source="Назад в будущее", label="продолжительность", target="116"))

kg_edges_country.append(Edge(source="Назад в будущее", label="страна производства", target="США"))
kg_edges_original_language.append(Edge(source="Назад в будущее", label="оригинальный язык", target="английский"))

kg_edges_genre.append(Edge(source="Назад в будущее", label="жанр", target="приключение"))
kg_edges_genre.append(Edge(source="Назад в будущее", label="жанр", target="научная фантастика"))
kg_edges_genre.append(Edge(source="Назад в будущее", label="жанр", target="семейный"))

kg_nodes_place.append(Node(id="30", label="30", color="#b0a9ab", size=10, shape="dot"))
kg_edges_place.append(Edge(source="Назад в будущее", label="место в рейтинге", target="30"))
kg_edges_type.append(Edge(source="Назад в будущее", label="тип", target="фильм"))

kg_nodes_tag.append(Node(id="тэги Назад в будущее", color="#b0a9ab", size=10, shape="dot"))
kg_edges_tag.append(Edge(source="Назад в будущее", label="тэг", target="тэги Назад в будущее"))

kg_edges_tags.append(Edge(source="тэги Назад в будущее", label="тэг", target="путешествия во времени"))

# show all knowledge graph
kg_nodes = set(kg_nodes_film + kg_nodes_year_of_issue + kg_nodes_duration + kg_nodes_country + kg_nodes_original_language + kg_nodes_genre + kg_nodes_type + kg_nodes_place + kg_nodes_tags + kg_nodes_tag)
kg_edges = set(kg_edges_year_of_issue + kg_edges_duration + kg_edges_country + kg_edges_original_language + kg_edges_genre + kg_edges_type + kg_edges_place + kg_edges_tags + kg_edges_tag)
#config = Config(width=2500, height=2500)
#return_value = agraph(nodes=kg_nodes, edges=kg_edges, config=config)