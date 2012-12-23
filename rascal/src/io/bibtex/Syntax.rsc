@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Syntax

layout L = WS;
lexical WS = [\uC2A0 \ \n\r\t]* !>> [\uC2A0 \ \n\r\t]; // note the nonbreakable space (0xC2A0 in Unicode)

syntax OneBibEntry = BibEntryType kind "{" BibEntryName name "," {BibPair ","}+ pairs ","? "}";
lexical BibEntryType = "@" [a-zA-Z]+ name;
lexical BibEntryName = ![,]+ >> [,];
syntax BibPair = BibKey key "=" BibValue val;
lexical BibKey = [a-z]+;

lexical BibValue
	= BibValueQ
	| BibValueC
	| [a-zA-Z0-9]+ !>> [a-zA-Z0-9]
	;

lexical BibValueQ = [\"] BQElement* [\"] ;
lexical BQElement = ![\"\\{}] | [\\] [\"\'`&$%a-zA-Z] | BibValueC;

lexical BibValueC = [{] BCElement* [}];
lexical BCElement = BibValueC | ![{}];

start syntax BibLibrary = OneBibEntry+ es;
