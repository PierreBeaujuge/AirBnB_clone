# Project: AirBnB Clone (@Holberton)

<p align='center'>
  <img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/HBTN-hbnb-Final.png" width="360" height=auto />
</p>

- This repository covers Part 1 & Part 2 of an AirBnB Clone project in Python/Flask.

-  The full-stack project is divided into 7 Parts:

|                                                      Parts                                                 |                    Description                    |
| :--------------------------------------------------------------------------------------------------------  | :-----------------------------------------------  |
| [1. Console](https://github.com/PierreBeaujuge/AirBnB_clone)                                               |   Data model management via command interpreter   |
| [2. Web static](https://github.com/PierreBeaujuge/AirBnB_clone/tree/master/web_static)                     |             Landing page in HTML and CSS          |
| 3. MySQL storage                                                                                           | Migration of local file storage to MySQL database |
| 4. Deploy static                                                                                           |        Deploy web static on an Nginx server       |
| 5. Web framework - templating                                                                              |         Web server deployment with Flask          |
| 6. RESTful API                                                                                             |      Creating endpoints for CRUD operations       |
| 7. Web dynamic                                                                                             | Loading of objects from client side using Jquery  |

### Expected web static for the final product:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

### Web Stack for building the product:

<p align="center">
  <img src="https://i.imgur.com/lgZnZrz.png">
</p>

### Schemas:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg">
</p>

---
## Part 1: 0x00. AirBnB clone - The console

![](./0x00-images/img_1.png)

Part 1 of AirBnB Clone project @Holberton: The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp (dare we say mastery?) of both front & backend development.

The overall Project scope is:

- Build a command line interpreter to manipulate data without a visual interface.
- A front-end (user interface) and a back-end for the web app: static and dynamic
- Data storage via a database or a file storage
- An API that bridges the front-end and the data (retrieve, create, delete, update)

### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

- **id:** string - assign with an uuid when an instance is created

- **created_at:** The current datetime when an instance is created

- **updated_at:** The current datetime when an instance is created, updated every time you change your object

- **__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

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
**Example Usage:**
```
newMod = BaseModel()
       - creates an instance of a method

print(NewMod.id)
	- prints the UUID
	   b6a6e15c-c67d-4312-9a75-9d084935e5

print(NewMod.created_at)
         - prints the time when the instance was created (ISO format)
	   '2017-09-28T21:03:54.052298'

print(NewMod.updated_at)
	- prints the most recent time that file was updated (ISO format)
       	  '2017-09-28T21:03:54.052302'
```
### Directory Tree Structure For Phase #1 of HBnB Clone:
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
│   │   ├── base_model.cpython-34.pyc
│   │   ├── city.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   ├── place.cpython-34.pyc
│   │   ├── review.cpython-34.pyc
│   │   ├── state.cpython-34.pyc
│   │   └── user.cpython-34.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    └── test_models
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── test_amenity.cpython-34.pyc
        │   ├── test_base_model.cpython-34.pyc
        │   ├── test_city.cpython-34.pyc
        │   ├── test_place.cpython-34.pyc
        │   ├── test_review.cpython-34.pyc
        │   ├── test_state.cpython-34.pyc
        │   └── test_user.cpython-34.pyc
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-34.pyc
        │   │   └── test_file_storage.cpython-34.pyc
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py

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

## Tasks

<summary>Console Tasks</summary>

### [ 0. README, AUTHORS ](./README.md)

- Write a README.md

---

### [ 1. Be PEP8 compliant! ](./README.md)

- Write beautiful code that passes the PEP8 checks.

---

### [ 2. Unittests ](./tests)

- All your files, classes, functions must be tested with unit tests

---

### [3. BaseModel ](./models/base_model.py)

- Write a class BaseModel that defines all common attributes/methods for other classes:
  - Public instance attributes:
    _ id: string - assign with an uuid when an instance is created:
    you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
    the goal is to have unique id for each BaseModel
    _ created_at: datetime - assign with the current datetime when an instance is created \* updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
  - **str**: should print: [<class name>](self.id) <self.**dict**>
  - Public instance methods:
    - save(self): updates the public instance attribute updated_at with the current datetime
    - to_dict(self): returns a dictionary containing all keys/values of **dict** of the instance:
      - by using self.**dict**, only instance attributes set will be returned
      - a key **class** must be added to this dictionary with the class name of the object
      - created_at and updated_at must be converted to string object in ISO format:
        - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        - you can use isoformat() of datetime object
      - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
```

```python
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

```

```
guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427
```

---

### [ 4. Create BaseModel from dictionary ](./models/base_model.py)

- Update models/base_model.py:
  - **init**(self, \*args, \*\*kwargs):
    - you will use \*args, \*\*kwargs arguments for the constructor of a BaseModel. More detail
    - \*args won’t be used
    - if kwargs is not empty:
      - each key of this dictionary is an attribute name
      - each value of this dictionary is the value of this attribute name
      - Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
    - otherwise:
      - create id and created_at as you did previously (new instance)

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
```

```python
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

```

```
guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'Holberton'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - Holberton
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
False
```

---

### [ 5. Store first object ](./models/file_storage.py)

- Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:
  - models/engine/file_storage.py
  - Private class attributes:
    - \_\_file_path: string - path to the JSON file (ex: file.json)
    - \_\_objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key \* will be BaseModel.12121212)
  - Public instance methods:
    - all(self): returns the dictionary \_\_objects
    - new(self, obj): sets in \_\_objects the obj with key <obj class name>.id
    - save(self): serializes **objects to the JSON file (path: **file_path)
    - reload(self): deserializes the JSON file to **objects (only if the JSON file (**file_path) exists ; otherwise, do nothing. If the file \* doesn’t exist, no exception should be raised)
- Update models/**init**.py: to create a unique FileStorage instance for your application
  - import file_storage.py
  - create the variable storage, an instance of FileStorage
  - call reload() method on this variable
- Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

  - import the variable storage
  - in the method save(self):
    - call save(self) method of storage
  - **init**(self, \*args, \*\*kwargs):
    - if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
```

```python
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

```

```
guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'Holberton', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'Holberton', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'Holberton', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'Holberton', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'Holberton', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'Holberton', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "Holberton", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "Holberton", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "my_number": 89}}
```

---

### [ 6. Console 0.0.1 ](./console.py)

- Write a program called console.py that contains the entry point of the command interpreter:
  - You must use the module cmd
  - Your class definition must be: class HBNBCommand(cmd.Cmd):
  - Your command interpreter should implement:
    - quit and EOF to exit the program
    - help (this action is provided by default by cmd but you should keep it updated and documented)
    - a custom prompt: (hbnb)
    - an empty line + ENTER shouldn’t execute anything
  - Your code should not be executed when imported

```sh
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
```

---

### [ 7. Console 0.1 ](./console.py)

- Update your command interpreter (console.py) to have these commands:
  - create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: \$ create BaseModel
    - If the class name is missing, print ** class name missing ** (ex: \$ create)
    - If the class name doesn’t exist, print ** class doesn't exist ** (ex: \$ create MyModel)
  - show: Prints the string representation of an instance based on the class name and id. Ex: \$ show BaseModel 1234-1234-1234.
    - If the class name is missing, print ** class name missing ** (ex: \$ show)
    - If the class name doesn’t exist, print ** class doesn't exist ** (ex: \$ show MyModel)
    - If the id is missing, print ** instance id missing ** (ex: \$ show BaseModel)
    - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: \$ show BaseModel 121212)
  - destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: \$ destroy BaseModel 1234-1234-1234.
    - If the class name is missing, print ** class name missing ** (ex: \$ destroy)
    - If the class name doesn’t exist, print ** class doesn't exist ** (ex:\$ destroy MyModel)
    - If the id is missing, print ** instance id missing ** (ex: \$ destroy BaseModel)
    - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: \$ destroy BaseModel 121212)
  - all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
    - The printed result must be a list of strings (like the example below)
    - If the class name doesn’t exist, print ** class doesn't exist ** (ex: \$ all MyModel)
  - update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: \$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
    - Usage: update <class name> <id> <attribute name> "<attribute value>"
    - Only one attribute can be updated at the time
    - You can assume the attribute name is valid (exists for this model)
    - The attribute value must be casted to the attribute type
    - If the class name is missing, print ** class name missing ** (ex: \$ update)
    - If the class name doesn’t exist, print ** class doesn't exist ** (ex: \$ update MyModel)
    - If the id is missing, print ** instance id missing ** (ex: \$ update BaseModel)
    - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: \$ update BaseModel 121212)
    - If the attribute name is missing, print ** attribute name missing ** (ex: \$ update BaseModel existing-id)
    - If the value for the attribute name doesn’t exist, print ** value missing ** (ex: \$ update BaseModel existing-id first_name)
    - All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com")
    - id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
    - Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

---

### [ 8. First User ](./models/user.py)

- Write a class User that inherits from BaseModel:
  - models/user.py
  - Public class attributes:
  - email: string - empty string
  - password: string - empty string
  - first_name: string - empty string
  - last_name: string - empty string
  - Update FileStorage to manage correctly serialization and deserialization of User.
- Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
```

```python
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

```

```
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@holbertonshool.com', 'first_name': 'Betty', 'last_name': 'Holberton', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@holbertonshool.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@holbertonshool.com", "first_name": "Betty", "__class__": "User", "last_name": "Holberton", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@holbertonshool.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@holbertonshool.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Holberton', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@holbertonshool.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@holbertonshool.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Holberton', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@holbertonshool.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@holbertonshool.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Holberton", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@holbertonshool.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@holbertonshool.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Holberton", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@holbertonshool.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
```

---

### [ 9. More classes! ](./models/)

- Write all those classes that inherit from BaseModel:
  - State (models/state.py):
    - Public class attributes:
      - name: string - empty string
  - City (models/city.py):
    - Public class attributes:
      - state_id: string - empty string: it will be the State.id
      - name: string - empty string
  - Amenity (models/amenity.py):
    - Public class attributes:
      - name: string - empty string
  - Place (models/place.py):
    - Public class attributes:
      - city_id: string - empty string: it will be the City.id
      - user_id: string - empty string: it will be the User.id
      - name: string - empty string
      - description: string - empty string
      - number_rooms: integer - 0
      - number_bathrooms: integer - 0
      - max_guest: integer - 0
      - price_by_night: integer - 0
      - latitude: float - 0.0
      - longitude: float - 0.0
      - amenity_ids: list of string - empty list: it will be the list of Amenity.id later
  - Review (models/review.py):
    - Public class attributes:
      - place_id: string - empty string: it will be the Place.id
      - user_id: string - empty string: it will be the User.id
      - text: string - empty string

---

### [ 10. Console 1.0 ](./models/engine/file_storage.py)

- Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
- Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

---

### [ 11. All instances by class name ](./models/engine/file_storage.py)

- Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all()

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
```

---

### [ 12. Count instances ](./console.py)

- Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
```

---

### [ 13. Show ](./console.py)

- Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Holberton")
** no instance found **
```

---

### [ 14. Destroy ](./console.py)

- Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Holberton")
** no instance found **
```

---

### [ 15. Update ](./console.py)

- Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
```

---

### [ 16. Update from dictionary ](./console.py)

- Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
```

---

### [ 17. Unittests for the Console! ](./console.py)

- Write all unittests for console.py, all features!

---

## Part 2: 0x01. AirBnB clone - Web static

![](./0x01-images/img_1.png)

### Background Context

_Web static, what?_

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

---

## Tasks

<summary>Console Tasks</summary>

### [ 0. Inline styling ](./web_static/0-index.html)

Write an HTML page that displays a header and a footer.

Layout:

- Body:
  - no margin
  - no padding
- Header:
  - color #FF0000 (red)
  - height: 70px
  - width: 100%
- Footer:
  - color #00FF00 (green)
  - height: 60px
  - width: 100%
  - text Holberton School center vertically and horizontally
  - always at the bottom at the page

- Requirements:

- You must use the header and footer tags
- You are not allowed to import any files
- You are not allowed to use the style tag in the head tag
- Use inline styling for all your tags

![](./0x01-images/img_2.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 0-index.html

---

### [ 1. Head styling ](./web_static/1-index.html)

Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

- You must use the header and footer tags
- You are not allowed to import any files
- No inline styling
- You must use the style tag in the head tag

The layout must be exactly the same as 0-index.html

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 1-index.html

---

### [ 2. CSS files ](./web_static/2-index.html)

Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

- You must use the header and footer tags
- No inline styling
- You must have 3 CSS files:
  - styles/2-common.css: for global style (i.e. the body style)
  - styles/2-header.css: for header style
  - styles/2-footer.css: for footer style
- The layout must be exactly the same as 1-index.html

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css

---

### [ 3. Zoning done! ](./web_static/3-index.html)

Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

- Common:
  - no margin
  - no padding
  - font color: #484848
  - font size: 14px
  - font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
  - icon in the browser tab
- Header:
  - color: white
  - height: 70px
  - width: 100%
  - border bottom 1px #CCCCCC
  - logo align on left and center vertically (20px space at the left)
- Footer:
  - color white
  - height: 60px
  - width: 100%
  - border top 1px #CCCCCC
  - text Holberton School center vertically and horizontally
  - always at the bottom at the page

Requirements:

- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 3 CSS files:
  - styles/3-common.css: for the global style (i.e body style)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style

![](./0x01-images/img_3.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/

---

### [ 4. Search! ](./web_static/4-index.html)

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)

- Container:
  - between header and footer tags, add a div:
  - classname: container
  - max width 1000px
  - margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
  - center horizontally
- Filter section:
  - tag section
  - classname filters
  - inside the .container
  - color white
  - height: 70px
  - width: 100% of the container
  - border 1px #DDDDDD with radius 4px
- Button search:
  - tag button
  - text Search
  - font size: 18px
  - inside the section filters
  - background color #FF5A5F
  - text color #FFFFFF
  - height: 48px
  - width: 20% of the section filters
  - no borders
  - border radius: 4px
  - center vertically and at 30px of the right border
  - change opacity to 90% when the mouse is on the button

Requirements:

- You must use: header, footer, section, button tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 4 CSS files:
  - styles/4-common.css: for the global style (body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style
  - styles/4-filters.css: for the filters style
- 4-index.html won’t be W3C valid, don’t worry, it’s temporary

![](./0x01-images/img_4.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/

---

### [ 5. More filters ](./web_static/5-index.html)

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

- Locations and Amenities filters:
  - tag: div
  - classname: locations for location tag and amenities for the other
  - inside the section filters (same level as the button Search)
  - height: 100% of the section filters
  - width: 25% of the section filters
  - border right #DDDDDD 1px only for the first left filter
  - contains a title:
    - tag: h3
    - font weight: 600
    - text States or Amenities
  - contains a subtitle:
    - tag: h4
    - font weight: 400
    - font size: 14px
    - text with fake contents

Requirements:

- You must use: header, footer, section, button, h3, h4 tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 4 CSS files:
  - styles/4-common.css: for the global style (body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style
  - styles/5-filters.css: for the filters style

![](./0x01-images/img_5.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/

---

### [ 6. It's (h)over ](./web_static/6-index.html)

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

- Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
  - tag ul
  - classname popover
  - text should be fake now
  - inside each div
  - not displayed by default
  - color #FAFAFA
  - width same as the div filter
  - border #DDDDDD 1px with border radius 4px
  - no list display
  - Location filter has 2 levels of ul/li:
    - state -> cities
    - state name must be display in a h2 tag (font size 16px)

Requirements:

- You must use: header, footer, section, button, h3, h4, ul, li tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 4 CSS files:
  - styles/4-common.css: for the global style (body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style
  - styles/6-filters.css: for the filters style

![](./0x01-images/img_6.png)

![](./0x01-images/img_7.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/

---

### [7. Display results](./web_static/7-index.html)

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

- Add Places section:
  - tag: section
  - classname: places
  - same level as the filters section, inside .container
  - contains a title:
    - tag: h1
    - text: Places
    - align in the top left
    - font size: 30px
  - contains multiple “Places” as listing (horizontal or vertical) describe by:
    - tag: article
    - width: 390px
    - padding and margin 20px
    - border #FF5A5F 1px with radius 4px
    - contains the place name:
      - tag: h2
      - font size: 30px
      - center horizontally

Requirements:

- You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 5 CSS files:
  - styles/4-common.css: for the global style (i.e. body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for footer style
  - styles/6-filters.css: for the filters style
  - styles/7-places.css: for the places style

![](./0x01-images/img_8.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/

---

### [ 8. More details ](./web_static/8-index.html)

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:

- Price by night:
  - tag: div
  - classname: price_by_night
  - same level as the place name
  - font color: #FF5A5F
  - border: #FF5A5F 4px rounded
  - min width: 60px
  - height: 60px
  - font size: 30px
  - align: the top right (with space)
- Information section:
  - tag: div
  - classname: information
  - height: 80px
  - border: top and bottom #DDDDDD 1px
  - contains (align vertically):
    - Number of guests:
      - tag: div
      - classname: max_guest
      - width: 100px
      - fake text
      - icon
    - Number of bedrooms:
      - tag: div
      - classname: number_rooms
      - width: 100px
      - fake text
      - icon
    - Number of bathrooms:
      - tag: div
      - classname: number_bathrooms
      - width: 100px
      - fake text
      - icon
- User section:
  - tag: div
  - classname: user
  - text Owner: <fake text>
  - Owner text should be in bold
- Description section:
  - tag: div
  - classname: description

Requirements:

- You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 5 CSS files:
  - styles/4-common.css: for the global style (i.e. body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style
  - styles/6-filters.css: for the filters style
  - styles/8-places.css: for the places style

![](./0x01-images/img_9.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/

---

### [ 9. Full details ](./web_static/100-index.html)

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 8-index.html)

Add more information to a Place article:

- List of Amenities:
  - tag div
  - classname amenities
  - margin top 40px
  - contains:
    - title:
      - tag h2
      - text Amenities
      - font size 16px
      - border bottom #DDDDDD 1px
    - list of amenities:
      - tag ul / li
      - no list style
      - icons on the left: Pet friendly, TV, Wifi, etc… feel free to add more
- List of Reviews:
  - tag div
  - classname reviews
  - margin top 40px
  - contains:
    - title:
      - tag h2
      - text Reviews
      - font size 16px
      - border bottom #DDDDDD 1px
    - list of review:
      - tag ul / li
      - no list style
      - a review is described by:
        - h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
        - p tag for the text (font size 12px)

Requirements:

- You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
- No inline style
- You are not allowed to use the img tag
- You are not allowed to use the style tag in the head tag
- All images must be stored in the images folder
- You must have 5 CSS files:
  - styles/4-common.css: for the global style (body and .container styles)
  - styles/3-header.css: for the header style
  - styles/3-footer.css: for the footer style
  - styles/6-filters.css: for the filters style
  - styles/100-places.css: for the places style

![](./0x01-images/img_10.png)

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/

---

### [10. Flex](./web_static/101-index.html)

Improve the Places section by using Flexible boxes for all Place articles

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/

---

### 11. Responsive design

Improve the page by adding responsive design to display correctly in mobile or small screens.

Examples:

- no horizontal scrolling
- redesign search bar depending of the width
- etc.

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/

---

### 12. Accessibility

Improve the page by adding Accessibility support

Examples:

- Colors contrast
- Header tags
- etc.

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/

---

## Authors

* **Pierre Beaujuge** - [GitHub - PierreBeaujuge](https://github.com/PierreBeaujuge) | [LinkedIn](https://www.linkedin.com/in/pierre-beaujuge-81b75a137/) at [Holberton
School](http://holbertonschool.com).
* **Brendan Eliason** - [GitHub - zinczar](https://github.com/zinczar) | [LinkedIn](https://www.linkedin.com/in/brendaneliason/) at [Holberton
School](http://holbertonschool.com).
