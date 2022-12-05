0-print_list_integer.py
1. Secure access to an element in a list
2. Replace element
3. Print a list of integers... in reverse!
4. Replace in a copy
5. Can you C me now?
6. Lists of lists = Matrix
7. Tuples addition
8. More returns!
9. Find the max
10. Only by 2
11. Delete at
12. Switch
13. Linked list palindrome
14. CPython #0: Python lists
Create a C function that prints some basic info about Python lists.

Prototype: void print_python_list_info(PyObject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
listobject.h
object.h
Common Object Structures
List Objects

