@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Unparser

import io::bibtex::Parser;
import Rascalware;

// TODO: check completeness, sort appropriately
list[str] good =
	["author","title","booktitle","year",
	"url","doi","numpages","publisher","series","acmid",
	"isbn","location","address","pages","keywords"];

public str bib2str(BibLib bl) = folds(bib2str,bl);

str bib2str(BibEntry be) =
	"@<be.kind>{<be.name>,
	'<for(k <- good, k in be.attrs){>\t<k> = <pp(be.attrs[k])>,
	'<}>}
	'";

str pp(quoted(BibString s)) = "\"<pp(s)>\"";
str pp(bracketed(BibString s)) = "{<pp(s)>}";
str pp(raw(str s)) = s;
str pp(bibseq(list[BibString] ss)) = folds(pp,ss);
default str pp(BibString s) = "<s>";