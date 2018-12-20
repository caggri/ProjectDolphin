import requests

def datamuse(clue, length = 3):

    # clue comes from
    query = clue.replace(" ", "+")
    query = query.lower()

    request = requests.get('https://api.datamuse.com/words?ml={}'.format(query))

    results = request.json()
    datamuse_words = []
    for result in results:
        datamuse_words.append(result['word'])

    datamuse_words = list(filter(lambda x: len(x) == length, datamuse_words))
    print("Datamuse Search \nWord Count: " + str(len(datamuse_words)))
    return datamuse_words

"""
search = "Hollywood Walk of Fame symbol"
length = 4
print(datamuse(search,length))
"""
