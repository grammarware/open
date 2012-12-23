@contributor{Vadim Zaytsev - vadim@grammarware.net - SWAT, CWI}
module Rascalware

import List;

public str folds(str(&T) f, list[&T] ss) = ("" | it + f(s) | &T s <- ss);
public str folds(str(&T) f, list[&T] ss, str sep) = (f(ss[0]) | it + sep + f(s) | &T s <- tail(ss));
public list[&T] mapl(&T(&D) f, list[&D] xs) = [f(x) | &D x <- xs];
//public list[&T] mapc2a(&T(&D) f, {&D &L}+ xs) = [f(x) | &D x <- xs];
//public list[&T] mapc2a(&T(&D) f, &D+ xs) = [f(x) | &D x <- xs];

public &T runall(&T v, list[&T(&T)] fs) = (v | f(it) | &T(&T) f <- fs);
