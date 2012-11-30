module io::date::AccessTwitterDate

import io::date::SyntaxTwitter;
import ParseTree;
import String;

public str gimmeDay(str x) = notrail("<parse(#TwiDate,x).date.d>");
public str gimmeMonth(str x) = "<monthno("<parse(#TwiDate,x).date.m>")>";
public str gimmeYear(str x) = "<parse(#TwiDate,x).date.y>";

public str gimmeDay(loc x) = notrail("<parse(#TwiDate,x).date.d>");
public str gimmeMonth(loc x) = "<monthno("<parse(#TwiDate,x).date.m>")>";
public str gimmeYear(loc x) = "<parse(#TwiDate,x).date.y>";

str notrail(str s)
{
	if (stringChar(charAt(s,0))=="0")
		return stringChar(charAt(s,1));
	else
		return s;
}

int monthno("Jan") = 1;
int monthno("Feb") = 2;
int monthno("Mar") = 3;
int monthno("Apr") = 4;
int monthno("May") = 5;
int monthno("Jun") = 6;
int monthno("Jul") = 7;
int monthno("Aug") = 8;
int monthno("Sep") = 19;
int monthno("Oct") = 10;
int monthno("Nov") = 11;
int monthno("Dec") = 12;
default int monthno(str s) = "?";
