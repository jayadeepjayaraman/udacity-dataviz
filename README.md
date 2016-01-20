## Introduction
This data visualization exercise charts the on time performace of the top US airlines for a decade and also plots a chart to look at different reasons contributing to delay.

##Summary
I downloaded the data from [BTS] (http://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp), selecting a dataset that included all domestic flights from all carriers to and from major airports from June 2003 through December 2015. On performing an exploratory analysis of the data I found that the data is very detailed and has information for many airlines (20-25), therefore after an initial analysis I decided to plot the on time percentages for the top 5 airlines. 

Along with this I also plotted another line chart where in the trend for the different delay causes were plotted for the same time period.

##Design

###Understanding Data
The data I downloaded had the details for on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled and diverted flights is also part of the dataset and is maintained between 2 airports. 

I wanted to show the On time statistics for the airlines therefore I did an initial data wrangling in python where i created some summary files and used them as input to the chart.

Also, based on one of the feedback I massaged and transformed the data in such a way that I was able to get the summary statistics fo rthe different delay causes.

###Data Visualization (dimple.js)
I  evaluated the design decisions that I made during exploratory data analysis, and considered that a line chart was the best way to represent the trends of each airline over time. Coloring each line series was also a good way to visually encode and distinguish airlines from each other. 

After the feedback I introduced some interaction where when one hovers over the line for a specific airline a tool tip appears and the line also appears stronger than the other lines.

Finally, for the two charts I provided a filter where one clicks on the airline name or the delay cause then it disappears from the chart and clicking on it again will make the line re-appear.

##Feedback
####Feedback #1
On inteviewing one of my colleagues he mentioned that it would be nice if I could also plot a similar chart for different causes of delay. This would make the analysis and visualization complete and self explanatory. Therefore, I put another chart showing the different causes of delay and how they have changed over the last decade.

####Feedback #2
The second person I had interviewed mentioned that there was no interactivity in the charts 

####Feedback #3
The third person mentioned that it would be nice to filter based on airline names, i.e. if I clicked on the airline name the corresponding information should be the only one present on the screen


##Changes Implemented post feedback
Following the feedback from the 3 interviews, I implemented the following changes:

- I added a mouseover event for the lines, so it would 'pop' it out and emphasize the path. This would allow for better understanding of each individual airline's trend from 2003 to 2014.
- I subdued and muted the grid lines.
- I polished the tooltip variable names to be more natural.
- I introduced logic to filter the delay causes and airline names

