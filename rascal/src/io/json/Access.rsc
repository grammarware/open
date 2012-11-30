@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::json::Access

import io::json::ADT;
import util::Math;

public real gimmeReal(jsnumber(n)) = n;
public default real gimmeReal(JSO x) = 0.0;

public int gimmeInt(jsnumber(n)) = toInt(n);
public default int gimmeInt(JSO x) = 0;

public str gimmeString(jsstring(s)) = s;
public default str gimmeString(JSO x) = "";

public bool gimmeBool(jsboolean(b)) = b;
public default bool gimmeBool(JSO x) = false;

public list[JSO] gimmeArray(jsarray(xs)) = xs;
public default list[JSO] gimmeArray(JSO x) = [];

public map[JSO,JSO] gimmeMap(jsobject(kvs)) = kvs;
public default map[JSO,JSO] gimmeMap(JSO x) = ();

public JSO gimmeNull(JSO x) = jsnull(); // well, if this is what you are asking...
