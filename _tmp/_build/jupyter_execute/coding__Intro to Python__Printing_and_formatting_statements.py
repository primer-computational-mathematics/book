(printing_intro)=
# Printing and formatting statements
``` {index} Python basics
```
## General

(basic_printing)=
### Printing text
A line of code in Python is a _statement_:

    print("Hellow world!")
    
_print_ is a function in Python that takes an argument in brackets () and prints it out to the terminal.

print("Hello world!")

_print_ function can also print multiple lines, using '\n' as a line separator in your text. Notice that you do not need to add spaces around '\n' in the text:

print("Hello world!\nThis is my first code.\nI love coding.")

Multiple lines can be also achieved by triple apostrophe """text""":

print("""Hellow world! 
This is my first code.
    I love coding.""") # This # is a comment that has no effect on code

# Note how added spaces in the last line are reflected in the printed statement

### Printing numbers
Apart from words, _print_ function can also take numbers and do some calculations:

print("10")     # Print text '10'
print(10)       # Print number 10
print(10+5-3)   # Calculate 10+5-3
print(10*5+3/2) # Multiply wiht *, divide with /
print(10**3)    # To take powers, use **, here 10 to de power of 3

# Finally more difficult calculation, brackets matter in order of calculation!!

print(5.0*0.6+(100.0+15)/5.0) # With brackets
print(5.0*0.6+100.0+15/5.0)   # Without brackets

(formatted_printing)=
## Formatted printing
``` {index} Formatted printing
```
Sometimes we want to insert certain texts or numbers into _print_ statemtens.

Inserting:
* use '%s' in the statement where you want to insert text
* use '%g' in the statement where you want to insert numbers, Python decides here how many significant figures are needed
* use '%.xf', where x is a number of significant figures you want displayed for your number

The syntax (coding rules) for inserting numbers/text into _print_ statement is:

    print("Text %s text text text" % ("text"))
    
An example below:

# Print your name and age inserted into text

print("My name is %s and I am %g years old." % ("<insert your name>", 18))

# Work out your height in meters, provided you are 5 ft 4 in and insert into text
# 1 foot = 0.3048
# 1 inch = 0.0254

print("I am %.2f m tall." % (5*0.3048+4*0.0254))

### Format() method:
This method allows to specify positions of the objects we want to insert into a string. For example:

print("I like {0} and {1}.".format('dinosaurs', 'brachiopods'))
print("I like {1} and {0}.".format('dinosaurs', 'brachiopods'))

We can also specify a variable name that will go into the string:

print("I like {0}, {1} and {other}.".format('dinosaurs', 'brachiopods', other = 'ammonites'))

Apart from strings, we can also insert numbers:

print("This fossil is {0:d} cm long and {1:.2f} cm wide.".format(12, 5.05))
print("This fossil is {0:g} cm long and {1:.4f} cm wide.".format(12.0, 5.05))
print("This fossil is {0:g} cm long and {1:8.4f} cm wide.".format(12.0, 5.05))

Both methods are valid so you can use whichever one suits you better!

(printing_exercises)=
### Exercises

1) **Print the following:**

Veni vidi vici



2) **Print the following:**

First line

Second line

Third line

         BOOM!
    
**HINT**: There is a '\t' character which works like tab



3) Some characters in printing statements can be a bit tricky to handle. Think about the following:

_"John is a great fan of Shakespeare, so he decided to reference the famous "Be of not the be?" from 'The Hamlet' is his latest essay"_

This is makes the Python parser confused. We need to use the backslash e.g. "\'" to make things specific. **Print the sentence from the example.**



4) **Printing can be art!** Use some characters to show your creativity! Try a triangle for example:


<pre>
     /\  
    /  \
   /    \  
  /      \  
  --------



**HINT**: What about printing the backslash?

If you want more, google ASCII art, people can really go insane with those...

<pre>
        __  _-==-=_,-.
        /--`' \_@-@.--<
        `--'\ \   <___/.  
             \ \\   " /  
              >=\\_/`<
  ____       /= |  \_|/
_'    `\   _/=== \___/
`___/ //\./=/~\====\
    \   // /   | ===:
     |  ._/_,__|_ ==:        __
      \/    \\ \\`--|       / \\
       |    _     \\:      /==:-\
       `.__' `-____/       |--|==:
          \    \ ===\      :==:`-'
          _>    \ ===\    /==/
         /==\   |  ===\__/--/
        <=== \  /  ====\ \\/
        _`--  \/  === \/--'
       |       \ ==== |
        -`------/`--' /
                \___-'
