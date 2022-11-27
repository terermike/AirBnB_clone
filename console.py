#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass       
    
    def do_create(self, line):
        """Creates an instance.
        """
        if line == '' or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)             

    def do_show(self, line):
        if line == '' or line is None:
            print("** class name missing **")
        else:
            arg_list = line.split()
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = f"{arg_list[0]}.{arg_list[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
    def do_destroy(self, line):
        if line == '' or line is None:
            print("** class name missing **")
        else:
            arg_list = line.split()
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = f"{arg_list[0]}.{arg_list[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, line):
        if line is None or line == '':
            new = [str(v) for k, v in storage.all().items()]
            print(new)
            return

        arg = line.split()
        if arg[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = [str(v) for k, v in storage.all().items()
                    if type(v).__name__ == arg[0]]
            print(new)
    
    def do_update(self, line):
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if  len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
