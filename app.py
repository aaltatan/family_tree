from pyDatalog import pyDatalog as log
import re


def query(predicate,p1,p2) -> list:
  """
    print the result of the query from knowledge base with indexes.
  """

  list_of_tuples = predicate(p1,p2).ask()

  if type(p1) == str:
    print(f"\n{p1} is a {predicate} for : ")
  else:
    print(f"\n{predicate} for {p2}: ")

  list(set([print(f"{idx+1} - {element[0]}") for idx,element in enumerate(list_of_tuples)]))



name_re = re.compile(r"[A-z0-9\_]+")

# importing terms
with open("./data.csv","r") as data_file:
  terms = ", ".join(list(set([cell for row in data_file for cell in re.findall(name_re,row)])))

# creating terms
log.create_terms(terms)

# creating facts
with open("./data.csv","r") as data_file:
  for row in data_file:
    new_row = re.findall(name_re,row)[1:]
    if new_row[0] == "father":
      +father(new_row[1],new_row[2])
    elif new_row[0] == "mother":
      +mother(new_row[1],new_row[2])
    elif new_row[0] == "male":
      +male(new_row[1])
    elif new_row[0] == "female":
      +female(new_row[1])

# rules

# parenthood
parent(P1,P2) <= father(P1,P2)
parent(P1,P2) <= mother(P1,P2)

query(parent,X,"saeed")
query(parent,"bashar",X)
query(parent,"elham",X)

# grandparenthood & great grandparenthood
grandparent(P1,P2) <= parent(P3,P2) & parent(P1,P3)
great_grandparent(P1,P2) <= parent(P3,P2) & parent(P4,P3) & parent(P1,P4)

query(great_grandparent,"bashar",X)
query(great_grandparent,X,"saeed_junior")

# childhood
son(P1,P2) <= parent(P2,P1) & male(P1)
daughter(P1,P2) <= parent(P2,P1) & female(P1)
child(P1,P2) <= parent(P2,P1)

query(son,X,"bashar")
query(daughter,X,"bashar")
query(child,X,"bashar")
query(son,X,"elham")
query(daughter,X,"elham")
query(child,X,"elham")

# grandparenthood & great grandparenthood
grandson(P1,P2) <= grandparent(P2,P1) & male(P1)
granddaughter(P1,P2) <= grandparent(P2,P1) & female(P1)
grandchild(P1,P2) <= grandparent(P2,P1)

query(grandson,"bashar_junior",X)
query(grandson,X,"bashar")
query(granddaughter,"elhamie",X)
query(granddaughter,X,"bashar")
query(grandchild,"elhamie",X)
query(grandchild,X,"bashar")


# sibling
brother(P1,P2) <= father(P3,P1) & father(P3,P2) & mother(P4,P1) & mother(P4,P2) & male(P1) & (P1 != P2)
sister(P1,P2) <= father(P3,P1) & father(P3,P2) & mother(P4,P1) & mother(P4,P2) & female(P1) & (P1 != P2)

query(brother,"bashar_junior",X)
query(brother,X,"abdullah")
query(sister,"elhamie",X)
query(sister,X,"abdullah")
query(sister,X,"bashar_junior")


# uncle & aunt & cousin & nephew & niece
uncle(P1,P2) <= brother(P3,P1) & parent(P3,P2) & male(P1)
uncle(P1,P2) <=sister(P3,P1) & parent(P3,P2) & male(P1)

query(uncle,X,"bashar_junior")
query(uncle,X,"sultan")

aunt(P1,P2) <= brother(P3,P1) & parent(P3,P2) & female(P1)
aunt(P1,P2) <= sister(P3,P1) & parent(P3,P2) & female(P1)

query(aunt,X,"bashar_junior")
query(aunt,X,"sultan")
query(aunt,"hiba",X)

nephew(P1,P2) <= parent(P3,P1) & brother(P3,P2) & male(P1)
nephew(P1,P2) <= parent(P3,P1) & sister(P3,P2) & male(P1)

query(nephew,X,"abdullah")
query(nephew,"mazen",X)

niece(P1,P2) <= parent(P3,P1) & brother(P3,P2) & female(P1)
niece(P1,P2) <= parent(P3,P1) & sister(P3,P2) & female(P1)

query(niece,X,"abdullah")
query(niece,"elhamie",X)

cousin(P1,P2) <= parent(P3,P1) & parent(P4,P2) & brother(P4,P3)
cousin(P1,P2) <= parent(P3,P1) & parent(P4,P2) & sister(P4,P3)

