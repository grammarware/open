@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Normal

import io::bibtex::Unparser;
import io::bibtex::Parser;
import IO;

public void main()
{
	println(bib2str([normalise(e) | e <- loc2bib(|home:///workspace/bibtex/list.bib|)]));
} 

BibEntry normalise(BibEntry e)
{
	return e;
}

//BibEntry normalise(BibEntry e)
//{
//	
//}
