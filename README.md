# AirBnB_clone

This is the first step of the Holberton School AirBnB Clone Project.  The goal of this project is to deploy a server with a simple copy of the AirBnB website.

The Final Project Scope Is:

- A command interpreter to manipulate data without a visual interface.
- A website (the front-end) for user interface: static and dynamic
- Data storage through a database or files (i.e. objects)
- An API that communicates between the front-end and the data (retrieve, create, delete, update)

---
## Part 1 (0x01)
---
### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

**id:** string - assign with an uuid when an instance is created

**created_at:** The current datetime when an instance is created

**updated_at:** The current datetime when an instance is created, updated every time you change your object

**__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

#### Public instance methods:
- save(self): updates the public instance with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.

### Objectives For The Command Line Interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Operating In Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Operating In Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

###Directory Tree Structure For Phase #1 of HBnB Clone:
```
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── file_storage.cpython-34.pyc
│   │       └── __init__.cpython-34.pyc
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-34.pyc
│   │   ├── base.cpython-34.pyc
│   │   ├── base_model.cpython-34.pyc
│   │   ├── city.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   ├── place.cpython-34.pyc
│   │   ├── rectangle.cpython-34.pyc
│   │   ├── review.cpython-34.pyc
│   │   ├── square.cpython-34.pyc
│   │   ├── state.cpython-34.pyc
│   │   └── user.cpython-34.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
└── README.md
```
---
## Files

File Name | Description
--- | ---
`README.md` | A description of the Holberton AirBnB Project
`AUTHORS` | A listing of the project contributors
`console.py` | The program to launch the HBNB console
`basemodel.py` | Defines the BaseModel Class
`file_storage.py` | Defines the FileStorage Class & handles the database
`user.py` | Defines the User Class, a subclass of BaseModel
`city.py` | Defines the City Class, a subclass of BaseModel
`state.py` | Defines the User Class, a subclass of BaseModel
`amenity.py` | Defines the Amenity Class, a subclass of BaseModel
`review.py` | Defines the Review Class, a subclass of BaseModel
`place.py` | Defines the Place Class, a subclass of BaseModel
`tests/` | The test directory containing the unittest files for each Class
---
## Authors
* **Pierre Beaujuge** - [GitHub - PierreBeaujuge](https://github.com/PierreBeaujuge) | [LinkedIn](https://www.linkedin.com/in/pierre-beaujuge-81b75a137//) at [Holberton
School](http://holbertonschool.com).
* **Brendan Eliason** - [GitHub - zinczar](https://github.com/zinczar) | [LinkedIn](https://www.linkedin.com/in/brendaneliason/) at [Holberton
School](http://holbertonschool.com).
