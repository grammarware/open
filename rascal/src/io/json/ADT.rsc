@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::json::ADT

data JSO
	= jsnumber(real n)
	| jsstring(str s)
	| jsboolean(bool b)
	| jsarray(list[JSO] xs)
	| jsobject(map[JSO,JSO] kvs)
	| jsnull()
	;
