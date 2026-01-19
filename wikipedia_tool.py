import wikipedia

def wiki_search(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "Sorry, I couldn't find that on Wikipedia."
