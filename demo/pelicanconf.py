AUTHOR = 'Adrian Loo'
SITENAME = 'Progem'
SITEURL = 'http://127.0.0.1:8000'
SITESUBTITLE = 'An elegant responsive theme for pelican-progem'

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/spydermaxi/pelican-progem'),
          ('linkedin', 'https://linkedin.com/adrian-loo-spydermaxi'))

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = '…'
DISPLAY_CATEGORIES_ON_MENU = False

THEME = '../'

IMAGE_PROCESS = {
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
