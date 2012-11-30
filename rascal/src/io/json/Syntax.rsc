@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module io::json::Syntax

layout L = WS;
lexical WS = [\ \n\r\t]* !>> [\ \n\r\t];

start syntax JSONData = JSONBasicType;

syntax JSONBasicType
	= JSONNumber
	| JSONString
	| JSONBoolean
	| JSONArray
	| JSONObject
	| JSONNull
	;

syntax JSONNumber = "-"? Digits ("." Digits)?;
lexical Digits = [0-9]+ !>> [0-9];

syntax JSONString = DoubleQuotedString;
lexical DoubleQuotedString = [\"] DQSElement* [\"]; //"
lexical DQSElement = ![\"] | [\\][\"] ; //"

syntax JSONBoolean = "false" | "true" ;

syntax JSONArray = "[" {JSONBasicType ","}* "]";

syntax JSONObject = "{" {JSONKeyValue ","}* "}";
syntax JSONKeyValue = JSONBasicType key ":" JSONBasicType val;

syntax JSONNull = "null" ;
