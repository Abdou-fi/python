import calendar
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

for m in range(1, 13):
    glass(calendar.month(2026, m))

year = int(input("Enter Year: ")) 
print(glass(calendar.calendar(year, 2, 1, 8, 3)))

