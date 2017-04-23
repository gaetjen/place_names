## Intro

I don't remember when or why, but at some point I asked myself "I wonder to what extent it is possible to know in which part of Germany you are, based only on the characteristics of nearby place names." Even just looking at a map, or traveling around Germany a bit, some rough patterns are pretty apparent: In Baden-Württemberg there are many cities ending in "-ingen" (Böblingen, Villingen-Schwenningen). In Berlin and Brandenburg you'll find places ending in "-ow" (Pankow, Rathenow). Other substrings, such as "dorf" (village), "burg" (castle) or "berg" (hill/mountain) are seemingly ubiquitous and not unique to a region.

Well, I've now gone ahead and created some relief maps for the density of places whose names contain certain substrings. They contain interesting insight into linguistic and geographic differences within Germany. Also, if you want to create a fictional German town, this data can give you an idea of what its name should be, based on where in Germany it is located!


## Methods

I downloaded OpenStreetMap data for Germany from Geofabrik and used a modified version of [lifeeth's osmnodepbf scripts](https://github.com/lifeeth/osmnodepbf) to extract the names and coordinates for all settlements. The extracted data can be found at [data/](data/). For the country and state borders I used data from Wolfram/Mathematica.

To estimate densities I calculated histograms and smoothed them with a Gaussian filter. To minimize biases due to different regions having different densities of named settlements I always normalized with the estimated prior density as shown below, which includes all places. For visualization I used Mathematica's builtin ReliefMap function. Due to the normalization in ReliefMap the height values from separate map images cannot be compared directly.

![all named places](pics/prior.png)

I haven't looked into why some areas have a much higher density of named places than other areas, but there is no obvious connection to population density. I suspect that it is either due to some data sets which were made freely available, or because of volunteers for openstreetmap being more active in those areas for whatever reasons.

A piece of border between Lower Saxony and Brandenburg is missing, because the data from Wolfram was in a stupid format and I couldn't be bothered to fix it.

Here is a collection of some of the more interesting results, more can be found at [pics/](pics/).

#### Some of the most common substrings

berg (hill/mountain)  
![](pics/bedeutung/häufig/berg.png)  

dorf (village)  
![](pics/bedeutung/häufig/dorf.png)  

haus (house)  
![](pics/bedeutung/häufig/haus.png)  

hof (farm)  
![](pics/bedeutung/häufig/hof.png)  

mühl (mill)  
![](pics/bedeutung/häufig/mühl.png)  


#### Variations on bach (brook/stream)

bach  
![](pics/bedeutung/bach/bach.png)

beck  
![](pics/bedeutung/bach/beck.png)

bek  
![](pics/bedeutung/bach/bek.png)


#### Variations on stadt (city, but originally, and depending on spelling, also place)

stadt  
![](pics/bedeutung/stadt/stadt.png)  

städt  
![](pics/bedeutung/stadt/städt.png)  

stätt  
![](pics/bedeutung/stadt/stätt.png)  

stedt  
![](pics/bedeutung/stadt/stedt.png)  

stett  
![](pics/bedeutung/stadt/stett.png)  


#### Various river and region names

allgäu  
![](pics/fluss/allgäu.png)  

harz  
![](pics/fluss/harz.png)

pfalz (palatinate)  
![](pics/fluss/pfalz.png)  

donau (Danube)  
![](pics/fluss/donau.png)  

neckar  
![](pics/fluss/neckar.png)  

rhein (Rhine)  
![](pics/fluss/rhein.png)  

ruhr  
![](pics/fluss/ruhr.png)  


#### Cardinal directions

nord (north)  
![](pics/ort/nord.png)  

süd (south)  
![](pics/ort/süd.png)  

west  
![](pics/ort/west.png)  

ost (east)  
![](pics/ort/ost.png)  


#### Relative positions

ober (upper)  
![](pics/ort/ober.png)  

mitte (middle)  
![](pics/ort/mitte.png)  

unter (lower)  
![](pics/ort/unter.png)  

vorder (front)  
![](pics/ort/vorder.png)  

hinter (behind)  
![](pics/ort/hinter.png)  


#### Variations on brunn (well or source)

brunn  
![](pics/quelle/brunn.png)  

bronn  
![](pics/quelle/bronn.png)  

born  
![](pics/quelle/born.png)  


#### tal and thal (valley)

tal  
![](pics/bedeutung/tal/tal.png)  

thal  
![](pics/bedeutung/tal/thal.png)  


#### Various, which all mean clearing

rath  
![](pics/bedeutung/rodung/rath.png)  

scheid  
![](pics/bedeutung/rodung/scheid.png)

rode  
![](pics/bedeutung/rodung/rode.png)  


#### Others

burg (castle)  
![](pics/bedeutung/burg.png)  

by (farm in northern Germany, in other parts (river) curve)
![](pics/bedeutung/by.png)  

hagen (enclosure)  
![](pics/bedeutung/hagen.png)  

heide (heath/heathen)  
![](pics/bedeutung/heide.png)  

heim (home)  
![](pics/bedeutung/heim.png)  

leben (legacy/heritage)  
![](pics/bedeutung/leben.png)  

torf (peat)  
![](pics/bedeutung/torf.png)

weiler (hamlet)  
![](pics/bedeutung/weiler.png)

ing  
![](pics/ing.png)  

ingen  
![](pics/ingen.png)  

itz  
![](pics/itz.png)  

oi  
![](pics/oi.png)  

ow  
![](pics/ow.png)  

tzsch  
![](pics/tzsch.png)  
