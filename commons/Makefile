TIMESTAMP = 20121118

all:

extract:
	./filter.py commonswiki-${TIMESTAMP}-pages-articles-multistream-index.txt

get:
	wget http://dumps.wikimedia.org/commonswiki/${TIMESTAMP}/commonswiki-${TIMESTAMP}-pages-articles-multistream-index.txt.bz2
	bzip2 -d commonswiki-${TIMESTAMP}-pages-articles-multistream-index.txt.bz2

clean:
	rm -rf *.bz2 *-index.txt
