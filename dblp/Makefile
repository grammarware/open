all:

extract:
	xsltproc --stringparam conf models filter.xslt _everything.xml > models.xml

get:
	wget http://dblp.uni-trier.de/xml/dblp.xml -O _everything.xml

clean:
	rm -rf *.xml

