Title: Codeblock Demo in Markdown
Date: 2022-05-02 21:45
Tags: codeblocks, demo, syntax highlight, codehilite, markdown
Authors: Progem
Summary: This is a demonstration of codeblock syntax highlighting produced from Markdown file. Contents are writtent in markdown and published using Progem Theme and Pelican static site generator.

This demo was written in markdown to demonstration after content generatrion using Pelican.

# Python syntax highlighting

Standard python code lines

```python
# This is a comment
this_is_int_var = 123
this_is_string_var = "I'm a string"
this_is_boolean_var = True

this_is_list = [
'item1',
'item2',
'item3'
]

this_is_dictionary = {
"item1": "value1",
"item2": 2,
"item3": False
}
```

Function codes

```python
def this_is_a_function(*args, **kwargs) -> None:
 '''
 This is a docstring
 '''
 print("Hello World")

def func(x: float) -> int:
 return int(x)
```

Class code lines

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

## HTML syntax highlighting

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

## CSS syntax highlighting

```css
body {
 background-color: lightblue;
}

h1 {
 color: white;
 text-align: center;
}

p {
 font-family: verdana;
 font-size: 20px;
}
```

## BASH syntax highlight

```bash
git commit && git push
git commit || echo "Commit failed"
```

Another sample

```bash
NAME="John"
echo "Hi $NAME"  #=> Hi John
echo 'Hi $NAME'  #=> Hi $NAME
```
