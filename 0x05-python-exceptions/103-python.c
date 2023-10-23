#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * byt_p - bytes prints
 * @ptr: pointer
 * Return: void
 */
void byt_p(PyObject *ptr)
{
	char *strg;
	size_t byt, itr;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(ptr) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	strg = ((PyBytesObject *)(ptr))->ob_sval, byt = PyBytes_Size(ptr);
	printf("  size: %ld\n  trying string: %s\n", byt, strg);
	byt >= 10 ? byt = 10 : b++;
	printf("  first %ld bytes: ", byt);
	for (itr = 0; itr < byt - 1; itr++)
		printf("%02hhx ", strg[itr]);
	printf("%02hhx\n", strg[itr]);
}
/**
 * flt_p - print float numbers
 * @ptr: pointer
 * Return: Empty
 */
void flt_p(PyObject *ptr)
{
	double fltt;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(ptr) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	fltt = ((PyFloatObject *)(ptr))->ob_fval;
	s = PyOS_double_to_string(fltt, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}
/**
 * lst_p - lists prints
 * @ptr: pointer
 * Return: Void
 */
void lst_p(PyObject *ptr)
{
	PyListObject *lssst;
	const char *garage;
	size_t sz, j_i, itrr;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(ptr) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	lssst = (PyListObject *)ptr;
	sz = PyList_GET_SIZE(ptr);
	j_i = lssst->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", sz, j_i);
	for (itrr = 0; itrr < sz; itrr++)
	{
		garage = (lssst->ob_item[itrr])->ob_type->tp_name;
		printf("Element %li: %s\n", itrr, garage);
		!strcmp(garage, "bytes") ? byt_p(lssst->ob_item[itrr]) : (void)garage;
		!strcmp(garage, "float") ? flt_p(lssst->ob_item[itrr]) : (void)garage;
	}
}
