#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date

dataInicio = date.fromisoformat('2020-01-26')

print(dataInicio)
print(type(dataInicio))

Mudou = dataInicio.strftime('%d/%m/%y')
print(Mudou)
print(type(Mudou))

