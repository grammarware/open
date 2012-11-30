@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module TwiSKO
// TWItter to subatomic Scientific Knowledge Objects

import io::json::Parser;
import io::json::Access;
import io::json::ADT;
import io::date::AccessTwitterDate;
import IO; // println
import String; //startsWith, endsWith
import List; //size, reverse

public void go()
{
	loc w = |home:///workspace/open/data/last1000.json|;
	loc r = |home:///workspace/open/data/last1000.xml|;
	//loc w = |home:///workspace/open/data/one.json|;
	list[JSO] tweets = gimmeArray(loc2jso(w));
	list[str] res = reverse([s | str s <- [processTweet(gimmeMap(tweet)) | JSO tweet <- tweets], s!=""]);
	//str res = ("" | it + processTweet(gimmeMap(tweet)) | JSO tweet <- gimmeArray(loc2jso(w)));
	writeFile(r,(""|it+res|str s <- res));
	println("<size(res)> entries created from <size(tweets)> tweets.");
}

str processTweet(map[str,JSO] t)
{
	str txt = gimmeString(t["text"]);
	if (startsWith(txt,"@") || startsWith(txt,"RT @"))
		return "";
	return "
	'\<entry\>
	'	\<ts d=\"<t2day(t)>\" m =\"<t2month(t)>\" y=\"<t2year(t)>\"\>
	'	\<text\><txt>\</text\>
	'	\<twi\><t2id(t)>\</twi\>
	'\</entry\>";
}

str t2day(map[str,JSO] t) = gimmeDay(gimmeString(t["created_at"]));
str t2month(map[str,JSO] t) = gimmeMonth(gimmeString(t["created_at"]));
str t2year(map[str,JSO] t) = gimmeYear(gimmeString(t["created_at"]));

str t2id(map[str,JSO] t) = gimmeString(t["id_str"]);
