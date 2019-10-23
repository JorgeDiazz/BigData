#!/usr/bin/env python
# coding: utf-8

# In[228]:


#Encontrar la cantidad de preguntas bien escritas de posibles preguntas

import re

text_temp = "El artículo es la ¿palabra que acompaña? al ¿sustantivo? y siempre va delante de él. Es la palabra que funciona siempre como un determinante o identificador del sustantivo, esto es, señala si el sustantivo es conocido o no, e indica el género (femenino o masculino) y el número del sustantivo (singular o plural)"

result = re.findall(r".*?\?", text_temp)
result1 = map(lambda question: re.search(r"¿.*?\?", question).group(), result)

print(len(list(result1)))


# In[ ]:




