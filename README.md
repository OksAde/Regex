# Principles of Programming

Task: Find how many times the word 'and' is in the book 'My Family and Other Animals'

## Logic

* Find the right pattern to match; in this case the word 'and' in the book

Procedure:
* Import the text file

* Read the file

* Define the pattern, which is the word 'and'

* Assign a count variable (initialize with 0) for counting the pattern

* Lowercase all the text (so that 'AND' and 'and' can be found and matched respectively)

* Iterate through the file and find the pattern while iterating

* Update the count variable suitably

* End iteration when the program meets the end of the book

## Data

* The text inside the pdf file of 'My Family and Other Animals' book

## Action

* Display the result (the total count of the word 'and')

## Pseudocode 

    import book_file
    read book_file
    pattern = "and"
    count_and = 0
    data = lowerCase(book_file)
    for line in data:  
      for word in line: 
        if data includes pattern:
          count = count + 1
    result = count


task: How to find a given name in a phonebook

## Logic

* Is the name found the correct match in the phonebook

Data

* the data inside of the phonebook

Action

* Display the correct name and corresponding phone number
