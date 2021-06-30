#!/usr/bin/python3
""" console module """
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class definition """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True

    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        'Creates a new instance of BaseModel, saves it'
        if len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist ** ")
        new = BaseModel()
        new.save()
        print(new.id)

    def do_show(self, arg):
        'Prints the string representation of an instance based on the class name and id'
        neww = BaseModel()
        if len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        if len(arg) > 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")
        print("{} {}".format(neww.__class__.__name__, neww.id))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
