vegetable(pomidor).
vegetable(cucumber).

berry(pomidor).

mystic_meal(X) :-
    vegetable(X), berry(X).

?- mystic_meal(pomidor), write("Yes").