from jinja2 import Template


menu = [
    {'href': 'index', 'title': 'Главная'},
    {'href': 'news', 'title': 'Новости'},
    {'href': 'about', 'title': 'О компании'},
    {'href': 'shop', 'title': 'Магазин'},
    {'href': 'contacts', 'title': 'Контакты'}
]

link = """<ul>
{% for m in menu -%}
{% if m.title == 'Главная' -%}
<li><a href="/{{ m['href'] }}" class="active">{{ m['title'] }}</a></li>
{% else -%}
<li><a href="/{{ m['href'] }}">{{ m['title'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(menu=menu)
print(msg)