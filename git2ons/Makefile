all: 101repo.lst 101worker.lst turing.lst rascal.lst rascal-shell.lst rascal-eclipse.lst wlm.lst \
	grammarware.github.com.lst personal.lst work.lst conf.lst slps.lst sotesola.lst sowiki.lst acceptware.lst
	make up

%.lst: log2csv.py %.log
	./log2csv.py $*.log > $*.lst

%.log:
	cd ../../../../$*/ && git log > tmp.log
	mv ../../../../$*/tmp.log $*.log

sowiki.lst:
	cd ../../../../SoTeSoLa/wiki/ && git log > tmp.log
	mv ../../../../SoTeSoLa/wiki/tmp.log sowiki.log
	./log2csv.py sowiki.log > sowiki.lst

up:
	@./update.py slps.lst ../data/notebook/2012.xml 2012.slps.xml SLPS
	@./update.py turing.lst 2012.slps.xml 2012.turing.xml Turing
	@./update.py grammarware.github.com.lst 2012.turing.xml 2012.web.xml SLPS-Web
	@./update.py work.lst 2012.web.xml 2012.work.xml Work
	@./update.py sotesola.lst 2012.work.xml 2012.sotesola.xml SoTeSoLa
	@./update.py sowiki.lst 2012.work.xml 2012.sowiki.xml SoTeSoLaWiki
	@./update.py conf.lst 2012.sowiki.xml 2012.ruconf.xml RuConf
	@./update.py wlm.lst 2012.ruconf.xml 2012.wlm.xml WLM
	@./update.py acceptware.lst 2012.wlm.xml 2012.FINAL.xml AcceptWare
	@echo Please pretty-print 2012.FINAL.xml for diffing

diff:
	diff 2012.FINAL.xml ../data/notebook/2012.xml

clean:
	rm -f *.log *.lst
