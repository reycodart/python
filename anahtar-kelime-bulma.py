from rake_nltk import Rake
rake = Rake()

text = """İnsanın konuşacak kadar zekaya, ya da susacak kadar
akla sahip olmaması büyük bir talihsizliktir. - Stefan Zweig"""

rake.extract_keywords_from_text(text)
keyword= rake.get_ranked_phrases()
print(keyword)


