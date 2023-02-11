#!/usr/bin/python3

"""Define HBNDCommand class, entry point of the command interpreter """

import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    myClasses = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                 "Review"]

    def do_EOF(self, line):
        """exit interpreter with ctrl+d"""
        return True

    def help_EOF(self):
        """help EOF"""
        print("EOF command to exit the program\n")

    def help_quit(self):
        """help quit"""
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        """exit interpreter with quit command"""
        return True

    def emptyline(self):
        """do nothing with empty line"""
        pass

    def do_create(self, className):
        """ create a new instance of a class
            saves it (to the JSON file) and
            prints the id
        """
        if len(className) == 0:
            print("** class name missing **")
        elif className not in self.myClasses:
            print("** class doesn\'t exist **")
            return False
        else:
            new = eval("{}()".format(className))
            new.save()
            print(new.id)

    def do_show(self, strings):
        """ Prints the string representation of an instance based on
            the class name and id
        """
        args = strings.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif args[0] not in self.myClasses:
            print('** class doesn\'t exist **')
            return False

        objs = storage.all()
        key_value = args[0] + '.' + args[1]
        if key_value in objs:
            print(objs[key_value])
        else:
            print("** no instance found **")

    def do_destory(self, strings):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        args = strings.split()
        if len(strings) == 0:
            print("** class name missing **""")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif args[0] not in self.myClasses:
            print("""** class doesn\'t exist **""")
            return False

        obj = args[0] + '.' + args[1]
        all_obj = storage.all()
        if obj in all_obj.keys():
            all_obj.pop(obj, None)
            storage.save()
        else:
            print("""** no instance found **""")

    def do_all(self, strings):
        """ Updates an instance based on the class name and
            id by adding or updating attribute
            (save the change into the JSON file)
        """
        args = strings.split()
        objs = storage.all()

        if len(args) == 0:
            for i in objs:
                strArg = str(objs[i])
                print(strArg)
        elif strings not in self.myClasses:
            print("""** class doesn\'t exist **""")
            return False
        else:
            for i in objs:
                if i.startswith(args[0]):
                    strArg = str(objs[i])
                    print(strArg)
        return False

    def do_update(self, strings):
        """Updates an instance based on the class name and id
           by adding or updating attribute (save the change into the JSON file)
        """
        args = strings.split()
        flag = 0

        if len(strings) == 0:
            print("""** class name missing **""")
            return False

        try:
            class_name = strings.split()[0]
            eval("{}()".format(class_name))
        except IndexError:
            print("""** class doesn\'t exist **""")
            return False

        try:
            ins_id = strings.split()[1]
        except IndexError:
            print("""** instance id missing **""")
            return False

        objs = storage.all()

        try:
            new_class = objs["{}.{}".format(class_name, ins_id)]
        except IndexError:
            print("""** no instance found **""")
            return False

        try:
            attrib_name = strings.split()[2]
        except IndexError:
            print("""** attribute name missing **""")
            return False

        try:
            updated_value = strings.split()[3]
        except IndexError:
            print("""** value missing **""")
            return False

        if updated_value.isdecimal() is True:
            setattr(new_class, attrib_name, int(updated_value))
            storage.save()
        else:
            try:
                setattr(new_class, attrib_name, float(updated_value))
                storage.save()
            except:
                setattr(new_class, attrib_name, str(updated_value))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
