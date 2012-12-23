@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Access

import io::bibtex::Parser;
import Rascalware;

public str gimmeStr(BibEntry e, str key) = gimmeStr(e.attrs[key]);
public str gimmeStr(quoted(BibString s)) = gimmeStr(s);
public str gimmeStr(bracketed(BibString s)) = gimmeStr(s);
public str gimmeStr(raw(str s)) = s;
public str gimmeStr(bibseq(list[BibString] ss)) = folds(gimmeStr,ss);
public default str gimmeStr(BibString s) = "<s>";
