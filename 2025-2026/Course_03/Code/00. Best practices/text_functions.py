# encoding: utf-8
def glass (text):
    lines = text.splitlines()
    w = max(len(l) for l in lines)
    print(chr(9581) + chr(9472) * (w+2) + chr(9582))
    for l in lines:
        print(chr(9474) + " " + l.ljust(w) + " " + chr(9474))
    print(chr(9584) + chr(9472) * (w+2) + chr(9583))

def arabic_display(text):
    import arabic_reshaper
    from bidi.algorithm import get_display

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

