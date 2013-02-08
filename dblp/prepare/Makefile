all:

pc.all:
	cat ../_everything.xml | grep '\<inproceedings\>' | grep 'key="conf/' | sed 's/.* .* key="\(.*\)".*/\1/' > pc.all

pj.all:
	cat ../_everything.xml | grep '\<article\>' | grep 'key="journals/' | sed 's/.* .* key="\(.*\)".*/\1/' > pj.all


e.all:
	cat ../_everything.xml | grep '<url>db/conf/' > tmp.all
	cat ../_everything.xml | grep '<ee>db/conf/' >> tmp.all
	cat tmp.all | sed 's/<.*>db\/\(.*\)\.html.*<\/.*>/\1/' | sort | uniq > e.all

i.all:
	cat ../_everything.xml | grep '<url>db/journals/' > tmp.all
	cat ../_everything.xml | grep '<ee>db/journals/' >> tmp.all
	cat tmp.all | sed 's/<.*>db\/\(.*\)\.html.*<\/.*>/\1/' | sort | uniq > i.all

v.all:
	cat e.all | sed 's/\(conf\/.*\)\/.*/\1/' | sort | uniq > v.all

j.all:
	cat i.all | sed 's/\(journals\/.*\)\/.*/\1/' | sort | uniq > j.all
