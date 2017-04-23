from osmnodepbf import osmnodepbf
import os


parser = osmnodepbf.Parser("data/germany-latest.osm.pbf")

places = parser.parse({"place": {
    "suburb", "borough", "quarter", "city", "neighbourhood", "city_block", "town", "village", "hamlet",
    "isolated_dwelling", "farm", "allotments"}}, refresh=True)

f = file("data/germany-places.csv", "w")

for p in places:
    for t in p["tag"]:
        if t.keys()[0] == "name":
            nm = t["name"]
            break
    # ideally, filter out commas from names
    f.write(nm + "," + str(p["lon"]) + "," + str(p["lat"]) + os.linesep)

f.close()
