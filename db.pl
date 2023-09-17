father(bashar,saeed).
father(bashar,hiba).
father(bashar,sameer).
father(bashar,abdullah).
father(saeed,bashar_junior).
father(saeed,celien).
father(saeed,elien).
father(saeed,khaled).
father(saeed,elham_junior).
father(sameer,sultan).
father(mounes,elhamie).
father(mounes,mazen).
father(bashar_junior,saeed_junior).
father(tahseen,anas).

mother(elham,saeed).
mother(elham,hiba).
mother(elham,sameer).
mother(elham,abdullah).
mother(amany,bashar_junior).
mother(amany,celien).
mother(amany,elien).
mother(reem,sultan).
mother(hiba,elhamie).
mother(hiba,mazen).
mother(noha,khaled).
mother(noha,elham_junior).
mother(noha,anas).
mother(elhamie,saeed_junior).

male(bashar).
male(saeed).
male(sameer).
male(abdullah).
male(bashar_junior).
male(sultan).
male(mounes).
male(mazen).
male(khaled).
male(saeed_junior).
male(anas).
male(tahseen).

female(elham).
female(hiba).
female(elien).
female(celien).
female(elhamie).
female(amany).
female(reem).
female(noha).
female(elham_junior).


parent(P1,P2) :-
    father(P1,P2).
parent(P1,P2) :-
    mother(P1,P2).

grandparent(P1,P2) :-
    parent(P3,P2),
    parent(P1,P3).

great_grandparent(P1,P2) :-
    parent(P3,P2),
    parent(P4,P3),
    parent(P1,P4).

son(P1,P2) :- parent(P2,P1),male(P1).
daughter(P1,P2) :- parent(P2,P1),female(P1).
child(P1,P2) :- parent(P2,P1).

grandson(P1,P2) :- grandparent(P2,P1),male(P1).
granddaughter(P1,P2) :- grandparent(P2,P1),female(P1).
grandchild(P1,P2) :- grandparent(P2,P1).

Brother(P1,P2) :-
    father(P3,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P4,P2),
    male(P1),
    P1 \= P2.

sister(P1,P2) :-
    father(P3,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P4,P2),
    female(P1),
    P1 \= P2.

uncle(P1,P2) :-
    brother(P3,P1),
    parent(P3,P2),
    male(P1).
uncle(P1,P2) :-
    sister(P3,P1),
    parent(P3,P2),
    male(P1).

aunt(P1,P2) :-
    brother(P3,P1),
    parent(P3,P2),
    female(P1).
aunt(P1,P2) :-
    sister(P3,P1),
    parent(P3,P2),
    female(P1).

nephew(P1,P2) :-
    parent(P3,P1),
    brother(P3,P2),
    male(P1).
nephew(P1,P2) :-
    parent(P3,P1),
    sister(P3,P2),
    male(P1).

niece(P1,P2) :-
    parent(P3,P1),
    brother(P3,P2),
    female(P1).
niece(P1,P2) :-
    parent(P3,P1),
    sister(P3,P2),
    female(P1).

cousin(P1,P2) :-
    parent(P3,P1),
    parent(P4,P2),
    brother(P4,P3).
cousin(P1,P2) :-
    parent(P3,P1),
    parent(P4,P2),
    sister(P4,P3).


wife(P1,P2) :-
    child(P3,P1),
    child(P3,P2),
    female(P1),
    P1 \= P2.

/*
wife(P1, P2) :-
    setof(P1, Child^(child(Child, P1),
                     child(Child, P2),
                     female(P1),
                     P1 \= P2
          ), Wives),
    Wives = [P1 | _].
*/


husband(P1,P2) :-
    child(P3,P1),
    child(P3,P2),
    male(P1),
    P1 \= P2.

/*
husband(P1, P2) :-
    setof(P1, Child^(child(Child, P1),
                     child(Child, P2),
                     male(P1),
                     P1 \= P2
          ), Husbands),
    Husbands = [P1 | _].
*/


mother_in_law(P1,P2) :-
    wife(P3,P2),
    mother(P1,P3).
mother_in_law(P1,P2) :-
    husband(P3,P2),
    mother(P1,P3).

father_in_law(P1,P2) :-
    wife(P3,P2),
    father(P1,P3).
father_in_law(P1,P2) :-
    husband(P3,P2),
    father(P1,P3).

parent_in_law(P1,P2) :-
    wife(P3,P2),
    parent(P1,P3).
parent_in_law(P1,P2) :-
    husband(P3,P2),
    parent(P1,P3).

brother_in_law(P1,P2) :-
    wife(P2,P3),
    brother(P1,P3),
    male(P1).
brother_in_law(P1,P2) :-
    husband(P2,P3),
    brother(P1,P3),
    male(P1).

sister_in_law(P1,P2) :-
    wife(P2,P3),
    sister(P1,P3),
    female(P1).
sister_in_law(P1,P2) :-
    husband(P2,P3),
    sister(P1,P3),
    female(P1).

half_brother(P1,P2) :-
    father(P5,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P4,P2),
    P5 \= P3,
    male(P1),
    P1 \= P2.
half_brother(P1,P2) :-
    father(P3,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P5,P2),
    P5 \= P4,
    male(P1),
    P1 \= P2.

half_sister(P1,P2) :-
    father(P5,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P4,P2),
    P5 \= P3,
    female(P1),
    P1 \= P2.
half_sister(P1,P2) :-
    father(P3,P1),
    father(P3,P2),
    mother(P4,P1),
    mother(P5,P2),
    P5 \= P4,
    female(P1),
    P1 \= P2.

step_mother(P1,P2) :-
    husband(Husband,P1),
    father(Husband,P2),
    mother(Mother,P2),
    Mother \= P1,
    female(P1).

step_father(P1,P2) :-
    wife(Wife,P1),
    mother(Wife,P2),
    father(Father,P2),
    Father \= P1,
    male(P1).

step_brother(P1,P2) :-
    male(P1),
    father(Father,P1),
    mother(Mother,P2),
    wife(Mother,Father),
    father(Father2,P2),
    mother(Mother2,P1),
    Father \= Father2,
    Mother \= Mother2,
    P1 \= P2.
step_brother(P1,P2) :-
    male(P1),
    father(Father,P2),
    mother(Mother,P1),
    husband(Father,Mother),
    father(Father2,P1),
    mother(Mother2,P2),
    Father \= Father2,
    Mother \= Mother2,
    P1 \= P2.

step_sister(P1,P2) :-
    female(P1),
    father(Father,P1),
    mother(Mother,P2),
    wife(Mother,Father),
    father(Father2,P2),
    mother(Mother2,P1),
    Father \= Father2,
    Mother \= Mother2,
    P1 \= P2.
step_sister(P1,P2) :-
    female(P1),
    father(Father,P2),
    mother(Mother,P1),
    husband(Father,Mother),
    father(Father2,P1),
    mother(Mother2,P2),
    Father \= Father2,
    Mother \= Mother2,
    P1 \= P2.

