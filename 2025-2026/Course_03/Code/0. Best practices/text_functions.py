def glass (text):
    lines = text.splitlines()
    w = max(len(l) for l in lines)
    print( "╭" + "─"*(w+2) + "╮" )
    # print(chr(9581)+chr(9472)*(w+2)+chr(9582))
    for l in lines:
        print( "│ " + l.ljust(w) + " │" )
        # print(chr(9474)+" "+l.ljust(w)+" "+chr(9474))
    print( "╰" + "─"*(w+2) + "╯" )
    # print(chr(9584)+chr(9472)*(w+2)+chr(9583))
    


