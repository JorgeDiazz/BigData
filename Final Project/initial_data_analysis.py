# Find the correct questions number, which contains '¿' and '?' characters

import re

text_to_evaluate = "El artículo es la ¿palabra que acompaña? al ¿sustantivo? y siempre va delante de él. Es la palabra que funciona siempre como un determinante o identificador del sustantivo, esto es, señala si el sustantivo es conocido o no, e indica el género (femenino o masculino) y el número del sustantivo (singular o plural)"

english_question_regex = r".*?\?"
spanish_question_regex = r"¿.*?\?"

possible_questions = re.findall(english_question_regex, text_to_evaluate)
correct_questions = len(map(lambda question: re.search(spanish_question_regex, question).group(), possible_questions))

print(list(correct_questions))
