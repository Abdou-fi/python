import re
text="the colour of the sky is blue and the color of the grass is green"
occurences_1=re.findall(r"colou?r", text)   # r stands for raw string, it tells python to ignore escape characters
print (occurences_1)    