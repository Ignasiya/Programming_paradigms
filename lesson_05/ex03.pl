male(серафим).
male(сергей).
male(александр).
male(алексей).
male(владимир).

female(анастасия).
female(ольга).
female(вера).
female(любовь).
female(галина).

parent(серафим, александр).
parent(серафим, анастасия).
parent(анастасия, вера).
parent(анастасия, алексей).
parent(ольга, вера).
parent(ольга, алексей).
parent(вера, сергей).
parent(вера, любовь).
parent(алексей, владимир).
parent(алексей, галина).

mother(X, Y) :-
    parent(X, Y), female(Y).
father(X, Y) :-
    parent(X, Y), male(Y).

grandfather(X, Z) :-
    parent(X, Y), father(Y, Z).
grandmonther(X, Z) :-
    parent(X, Y), mother(Y, Z).

child(X, Y) :-
    parent(Y, X).

?- mother(анастасия, Z), write(Z), write("\n").
?- father(анастасия, Z), write(Z), write("\n").
?- grandfather(анастасия, Z), write(Z), write("\n").
?- grandmonther(анастасия, Z), write(Z), write("\n").
?- child(анастасия, Z), write(Z), write("\n").