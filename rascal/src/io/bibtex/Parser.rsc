@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Parser

//import Rascalware;
import io::bibtex::Syntax;
import ParseTree;
import String;
import List; // size
import IO;

alias BibLib = list[BibEntry];
alias BibAttrs = map[str,BibString];
alias BibEntry = tuple[str kind, str name, BibAttrs attrs];
data BibString
	= raw(str s)
	| quoted(BibString bs)
	| bracketed(BibString bs)
	| bibseq(list[BibString])
	;

public BibLib loc2bib(loc l) = str2bib(readFile(l));
BibLib str2bib(str s) = library2list(parse(#BibLibrary,trim(s)));

//BibLib library2list(BibLibrary b) = mapc2a(mapEntry,b.es);
BibLib library2list(BibLibrary b) = [mapEntry(e) | OneBibEntry e <- b.es];

BibEntry mapEntry(OneBibEntry e) = <"<e.kind.name>","<e.name>",mapKVs(e.pairs)>;

BibAttrs mapKVs({BibPair ","}+ ps) = ("<p.key>":mapStr(p.val) | BibPair p <- ps);

BibString mapStr((BibValue)`<BibValueQ v>`) = quoted(mapStrQ(v));
BibString mapStr((BibValue)`<BibValueC v>`) = bracketed(mapStrC(v));
default BibString mapStr(BibValue v) = raw("<v>");

BibString mapStrQ(BibValueQ v) = normalise([mapQEl(e) | BQElement e <- v.es]);

BibString mapQEl((BQElement)`<BibValueC c>`) = bracketed(mapStrC(c));
default BibString mapQEl(BQElement e) = raw("<e>");

BibString mapStrC(BibValueC v) = normalise([mapCEl(e) | BCElement e <- v.es]);

BibString mapCEl((BCElement)`<BibValueC c>`) = bracketed(mapStrC(c));
default BibString mapCEl(BCElement e) = raw("<e>");

BibString normalise(list[BibString] bs)
{
	bs2 = innermost visit(bs)
	{
		case [*L1,raw(str s1),raw(str s2),*L2] => [*L1,raw(s1+s2),*L2]
	};
	if (size(bs2)==1)
		return bs2[0];
	else
		return bibseq(bs2);
}



// TODO will be useful later for checking unparser completeness
public void do()
{
	list[str] allkeys = [];
	for(BibEntry b <-loc2bib(|home:///workspace/bibtex/icse2010.bib|), str x <- b.attrs)
		if (x notin allkeys)
			allkeys += x;
	iprintln(allkeys);
}

