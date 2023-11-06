#include <stdlib.h>
#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - function that prints basic info about python lists
 *
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int element;

	printf("[*] size of python list = %lu\n", py_size(p));
	printf("[*] allocated = %lu\n", ((pylist)p
}
