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

I then re-watched the [module video](https://web.microsoftstream.com/video/166bc23b-d814-42f6-90df-5748712026bc) on regular expressions making sure I had an understanding of what regular expressions are, how they are used and what each metacharacter meant. Regular expressions are essentially a sequence of characters that will specify a search pattern through a string. Metacharacters or known as 'operators' are characters with a unique meaning, from the previous labs I know I will be using the '|', '* ' and the '.' operator. The '|' character indicates zero or one occurence, for example the string 'a|b' will match  'a' or 'b' but not 'ab'. The '.' character which is concatenation, indicates a series of characters for example the string 'ab.' will match with 'ab'. Lastly the '* ' character indicates zero or more occurrences, for example 'ab* c' will match 'ac' 'abc' abbc' and so on.

The first step I needed to take on the project was to convert the regular expression from infix notation to postfix notation, using the [Shunting Yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). Postfix notation removes the need for parentheses and allows the computer to read in expressions one symbol after another without the worry of operator precedence and parentheses during computation. An example of this is would be an infix expression of (A.B|B*) and the postfix notation of this expression would be AB.B*|. I found [this](http://www.cs.man.ac.uk/~pjj/cs212/fix.html#:~:text=Infix%2C%20Postfix%20and%20Prefix%20notations,operators%20that%20take%20two%20operands.&text=Operators%20are%20written%20in%2Dbetween%20their%20operands.) website very helpful for understanding and visualising the difference from infix notation to postfix notation. I knew from working on the Shunting Yard algorithm earlier in this semester that each operator had a different precedence, the precedence from highest to lowest are: * (Kleene star), . (concatentation) and the | (or) operator. Once I wrote the algorithm I tested with some default inputs and it was a success.

After implementing Shunting Yards algorithm, the next step will be to transform the postfix regular expression into a nondeterministic finite automaton using the Thompson's construction. An algorithm created by Ken Thompson, a pioneer in computer science. Thompsons algorithm reads in a postfix expression and passes in one character at a time into a smaller NFA. As the entire expression is passed through the algorithm, it builds into a larger NFA, depending on what operator is passed into the NFA the outcome is different. On doing research on thomsons algorithm I found this [website](http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html) which really demonstrates what each operator does in terms of the NFA. Referencing this page and looking back at the previous lecture content helped me to fully understand the code that I have written. There was no real way for me to test this algorithm as the NFA returns a memory address, however using the last lab video on April 15th as guidance I was able to create a function that could determine if a set of characters would pass through the NFA and returning "True" if the set ends in an accept state or otherwise "False".

Now that I was comfortable that I had the logical side of the program completeted, I moved on to reading in a string from a text file as stated in the project brief.








# Description of repository

# Instructions on how to run and test program

# Explanation of your algorithm

# Answer Questions in own words up to 500 words

** What is a regular expression? **
** How do regular expressions differ across implementations? **
** Can all formal languages be encoded as regular expressions? **
