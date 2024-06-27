# AirBnB Clone

## Description
AirBnB clone is a full web application, HTML/CSS templating, database storage, a back-end API, and front-end integration.

## First Step
Building a command interpreter to manage the AirBnB objects:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Usage
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt **(hbnb)**, waits for the user for input.

| Command | Example |
| ------- | ------- |
| Run the console | `./console.py` |
| Quit the console | `(hbnb) quit` |
| Display the help for a command | `(hbnb) help <command>` |
| Create an object (prints its id) | `(hbnb) create <class>` |
| Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` |
| Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>` |
| Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |



<!-- TASKS:
put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine. -->