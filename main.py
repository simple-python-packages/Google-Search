#Siz buni telegram botlarda qo'llashingiz mumkin
from googlesearch import search

enter = input('nima qidirmoqchisiz:')

for i in search(query=enter, tld='com',num=10,stop=10,pause=2):
    print(i)
    
#Github sahifamga obuna bo'ling va star bosing #xaxaxxa