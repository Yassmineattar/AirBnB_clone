<h2>Description</h2>
AirBnB clone is a full web application, HTML/CSS templating, database storage, a back-end API, and front-end integration
<h3>1-First step</h3>
Building a command interpreter to manage the AirBnB objects:
<ul><li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li></ul>

<!-- TASKS:
put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine. -->