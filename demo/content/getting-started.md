Title: Getting Started with Progem
Date: 2022-04-29 22:00
Tags: getting started, progem, how to
Slug: getting-started-with-progem
Authors: Progem
Feature_Image: images/light_times_square.jpg
Summary: Some simple instructions on how to get started with Progem.

Photo by [darknessgamer739](#) on [wallpaper.com](https://www.wallpaperup.com/1101096/light_times_square.html)

## Progem

An elegant and responsive theme for Pelican Static Site generator.
<br>See a demo at: [progem.spydermaxi.com](#)

This is a serious adaption from [Attila Ghost Theme](https://github.com/zutrinken/attila).
<br>See a demo at: [attila.peteramende.de](https://attila.peteramende.de/)

## 📷 Screenshot

<img src="https://raw.githubusercontent.com/spydermaxi/pelican-progem/main/screenshots/Progem_light.png" />

<img src="https://raw.githubusercontent.com/spydermaxi/pelican-progem/main/screenshots/Progem_dark.png" />

## 💻 ➡️ 📱 Responsive

<img src="https://raw.githubusercontent.com/spydermaxi/pelican-progem/main/screenshots/Responsive_menu.png" />

## ⭐️ Features

* Theme options
* Responsive layout
* Light and Dark Mode
* Search & Popular Tags
* Code highlight including line numbers

## 📥 Install Progem theme

First, choose a location to hold your themes. For this example, we'll use the directory ~/pelican-themes/progem, but yours could be different. Clone the pelican-themes repository to that location on your local machine:

```bash
git clone https://github.com/spydermaxi/pelican-progem ~/pelican-themes/progem
```

Now you should have **Progem** repository stored at ``~/pelican-themes/progem``.

To use one of the themes, edit your Pelican settings file (``pelicanconf.py``) to include this line:

```python
THEME = "/home/user/pelican-themes/progem"
```


## ⚙️ Setup Pelican Plugins

### Plugins requirements

1. [Neighbor Articles: A Plugin for Pelican](https://github.com/pelican-plugins/neighbors) - Neighbors is a Pelican plugin that adds Next/Previous links to articles.

    **Installation** - Simply activate your environment and install via:
    ```bash
    python -m pip install pelican-neighbors
    ```

    **Usage** - The theme uses the ``prev_article`` and ``next_article`` variables to create links in article page in jinja templating. No configuration required from you.

2. [Image Process: A Plugin for Pelican](https://github.com/pelican-plugins/image-process) - Image Process also makes it easy to create responsive images using the HTML5 srcset attribute and <picture> tag. It does this by generating multiple derivative images from one or more sources.

    **Installation** - Simply activate your environment and install via:
    ```bash
    python -m pip install pelican-image-process
    ```

    **Usage** - Add the following codes into ``pelicanconf.py`` file to enable responsive srcset images
    ```python
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
    ```

## 🕹️ Setup Custom variable in ``pelicanconf.py``

Additional variables that the theme uses:

1. **Theme**
```python
# Example directory of progem
THEME = "/home/user/pelican-themes/progem"
```
2. **Site Subtitles**
```python
SITESUBTITLE = 'An elegant responsive theme for pelican-progem'
```
3. **Social Widgets**
```python
# Social widget should be in tuple format ('social-name', 'social-website') #
SOCIAL = (('github', 'http://github.com/spydermaxi/pelican-progem'),
          ('facebook', 'https://facebook.com'),
          ('instagram', 'https://instagram.com'),
          ('youtube', 'https://youtube.com'))
```

## 🔠 Setup custom google fonts

1. Go to [fonts.google.com](https://fonts.google.com/) and choose a font.
2. Choose __Embed__ and copy the `<link>` code.
3. Go to __Code injection__.
4. Add this to __Blog Header__:
````html
<link href="https://fonts.googleapis.com/css2?family=Mukta&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text&display=swap" rel="stylesheet">
<style>
  :root {
    --font-primary: 'Mukta', sans-serif;
    --font-secondary: 'Crimson Text', serif;
  }
</style>
````

## ✍🏼 Writing content

Each article allows the author to include a cover image.

To add the image simply add the ``Feature_Image`` meta data at the top of the article like so:

```
Feature_Image: images/light_times_square.jpg
```

The ``images/loght_time_square.jpg`` is where you store the original image in your ``content/images/`` directory/folder

Here's how it looks like in the article:

```
Title: Getting Started with Progem
Date: 2022-04-30 22:00
Tags: getting started, progem, how to
Slug: getting-started-with-progem
Authors: Progem
Feature_Image: images/light_times_square.jpg
Summary: Some simple instructions on how to get started with Progem.
```

<img src="https://raw.githubusercontent.com/spydermaxi/pelican-progem/main/screenshots/Coverimage_sample.png" />

## ⚖️ Copyright & License

Copyright (C) 2022 Adrian Loo - Released under the [MIT License](https://github.com/spydermaxi/pelican-progem/blob/main/LICENSE).
