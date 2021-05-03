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

Now that I was comfortable that I had the logical side of the program completeted, I moved on to reading in a string from a text file as stated in the project brief. I went on w3schools to learn about file reading, after testing a file read of a single string. I added "The Odysses" by the famous greek author Homer, as my text file. I then wrote a function that would loop through each word in the text file and match with the entered expression, I added a counter that incremented anytime there was a match and populated an array with the matched text. I then went on to create a simple menu where the user can choose from a set of predfined expressions and matches or the choice to search their own expression through the textfile. Lastly I cleaned up my code and added any extra comments necessary.

# Instructions on how to run and test program
* On running the program, the user is presented with a menu where they can choose between a set of predefined expressions or they can enter an infix expression to search through the provided text file. ![alt text](https://github.com/johngroves1/graph-theory-project/blob/main/UserGuideImages/Menucmd.PNG)

* When the user enters '1' a set of predefined infix expressions and matching strings are printed to the console. ![alt text](https://github.com/johngroves1/graph-theory-project/blob/main/UserGuideImages/predefined.PNG)

* If the user enters '2' they are prompt to enter an infix expression to search through the text file. The algorithm will break if the user enters two characters without concatenation or if the syntax of the expression is wrong. In the example below the user entered the expression ((b.e.d)|(r.o.o.m)) to match all words of bed and room.![alt text](https://github.com/johngroves1/graph-theory-project/blob/main/UserGuideImages/EnteredExpression.PNG)

* When the user enters an expression to search through the text file, each word in the novel "The Odysses" is matched to the input. All words that do match with the inputted expression are outputted to a list and a counter displays how many words matched. ![alt text](https://github.com/johngroves1/graph-theory-project/blob/main/UserGuideImages/MatchingOutput.PNG)

* If the users enters a wrong number in the menu they are prompt to enter a valid number again, if the user wishes to exit the program they can enter '3'.

# Explanation of your algorithm

### Infix to postfix conversion using the Shunting Yard Algorithm:
 * The algorithm loops through the expression one character at a time. If the input is a letter or number, append directly to the output queue.
 * If the input is an operator, push to operator stack. If an operator already exists on top of the operator stack with higher or equal precedence than the current input symbol, remove the operator from the top of the stack and append it to the output queue. Repeat until the current operator input has a higher precedence than the operator on the stack or until the stack is empty.
 * If the input is '(' append it to operator stack
 * If the input is ')' pop all operators from the stack and append to the output queue, pop the left bracket from the stack and discard both brackets
 * If any operators are left in the stack add too the output queue.

### Thompsons construction algorithm 
This algorithm works by reading in the postfix expression and splitting each operator into a smaller expression, from which an NFA is constructed using that operators set of rules. Each NFA has a start state and end state, when the nfa reaches the end state it is added to an overall NFA stack. Below are how each operator works in the algorithm
* ### Concatenation '.'
  Creates two NFA's where the first NFA's accept state is the second NFA's start state which connects both NFA's and pushes to the NFA stack.
  
* ### Or '|'
  Creates two NFA's and pops of the stack, creates a new start state and accept state. Makes a new start state point at the old start states and makes the old accept states non-  accept. Using the 'e' arrows, to point the old accept states of both NFA's to a new accept state and push to the NFA stack.
  
 * ### Kleene Star '*'
 Pop one NFA off the stack and create a new start and end state. Using the 'e' arrows to point the new start state to the old start state of the NFA. Create another 'e' arrow to the new accept state and set the 'e' arrow of the initial accept state back to the initial state of the NFA which allows for repetition of the expression. 
 
### Matching Algorithm
The Match algorithm checks to see if the converted infix expression matches with the given string of text. It first calls the shunting algorithm to convert the entered expression to postfix and then passes the postfix expression through the thompsons algorithm. It creates a set of all previous states that the expression is still in and the set of current states that it will be in. It then it loops through the string a character at a time in the current set to check if the set contains the characters of the expression, if so it adds the next state and makes the previous set equal to the current set and loop through again. At the end of the current set if all characters are in the accept state then the function returns true and the enterted expression matches with the String of text, if not it returns false and the String does not match with any of the expressions NFA.

### fileread()
Reads in the text file "input.txt" which contains the novel "The Odysses". Loops through the text file reading in word by word and matching each word to the entered infix expression returning all words True or False. It also counts how many words matched in the search and outputs the count and the matched words to a list. 

# Answer Questions in own words up to 500 words

### What is a regular expression?
A regular expression is a string of text that allows you to create a search pattern for matching, locating and managing text. Strings of text can be compared to the pattern in order to identify strings that match the logical pattern defined by the regular expression. Regular expressions emerged in the 1950s as a way to describe regular languages in mathematics, they began to show up in the programming world in the 1970s mainly due to Ken Thompson who built the Thompsons construction as a means to match patterns in a text file. Regular expressions are very useful and a powerful tool for companies and developers, they are used today in search engines, text editors, programming languages and much more. 

A regular expression is a combination of literal characters that represent themselves and operators which have a logical meaning to them. Each operator character has a different logical meaning to them, an example of some are the concatenation operator which are used  to indicate a series of characters, the or operator for one set of characters or another and the kleene star operator which indicates zero or more times. There are a lot more operator characters used in regular expressions, all of which have a unique logical meaning to them. On their own, each operator is somewhat useful, however the combination of these operators can create a very powerful pattern. The use of these characters means a regular expression can search for a very specific string in a huge range of data, a great example of this would be this regular expression: ^[A-Z0-9.%+-]+@[A-Z0-9.-]+.[A-Z]{2,}$. This regular expression can be used for checking if a given set of strings are an email address or not, it would return any email address from just this one line of code. As you can see regular expressions are hugely beneficial for both developers or anyone who wishes to identify strings or patterns in any given text.

### How do regular expressions differ across implementations? 
The main difference in regular expressions across implementations are the way special characters are handled. Some implementations differ slightly by the way they handle line breaks and some differ significantly by the way they handle syntax and operator behaviour. Each programming language operators work slightly differently to each other, an example of this would be that in Python, regular expressions, the * and + operator are classified as greedy, that is they match as much text as possible, while in UNIX-like systems such as Linux the regular expressions would have to be more specific. A simpler example of different implementation would be regular expressions in word processing programs often arent as extensive or as robust with wider practice as what you would find in programming language context such as java or perl.

On doing research of this question I learned about POSIX "Portable Operating Systems Interface for uniX" which are a collection of standards that define some of the functionality that a UNIX operating system should support. Part of the collection of standards is the basic regular expressions BRE, which follows a set standard where most operators require a backslash to give the operator its logical meaning. This standard is quite old and was defined in 1986, regular expressions have come a long way since then, another commonly used standard today is the extended regular expressions ERE. In this group only bracket expressions, dot, caret, dollar and star operators work, so using backslash in this implementation of regular expression wont work. Most implementations use either POSIX BR or ERE but some have their own designed regular expression rules. There are other styles powerful regular expression Implementation , such as the RE2, a software library for regular expressions implemented and used by Google. RE2 has very predictable run-time and a maximum memory allotment, which makes it suitable for use in server side applications where memory and time are crucial. Google uses this library for Gmail, Google Documents and Google Sheets.

So in conclusion to the question, regular expressions differ across implementations by the logic of operators and the standards they use. Regular expressions are implemented in a huge number of softwares, libraries and technologies. All of which follow a slighly different set of rules and standards.

### Can all formal languages be encoded as regular expressions?
