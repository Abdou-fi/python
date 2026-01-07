from text_functions import arabic_display

text1 = "مرحبا بالعالم"
text2="Python رائع"
print(arabic_display(text1))
print(arabic_display(text2))


def arabic_display(text):
    import arabic_reshaper
    from bidi.algorithm import get_display       # https://pypi.org/project/python-bidi/         pip install python-bidi

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text