query(cousin,"bashar_junior",X)
query(cousin,X,"bashar_junior")


# wife & husband
wife(P1,P2) <= child(P3,P1) & child(P3,P2) & female(P1) & (P1 != P2)
husband(P1,P2) <= child(P3,P1) & child(P3,P2) & male(P1) & (P1 != P2)

query(wife,X,"saeed")
query(husband,X,"amany")
query(wife,X,"sameer")
query(husband,X,"reem")
query(wife,"hiba",X)
query(husband,"mounes",X)


# in_law
mother_in_law(P1,P2) <= wife(P3,P2) & mother(P1,P3)
mother_in_law(P1,P2) <= husband(P3,P2) & mother(P1,P3)

query(mother_in_law,"elham",X)
query(mother_in_law,X,"mounes")

father_in_law(P1,P2) <= wife(P3,P2) & father(P1,P3)
father_in_law(P1,P2) <= husband(P3,P2) & father(P1,P3)

query(father_in_law,"bashar",X)
query(father_in_law,X,"reem")

parent_in_law(P1,P2) <= wife(P3,P2) & parent(P1,P3)
parent_in_law(P1,P2) <= husband(P3,P2) & parent(P1,P3)

query(parent_in_law,"bashar",X)
query(parent_in_law,X,"reem")

brother_in_law(P1,P2) <= wife(P2,P3) & brother(P1,P3) & male(P1)
brother_in_law(P1,P2) <= husband(P2,P3) & brother(P1,P3) & male(P1)

query(brother_in_law,"abdullah",X)
query(brother_in_law,X,"reem")

sister_in_law(P1,P2) <= wife(P2,P3) & sister(P1,P3) & female(P1)
sister_in_law(P1,P2) <= husband(P2,P3) & sister(P1,P3) & female(P1)

query(sister_in_law,"hiba",X)
query(sister_in_law,X,"reem")


# half sibling
half_brother(P1,P2) <= father(P5,P1) & father(P3,P2) & mother(P4,P1) & mother(P4,P2) & (P5 != P3) & male(P1) & (P1 != P2)
half_brother(P1,P2) <= father(P3,P1) & father(P3,P2) & mother(P4,P1) & mother(P5,P2) & (P5 != P4) & male(P1) & (P1 != P2)

half_sister(P1,P2) <= father(P5,P1) & father(P3,P2) & mother(P4,P1) & mother(P4,P2) & (P5 != P3) & female(P1) & (P1 != P2)
half_sister(P1,P2) <= father(P3,P1) & father(P3,P2) & mother(P4,P1) & mother(P5,P2) & (P5 != P4) & female(P1) & (P1 != P2)

query(half_brother,X,"bashar_junior")
query(half_brother,X,"khaled")
query(half_sister,X,"bashar_junior")
query(half_sister,X,"khaled")


# step father & mother & brother & sister

step_mother(P1,P2) <= husband(Husband,P1) & father(Husband,P2) & mother(Mother,P2) & (Mother != P1) & female(P1)
step_father(P1,P2) <= wife(Wife,P1) & mother(Wife,P2) & father(Father,P2) & (Father != P1) & male(P1)

query(step_mother,X,"bashar_junior")
query(step_mother,X,"khaled")
query(step_mother,"amany",X)
query(step_mother,"noha",X)
query(step_father,X,"anas")

step_brother(P1,P2) <= male(P1) & father(Father,P1) & mother(Mother,P2) & wife(Mother,Father) & father(Father2,P2) & mother(Mother2,P1) & (Father != Father2) & (Mother != Mother2) & (P1 != P2)
step_brother(P1,P2) <= male(P1) & father(Father,P2) & mother(Mother,P1) & husband(Father,Mother) & father(Father2,P1) & mother(Mother2,P2) & (Father != Father2) & (Mother != Mother2) & (P1 != P2)

query(step_brother,X,"anas")
query(step_brother,X,"bashar_junior")
query(step_brother,"anas",X)

step_sister(P1,P2) <= female(P1) & father(Father,P1) & mother(Mother,P2) & wife(Mother,Father) & father(Father2,P2) & mother(Mother2,P1) & (Father != Father2) & (Mother != Mother2) & (P1 != P2)
step_sister(P1,P2) <= female(P1) & father(Father,P2) & mother(Mother,P1) & husband(Father,Mother) & father(Father2,P1) & mother(Mother2,P2) & (Father != Father2) & (Mother != Mother2) & (P1 != P2)

query(step_sister,X,"anas")