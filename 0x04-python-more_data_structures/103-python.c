#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid Python list object.\n");
        return;
    }

    Py_ssize_t size = PyObject_Length(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyVarObject *)p)->ob_size);

    for (i = 0; i < size; i++) {
        PyObject *item = ((PyListObject *)p)->ob_item[i];
        const char *typeName = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, typeName);
    }
}

/**
 * prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Python bytes object.\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    Py_ssize_t i;

    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %ld\n", size);
    printf("Bytes object content: ");

    // Print up to 10 bytes or the size of the bytes object, whichever is smaller
    Py_ssize_t numBytes = size < 10 ? size : 10;

    for (i = 0; i < numBytes; i++) {
        unsigned char byte = ((unsigned char *)p->ob_start)[i];
        printf("%02x", byte);
    }
    printf("\n");
}
