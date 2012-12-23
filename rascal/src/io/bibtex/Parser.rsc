@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Parser

import io::bibtex::Syntax;
import ParseTree;
import String;
import IO;

alias BibLib = list[BibEntry];
alias BibEntry = tuple[str kind, str name, map[str,str] attrs];

public BibLib loc2bib(loc l) = str2bib(readFile(l));
BibLib str2bib(str s) = library2list(parse(#BibLibrary,trim(s)));

BibLib library2list(BibLibrary b) = [mapEntry(e) | OneBibEntry e <- b.es];

BibEntry mapEntry(OneBibEntry e) = <"<e.kind.name>","<e.name>",mapKVs(e.pairs)>;

map[str,str] mapKVs({BibPair ","}+ ps) = ("<p.key>":"<p.val>" | BibPair p <- ps);

public void main()
{
	loc2bib(|home:///workspace/zaytsev.bib|);
} 