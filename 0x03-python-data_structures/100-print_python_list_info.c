#include <Python.h>

/**
 * print_python_list_info - Exihibits basic info about Python.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sz, all, a;
	PyObject *obj;

	sz = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", all);

	for (a = 0; a < sz; a++)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
