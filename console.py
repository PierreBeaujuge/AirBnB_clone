#!/usr/bin/python3
"""
console.py module
"""
import cmd
import shlex
import ast
import models
from models.base_model import BaseModel
# Note: no need to import FileStorage if __objects is called
# from models.storage
# Reminder: models.storage is the instance of FileStorage
# from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class that defines the "entry point of the command interpreter"
    """

    prompt = '(hbnb) '
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def do_create(self, arg):
        """Create command to create an instance/object of a class"""
        """
        method that creates a new instance of a class, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.className[arg]()
            HBNBCommand.className[arg].save(obj)
            print(obj.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        """
        method that prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            print(models.storage._FileStorage__objects[args[0]+'.'+args[1]])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        """
        method that deletes an instance of a class
        based on the class name and id and saves the change into the JSON file
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            models.storage.save()

    def do_all(self, arg):
        """All command to print all instances of a/all class/es"""
        """
        method that prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.
        """
        if not arg:
            list_objs = []
            for key, obj in models.storage._FileStorage__objects.items():
                list_objs.append(str(obj))
            if len(list_objs) > 0:
                print(list_objs)
        else:
            if arg not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            else:
                list_objs = []
                for key, obj in models.storage._FileStorage__objects.items():
                    if arg == key.split('.')[0]:
                        list_objs.append(str(obj))
                if len(list_objs) > 0:
                    print(list_objs)

    def default(self, arg):
        """Default command that handles class cmds: <class name>.func()"""
        """
        <class name>.all(): retrieve all instances of a class
        <class name>.count(): retrieve the number of instances of a class
        <class name>.show(<id>): retrieve an instance based on its ID
        <class name>.destroy(<id>): destroy an instance based on his ID
        <class name>.update(<id>, <attribute name>, <attribute value>):
        update an instance based on his ID
        <class name>.update(<id>, <dictionary representation>):
        update an instance based on his ID
        Note: d = ast.literal_eval(re.search('({.+})', update_dict).group(0))
        """
        args = arg.split('.', 1)
        # print("default: {}".format(args))
        if args[0] in HBNBCommand.className.keys():
            if args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].strip('()') == 'count':
                self.obj_count(args[0])
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'update':
                arg0 = args[0]
                if ', ' not in args[1]:
                    arg1 = args[1].split('(')[1].strip(')')
                    self.do_update(arg0+' '+arg1)
                elif ', ' in args[1] and\
                     '{' in args[1] and ':' in args[1]:
                    arg1 = args[1].split('(')[1].strip(')').split(', ', 1)[0]
                    attr_dict = ast.literal_eval(args[1].split('(')[1]
                                                 .strip(')').split(', ', 1)[1])
                    # Note: json.loads NOT working here w/ single-quoted values
                    # attr_dict = json.loads(args[1].split('(')[1].strip(')')\
                    # .split(', ', 1)[1])
                    for key, value in attr_dict.items():
                        self.do_update(arg0+' '+arg1+' '+key+' '+str(value))
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) == 2:
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    self.do_update(arg0+' '+arg1+' '+arg2)
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) >= 3:
                    print(args[1])
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    print(arg1)
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    print(arg2)
                    arg3 = args[1].split('(')[1].strip(')').split(', ')[2]
                    print(arg3)
                    self.do_update(arg0+' '+arg1+' '+arg2+' '+arg3)
            else:
                print('*** Unknown syntax: {}'.format(arg))
        else:
            print("** class doesn't exist **")

    @staticmethod
    def obj_count(arg):
        """Obj_count command to print the number of instances of a class"""
        """
        Usage: <class name>.count(), retrieve the number of instances
        of a class
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            counter = 0
            for key, obj in models.storage._FileStorage__objects.items():
                if arg == key.split('.')[0]:
                    counter += 1
            print(counter)

    def do_update(self, arg):
        """Update command to add or update attributes"""
        """
        method that updates an instance/object based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        # print("do_update: {}".format(args))
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            if args[2] in obj.__dict__.keys():
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            else:
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            HBNBCommand.className[args[0]].save(obj)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        """
        method called when 'quit' is passed by the user; provides a way of
        exiting the command line interpreter (via Ctrl+d)
        """
        # Return True to stop the command loop
        return True

    def do_EOF(self, arg):
        """EOF implementation to exit the program (via Ctrl+d)\n"""
        """
        method called when Ctrl+d is typed in; provides the standard way of
        exiting the command line interpreter (via Ctrl+d). Note: Ctrl+d sends
        an EOF (End Of File) signal and by default Cmd does not know what
        to do with it unless the do_EOF method is implemented.
        """
        # Return True to stop the command loop
        return True

    def emptyline(self):
        """
        method that disables the repetition of the last command on passing
        an empty line. Note: by default when an empty line is entered, the
        last command is repeated; one can change this behavior by overriding
        the emptyline method as shown below
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
