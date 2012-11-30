@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module TwiSKO
// TWItter to subatomic Scientific Knowledge Objects

import io::json::Parser;
import io::json::Access;

public void go()
{
	list[JSO] tweets = gimmeArray(loc2jso(|home:///workspace/open/data/last1000.json|));
}