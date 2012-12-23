@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Access

import io::bibtex::Parser;
import util::Math;
import String;
import Rascalware;

public str gimmeStr(BibEntry e, str key) = gimmeStr(e.attrs[key]);
public str gimmeStr(quoted(BibString s)) = gimmeStr(s);
public str gimmeStr(bracketed(BibString s)) = gimmeStr(s);
public str gimmeStr(raw(str s)) = s;
public str gimmeStr(bibseq(list[BibString] ss)) = folds(gimmeStr,ss);
public default str gimmeStr(BibString s) = "<s>";

public tuple[int,int] gimmeRange(BibEntry e, str key) = gimmeRange(gimmeStr(e,key));
public tuple[int,int] gimmeRange(str s) = (/<i1:\d+>\s*\-\-?\s*<i2:\d+>/ := s)?<toInt(i1),toInt(i2)>:<0,0>;

public int gimmeInt(BibEntry e, str key) = toInt(gimmeStr(e,key));

