# IAI HOMEWORK REPORT

- PhD. Bassel Alkhateeb
- Introduction for artifical inteligence
- S23
- Abdullah Altatan
- abdullah_232943
- [`Colab Link`](https://colab.research.google.com/drive/13mumDxQcCnX_EGMiguhsw2OCy86nT5kN?usp=sharing)

[`Family Tree`](#family-tree)  
[`Solution`](#solution)

## Family Tree

```
bashar
|
+ elham (wife)
|
|-------saeed----------------------------
|       |                               |
|       + amany (wife)                  + noha (second wife) --------
|       |                               |                           |
|       |--- bashar_junior + elhamie    |--- elham_junior           + tahseen (previous hubsand)
|       |       |--- saeed_junior       |--- khaled                 |
|       |                                                           |--- anas
|       |--- celien
|       |--- elien
| 
|-------hiba
|       |
|       + mounes (husband)
|       |
|       |--- elhamie
|       |--- mazen
|       
|-------sameer
|       |
|       + reem (wife)
|       |
|       |--- sultan
|       
|-------abdullah
```

## Solution

### Data

I put all rules,facts and atoms in [`Data File`](./data.csv) which i will import them in the code in the next step.

### Coding

[`Declaring query Function`](#declaring-query-function)  
[`Regular Expression`](#regular-expression)  
[`Getting terms`](#getting-terms)  
[`Creating Terms & Rules`](#creating-terms--rules)

#### Declaring query Function

i decalre a function to help me printing the result of the query which i want to use, by passing :
- **predicate** parameter as a rule which i will use.
- **p1** first atom.
- **p2** second atom.

i uses a list comprihansion to flat the elements from tuples inside the list directly insted of keep them in tuples and give them indexes.

```
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
```

#### Regular Expression

is used re module to compile a pattern to help me in exctracting the data from csv file.

```
name_re = re.compile(r"[A-z0-9\_]+")
```

#### Getting terms

i looped through the rows of csv file and exctracted the data using the pattern which i compiled before, and putted them into a set to remove duplicates and surrounded the whole set with list and joined it into one string to use that string as terms.

```
with open("./data.csv","r") as data_file:
  terms = ", ".join(list(set([cell for row in data_file for cell in re.findall(name_re,row)])))
```

#### Creating Terms & Rules

i looped through the rows again to define the facts using conditions.

```
log.create_terms(terms)

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
```

then i started decalring the rules and query them one by one, eg.:

```
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
.
.
.
and so on.
```

i hope the code explains itself.  
a lot of thanks.