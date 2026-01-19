import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def wiki_search(query):
    try:
        return wikipedia.summary(query, sentences=2)

    except DisambiguationError as e:
        # Pick the first suggested option
        try:
            return wikipedia.summary(e.options[0], sentences=2)
        except:
            return "Your query was ambiguous. Please be more specific."

    except PageError:
        return "No Wikipedia page found for this topic."

    except Exception:
        return "Sorry, I couldn't fetch information right now."
