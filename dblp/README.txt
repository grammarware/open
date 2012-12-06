This directory contains the XML dump taken from DBLP:
	http://dblp.uni-trier.de/xml/
The data itself is distributed with an open data license ODC-BY:
	http://opendatacommons.org/licenses/by/1.0

The _everything.xml file is identical to dblp.xml, but preprocessed to be made self-contained: all SGML entities otherwise specified by dblp.dtd, are replaced with their Unicode counterparts.

DO NOT run 'make get' on your machine unless you want to sacrifice about 1 GB of network traffic and 4 hours or so on preprocessing. Otherwise, go ahead.

DO NOT run 'make clean' unless you managed to irreparably damage the XML files. Otherwise, go ahead.

Yours,
	Vadim Zaytsev aka @grammarware,
	http://grammarware.net
