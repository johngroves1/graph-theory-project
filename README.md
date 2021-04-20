# Project: Graph Theory 2021

**Student ID:** G00367771

# Introduction
For this module I was tasked to write a program in the Python 3 programming language to search a text file using a regular expression. The program must take a regular expression and the name or path of the file as command line arguments and output the lines of the file matching the regular expression.

A README should be included with the following content: 

* A description of your repository and its contents pitched at a knowledgeable outsider.
* Instructions stating how to run and test your program.
* An explanation of your algorithm.
* Answers to each of the following three questions, up to 500 words each:
  * What is a regular expression?
  * How do regular expressions differ across implementations?
  * Can all formal languages be encoded as regular expressions?

# Research and Development
Before I started to code this project, I first looked back at the first few labs I did this semester. I wanted to make sure I had a good understanding of basic python syntax. In our first few labs we used examples of functions, variables, loops and if statements. I reinforced my understanding of this by reading through [tutorialspoints](https://www.tutorialspoint.com/python/python_basic_syntax.html) documentation on python syntax, which I found very helpful and easy to read through.

I then re-watched the [module video](https://web.microsoftstream.com/video/166bc23b-d814-42f6-90df-5748712026bc) on regular expressions making sure I had an understanding of what regular expressions are, how they are used and what each metacharacter meant. Regular expressions are essentially a sequence of characters that will specify a search pattern through a string. Metacharacters or known as 'operators' are characters with a unique meaning, from the previous labs I know I will be using the '|', '* ' and the '+' operator. The '|' character indicates zero or one occurence, for example 'a?bc' will match 'abc' and 'ac'. The '* ' character indicates zero or more occurrences, for example 'ab* c' will match 'ac' 'abc' abbc' and so on. The '+' character indicates one or more occurences, for example 'ab+c' will match 'abc, 'abbc, abbbc' and so on, but not 'ac'.

The first step I needed to take on the project was to convert the regular expression from infix notation to postfix notation, using the [Shunting Yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). Postfix notation removes the need for parentheses and allows the computer to read in expressions one symbol after another without the worry of operator precedence and parentheses during computation. An example of this would be an infix notation would be ((A * B)+(C | D)) and the postfix notation of this expression would be AB*+CD|. I found [this](http://www.cs.man.ac.uk/~pjj/cs212/fix.html#:~:text=Infix%2C%20Postfix%20and%20Prefix%20notations,operators%20that%20take%20two%20operands.&text=Operators%20are%20written%20in%2Dbetween%20their%20operands.) website very helpful for understanding and visualising the difference from infix notation to postfix notation. I knew from working on the Shunting Yard algorithm earlier in this semester that each operator had a different precedence, the precedence from highest to lowest are: * (Kleene star), . (concatentation) and the | (or) operator. Once I wrote the algorithm I tested with some default inputs and then matched it with this [infix to postfix converter](https://www.web4college.com/converters/infix-to-postfix-prefix.php) and it was a success.


# Description of repository

# Instructions on how to run and test program

# Explanation of your algorithm

# Answer Questions in own words up to 500 words

** What is a regular expression? **
** How do regular expressions differ across implementations? **
** Can all formal languages be encoded as regular expressions? **
