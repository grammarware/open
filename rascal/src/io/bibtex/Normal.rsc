@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Normal

import Rascalware;
import io::bibtex::Unparser;
import io::bibtex::Parser;
import io::bibtex::Access;
import String;
import IO;

list[str] dontcap = ["a","an","and","as","at","but","by","for","from","in","into","nor","of","on","or","over",
"per","the","to","upon","vs.","vs","with"];


BibEntry normalise(BibEntry e) = runall(e,[locVSaddr,capTitle,doiVSurl,normPages]);

// The idea is that "address" usually refers to the publisher, while "location" refers to the event.
// Since some BibTeX processors do not accept both, location is preferred here.
BibEntry locVSaddr(BibEntry e)
{
	if(("location" in e.attrs) && ("address" in e.attrs))
	{
		println("[x] Removed address which conflicted with location");
		e.attrs -= ("address" : e.attrs["address"]);
	}
	return e;
}

// A very lightweight (and therefore error-prone) scheme of recapitalisation for the paper titles.
BibEntry capTitle(BibEntry e)
{
	if("title" notin e.attrs)
		return e;
	str s1 = gimmeStr(e,"title"), s2 = capitalise(s1);
	if (s1!="" && s1 != s2)
	{
		println("[x] Title recapitalised to \"<s2>\"");
		e.attrs["title"] = quoted(bracketed(raw(s2)));
	}
	return e; 
}

str capW(str w) = (w in dontcap)?w:toUpperCase(substring(w,0,1))+substring(w,1);
str capitalise(str s) = folds(capW,split(" ",s)," ");

// If the DOI field is present, we do not need an additional URL pointing to the same location.
// E.g., we should remove all links to http://doi.acm.org/<doi>, url=="http://dx.doi.org/<doi>,
// http://link.springer.com/article/<doi>, http://doi.ieeecomputersociety.org/<doi>, etc
BibEntry doiVSurl(BibEntry e)
{
	if("doi" notin e.attrs || "url" notin e.attrs)
		return e;
	str doi = gimmeStr(e,"doi"), url = gimmeStr(e,"url");
	if (endsWith(url,doi))
	{
		println("[x] Removed excessive URL field.");
		e.attrs -= ("url" : e.attrs["url"]);
	}
	return e;
}

// The properties pages and numpages must be synchronised
BibEntry normPages(BibEntry e)
{
	if ("pages" notin e.attrs)
	{
		println("[!] Cannot fix: no information about pages.");
		return e;
	}
	int i1,i2;
	<i1,i2> = gimmeRange(e,"pages");
	if (i1+i2 == 0)
	{
		println("[!] Cannot understand \"<gimmeStr(e,"pages")>\" pages.");
		return e;
	}
	if ("numpages" notin e.attrs)
	{
		println("[x] Added numpages based on pages.");
		e.attrs += ("numpages":bracketed(raw("<i2-i1+1>")));
		return e;
	}
	if (i2-i1+1 != gimmeInt(e,"numpages"))
	{
		println("[x] Fixed wrong numpages based on pages.");
		e.attrs = e.attrs
				- ("numpages":e.attrs["numpages"])
				+ ("numpages":bracketed(raw("<i2-i1+1>")));
		return e;
	}
	if ("<i1>--<i2>" != gimmeStr(e,"pages"))
	{
		println("[x] Fixed slightly deviant format of pages.");
		e.attrs = e.attrs
				- ("pages":e.attrs["pages"])
				+ ("pages":bracketed(raw("<i1>--<i2>")));
		return e;
	}
	return e;
}
