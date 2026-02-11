import matplotlib.pyplot as pl
labaels = ["Python", "Scala", "C#", "Java", "PHP"] 
index= [0, 1, 2, 3, 4] #provide location on x axis
sizes= [45, 10, 15, 30, 22] #provide size of each bar

#set up tha bar chart
pl.bar(index, sizes, tick_label=labaels,
       color=('red', 'red', '#030303','yellow', 'orange'), width=0.2)

#configure the layout
pl.title("Programming Languages Popularity")
pl.xlabel("Languages")
pl.ylabel("Popularity")

#show the plot 
pl.show()
