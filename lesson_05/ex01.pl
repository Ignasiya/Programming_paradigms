len([], 0).
len([_|T], Len) :-
    len(T, Len1), Len is Len1 + 1.

?- len([1, 2, 2, 3, 3, 3], Result), write(Result).