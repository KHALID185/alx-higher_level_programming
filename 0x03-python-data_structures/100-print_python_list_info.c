#include <Python.h>

/**
 * p_pyt - print info about list
 * @p: python object
*/
void print_python_list_info(PyObject *p)
{
int sz, al, j;
PyObject *ob;

sz = Py_SIZE(p);
al = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", sz);
printf("[*] Allocated = %d\n", al);
for (j = 0; j < sz; j++)
{
	printf("Element %d: ", j);
	ob = PyList_GetItem(p, j);
	printf("%s\n", Py_TYPE(ob)->tp_name);
}
}
