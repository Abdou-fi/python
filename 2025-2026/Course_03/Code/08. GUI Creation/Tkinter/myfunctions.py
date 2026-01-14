def file_path(filename : str) -> str:
    import os
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__) 
    print(script_dir)
    # Join it with the filename
    file_path = os.path.join(script_dir, filename)
    return file_path
    
def glass (text):
    lines = text.splitlines()
    w = max(len(l) for l in lines)
    print(chr(9581)+chr(9472)*(w+2)+chr(9582))
    # print( "╭" + "─"*(w+2) + "╮" )
    for l in lines:
        print(chr(9474)+" "+l.ljust(w)+" "+chr(9474))
        # print( "│ " + l.ljust(w) + " │" )
    print(chr(9584)+chr(9472)*(w+2)+chr(9583))
    # print( "╰" + "─"*(w+2) + "╯" )
    
def arabic_display(text):
    import arabic_reshaper
    from bidi.algorithm import get_display       # https://pypi.org/project/python-bidi/         pip install python-bidi

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text