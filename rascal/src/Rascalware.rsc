@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module Rascalware

public str folds(str(&T) f, list[&T] ss) = ("" | it + f(s) | &T s <- ss);
public list[&T] mapl(&T(&D) f, list[&D] xs) = [f(x) | &D x <- xs];
//public list[&T] mapc2a(&T(&D) f, {&D &L}+ xs) = [f(x) | &D x <- xs];
//public list[&T] mapc2a(&T(&D) f, &D+ xs) = [f(x) | &D x <- xs];
