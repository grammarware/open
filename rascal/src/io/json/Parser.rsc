@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::json::Parser

import io::json::ADT;
import io::json::Syntax;
import IO;
import String;
import ParseTree;
import util::Math;

public JSO loc2jso(loc l) = str2jso(readFile(l));

JSO str2jso(str s) = basic2jso(parse(#JSONBasicType,trim(s)));
	
JSO basic2jso((JSONBasicType)`<JSONNumber v>`) = str2num("<v>");
JSO basic2jso((JSONBasicType)`<JSONString v>`) = str2str("<v>");
JSO basic2jso((JSONBasicType)`<JSONBoolean v>`) = str2bool("<v>");
JSO basic2jso((JSONBasicType)`<JSONArray v>`) = jsarray(arr2array(v));
JSO basic2jso((JSONBasicType)`<JSONObject v>`) = jsobject(obj2object(v));
JSO basic2jso((JSONBasicType)`<JSONNull v>`) = jsnull();
default JSO basic2jso(JSONBasicType t)
{
	println("wtf?!");
	return jsnull();
}

JSO str2num(str s) = jsnumber(toReal(s)); // TODO so that it recognizes ints? (not crucial)
JSO str2str(str s) = jsstring(s);

JSO str2bool("true") = jsboolean(true);
default JSO str2bool(str s) = jsboolean(false);

list[JSO] arr2array((JSONArray)`[<{JSONBasicType ","}* vs>]`) = [basic2jso(v) | JSONBasicType v <- vs];

map[JSO,JSO] obj2object((JSONObject)`{<{JSONKeyValue ","}* kvs>}`) = (basic2jso(kv.key):basic2jso(kv.val) | JSONKeyValue kv <- kvs);
