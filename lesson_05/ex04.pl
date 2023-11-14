max_item_list([X], X).
max_item_list([I|L], Result) :-
    max_item_list(L, R1), (I > R1, Result is I; Result is R1).

?- max_item_list([1, 2, 3, 4, 5, 6], X), write(X).