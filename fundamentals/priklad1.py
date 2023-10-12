import requests

rq = requests.get("https://gutenberg.org/cache/epub/11/pg11.txt")
text_knihy = rq.text

#priklad 1 - pocet slov v stringu
print("Pocet slov v texte je: ",len(text_knihy.split(" ")))

#priklad 2 - pocet viet v stringu
print("Pocet viet v texte je: ",len(text_knihy.split(".")))

#priklad 3 - kde sa v knihe prvykrat nachadza slovo "Hatter"
index_of_Hatter = text_knihy.split(" ").index("Hatter")
print("Index slova Hatter je: ", index_of_Hatter)


#priklad 4 - kolko krat sa nachadza slovo "Hatter"
print("Slovo 'Hatter' sa v texte nachadza: ", text_knihy.count("Hatter"), "krat")

#priklad 5 - vypisat 361. - 474. slovo z knihy tak, aby zacinalo velkym pismenok
print("361.slovo je: ",text_knihy.split(" ")[360].capitalize())
print("474.slovo je: ",text_knihy.split(" ")[473].capitalize())
print("Text pri 361. az 474. slove: ", " ".join(text_knihy.split(" ")[360:474]).capitalize())


#priklad 6 - vypiste prvych 9 slov z knihy
#pri text_knihy.split() nam rozdeli text na pole pricom kazde slovo predstavuje jednotlivy prvok, pri " ".join() sa pole zluci do jedneho stringu
print("\nPrvych 9 slov z knihy je: "," ".join(text_knihy.split()[:9]))

#priklad 7 - poslendych 10 slov z knihy
last_10_words = " ".join(text_knihy.split()[-10:])
print("Poslednych 10 slov:", last_10_words)

