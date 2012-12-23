@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::bibtex::Syntax

layout L = WS* !>> [\u0009-\u000D \u0020 \u0085 \u00A0 \u1680 \u180E \u2000-\u200A \u2028 \u2029 \u202F \u205F \u3000];
lexical    WS   =  [\u0009-\u000D \u0020 \u0085 \u00A0 \u1680 \u180E \u2000-\u200A \u2028 \u2029 \u202F \u205F \u3000];

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

lexical BibValueQ = [\"] BQElement* es [\"] ;
lexical BQElement = ![\"\\{}] | [\\] [\"\'`&$%a-zA-Z] | BibValueC;

lexical BibValueC = [{] BCElement* es [}];
lexical BCElement = BibValueC | ![{}];

start syntax BibLibrary = OneBibEntry+ es;
