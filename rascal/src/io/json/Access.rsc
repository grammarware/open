@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::json::Access

import io::json::ADT;
import util::Math;
import String;

public real gimmeReal(jsnumber(n)) = n;
public default real gimmeReal(JSO x) = 0.0;

public int gimmeInt(jsnumber(n)) = toInt(n);
public default int gimmeInt(JSO x) = 0;

public str gimmeString(jsstring(s)) = unquote(s);
public str gimmeString(jsnumber(n)) = toString(n); // reasonably immoral
public default str gimmeString(JSO x) = "";

public bool gimmeBool(jsboolean(b)) = b;
public default bool gimmeBool(JSO x) = false;

public list[JSO] gimmeArray(jsarray(xs)) = xs;
public default list[JSO] gimmeArray(JSO x) = [];

public map[str,JSO] gimmeMap(jsobject(kvs)) = (gimmeString(k):kvs[k] | k <- kvs);
public default map[JSO,JSO] gimmeMap(JSO x) = ();

public JSO gimmeNull(JSO x) = jsnull(); // well, if this is what you are asking...

// other supplementary stuff

str unquote(str s)
{
	if (startsWith(s,"\"") && endsWith(s,"\""))
		return replaceLast(replaceFirst(s,"\"",""),"\"","");
	else
		return s;
}