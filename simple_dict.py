from gettext import translation

d = {}
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["three"])
print(f"i know {len(eng_to_spa)} spanish words")
sentence = "i am cuban"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+" "
print(f"{sentence} translate to: {translation}")
print(list(eng_to_spa.keys()))
print(list(eng_to_spa.values()))
eng_to_spa.pop("pineapple")
eng_to_spa.

if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("i dont know this world")

print(eng_to_spa.get("car", "sorry dont know"))
eng_to_spa.setdefault(("one", "sorry dont know"))
eng_to_spa.setdefault("monkey", "sorry dont know")
print(eng_to_spa)
