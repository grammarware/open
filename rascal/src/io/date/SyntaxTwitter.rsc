@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::date::SyntaxTwitter

start syntax TwiDate = TwiDateSimplified date;
lexical TwiDateSimplified = NotSpace [\ ] TwiMonth m [\ ] TwiDay d [\ ] NotSpace [\ ] NotSpace [\ ] TwiYear y;
lexical TwiMonth = [A-Z][a-z][a-z];
lexical TwiDay = [0-9][0-9];
lexical NotSpace = ![\ ]+ >> [\ ];
lexical TwiYear = [2][0][0-1][0-9];
