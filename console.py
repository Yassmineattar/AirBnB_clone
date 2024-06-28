#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State, 'Place': Place, 'City': City,
        'Amenity': Amenity, 'Review': Review
    }

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """ EOF command to exit the program """
        print()
        exit()

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. """
        if not line:
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[line]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """" Prints the string representation of an instance
        based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name. """
        if line and line not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        obj_list = []
        for key, obj in all_objs.items():
            if not line or key.startswith(line):
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if attr_name in ['id', 'created_at', 'updated_at']:
            print("** attribute not allowed to be updated **")
            return
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
