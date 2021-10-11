import wikipedia

def __init__():
    wikipedia.set_lang('pt')


def search(text):
    __init__()
    return wikipedia.search(f'extensão {text}', results=1)


def bring_summary(url):
    summary = wikipedia.summary(url, sentences=2)
    return summary