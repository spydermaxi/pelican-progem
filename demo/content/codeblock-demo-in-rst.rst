Codeblock Demo in reStructuredText
##################################

:date: 2022-05-02 21:45
:tags: codeblocks, demo, syntax highlight, codehilite, reStructuredText
:authors: Progem
:summary: This is a demonstration of codeblock syntax highlighting produced from reStructuredText file. Contents are writtent in reStructuredText and published using Progem Theme and Pelican static site generator.

This demo was written in reStructuredText to demonstration after content generatrion using Pelican.

Python syntax highlighting
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Standard code lines

   .. code-block:: python

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

2. Function code lines

   .. code-block:: python

      def this_is_a_function(*args, **kwargs) -> None:
          '''
          This is a docstring
          '''
          print("Hello World")

      def func(x: float) -> int:
          return int(x)

3. Class code lines

   .. code-block:: python

      class Person:
          def __init__(self, name, age):
            self.name = name
            self.age = age

      p1 = Person("John", 36)

      print(p1.name)
      print(p1.age)

HTML syntax highlighting
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: html

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

CSS syntax highlighting
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: css

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

BASH syntax highlight
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git commit && git push
   git commit || echo "Commit failed"

Another sample

.. code-block:: bash

   NAME="John"
   echo "Hi $NAME"  #=> Hi John
   echo 'Hi $NAME'  #=> Hi $NAME
