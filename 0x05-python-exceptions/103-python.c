#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - bytes prints
 * @p: pointer
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *Stt;
	long int iterr, l_value, szz;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	szz = ((PyVarObject *)(p))->ob_size;
	Stt = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", szz);
	printf("  trying string: %s\n", Stt);

	if (szz >= 10)
		l_value = 10;
	else
		l_value = szz + 1;

	printf("  first %ld bytes:", l_value);

	for (iterr = 0; iterr < l_value; iterr++)
		if (Stt[iterr] >= 0)
			printf(" %02x", Stt[iterr]);
		else
			printf(" %02x", 256 + Stt[iterr]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - print float numbers
 * @p: pointer
 * Return: Empty
 */
void print_python_float(PyObject *p)
{
	char *strg;
	double flt_num;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	flt_num = ((PyFloatObject *)(p))->ob_fval;
	strg = PyOS_double_to_string
		(flt_num, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", strg);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - lists prints
 * @p: pointer
 * Return: Void
 */

void print_python_list(PyObject *p)
{
	long int lmt_sz;
	long int itrr;
	PyListObject *lsst;
	PyObject *o_b_j;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	lmt_sz = ((PyVarObject *)(p))->ob_size;
	lsst = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", lmt_sz);
	printf("[*] Allocated = %ld\n", lsst->allocated);

	for (itrr = 0; itrr < lmt_sz; itrr++)
	{
		o_b_j = lsst->ob_item[itrr];
		printf("Element %ld: %s\n", itrr, ((o_b_j)->ob_type)->tp_name);

		if (PyBytes_Check(o_b_j))
			print_python_bytes(o_b_j);
		if (PyFloat_Check(o_b_j))
			print_python_float(o_b_j);
	}
	setbuf(stdout, NULL);
}
