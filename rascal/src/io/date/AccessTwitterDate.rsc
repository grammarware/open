module io::date::AccessTwitterDate

import io::date::SyntaxTwitter;
import ParseTree;

public str gimmeDay(str x) = "<parse(#TwiDate,x).date.d>";
public str gimmeMonth(str x) = "<parse(#TwiDate,x).date.m>";
public str gimmeYear(str x) = "<parse(#TwiDate,x).date.y>";

public str gimmeDay(loc x) = "<parse(#TwiDate,x).date.d>";
public str gimmeMonth(loc x) = "<parse(#TwiDate,x).date.m>";
public str gimmeYear(loc x) = "<parse(#TwiDate,x).date.y>";
