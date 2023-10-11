#include <Python.h>

/**
 * print_python_bytes - print bytes
 * @p: python object
 * Return: void
*/

void print_python_bytes(PyObject *p)
{
	unsigned char j, sz;
	PyBytesObject *b = (PyObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", sz);
	for (j = 0; j < sz; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}

}

/**
 * print_python_list - print info about list
 * @p: python object
*/
void print_python_list(PyObject *p)
{
	int sz, al, j;
	PyListObject *l = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;
	char *t;

	sz = v->ob_sz;
	al = l->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", al);
	for (j = 0; j < sz; j++)
	{
		t = l->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(l->ob_item[j]);
	}
}
