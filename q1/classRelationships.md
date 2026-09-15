# Class Relationships: Association and Multiplicity


## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)


## Existing Class
Class: MusicGenre
Description: My class represents the diverse genre that is popular in different generations.


## New Related Class
Class: DiskAlbum
Description: My new class represents the physical copy of how a music can be played, regarding what song it is or what genre.


## Association
Relationship: Music artists HAS albums.
Explanation: I chose to make this kind of relationship because artists most likely have many songs that they all want to connect together in one genre, or category. Therefore, they create an ALBUM-- to show organized songs and music styles in different categories.


## Multiplicity
Multiplicity: 1 Album─────────1..* Singer
Explanation: This multiplicity fits my system because as a person who listens to music, I like it when some of my favorite music artists "collab" in an album, therefore, it also musical blending. But besides of 2 people creating music to 1 album, a singer can also choose sing alone, which in modern music terms is having a "solo".


## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
![Relationship Test Run](images/relationshipTestRun2.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)




## Analysis
### What is the association between your two classes?


### What multiplicity did you choose and why?


### How did you implement the relationship in Python?


### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?

