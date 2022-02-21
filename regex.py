# https://colab.research.google.com/drive/1_WFtAh8dYqkdd2zezK_vZKKAB6KlJLHP?usp=sharing

pip install tika
import re # regular expressions

from tika import parser # pip install tika

# opening pdf file
parsed_pdf  = parser.from_file('MY_FAMILY_AND_OTHER_ANIMALS_Gerald_Durre.pdf')

# grab the content of the pdf file object
data = parsed_pdf['content'] 

print(type(data))
print(data)

# lowecase all string
data = data.lower()

# define the pattern 
pattern = 'and' 

# define the way you want to match the pattern with the text
match = re.findall(pattern, data)
print(len(match))
