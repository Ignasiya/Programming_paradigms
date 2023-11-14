member(X,[X|_]).
member(X,[_|T]) :- member(X,T).

rem_dup([], []).
rem_dup([T|C], Res) :-
    member(T, C), rem_dup(C, Res).
rem_dup([T|C], [T|Res]) :-
    \+ member(T, C), rem_dup(C, Res).

?- rem_dup([1,2,3,4,5,6,1,1,2,3,4], Res), write(Res).