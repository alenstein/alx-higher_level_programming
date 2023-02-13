#!/usr/bin/python3
""" Module contains definition for a function that multiplies two matrices."""


def validate_list(the_list):
    """
    function validates if a list meets the project requirements.

    Parameter(s):
        the_list: (list) list to be tested.

    Returns: None if all tests pass, otherwise raises an exception.
    """
    name = str(validate_list.__code__.co_varnames)
    if the_list is None:
        raise ValueError(name + " can't be empty")
    if type(the_list) is not list:
        raise ValueError(name + " must be a list")
    for item in the_list:
        if type(item) is not list:
            raise TypeError(name + "must be a list of lists.")
        for element in item:
            if element not in  [float, int]:
                raise ValueError(name + " should contain only integers"
                                        " or floats")
        if len(item) is not len(the_list[0]):
            raise TypeError(name + " each row of m_a must be of the same size")




def matrix_mul(m_a, m_b):
    """
     function that multiplies 2 matrices

     Parameters:
         m_a: (list) first matrix to be multiplied.
         m_b: (list) second matrix to be multiplied.

     Returns:
           a new matrix representing the product of teh two matrices.
    """
    m_a_m_b =  []

    rows = len(m_b)
    cols = len(m_a[0])

    # test if matrix multiplication is possible.
    if not (len(m_b) == len(m_a[0])):
        raise ValueError("")

    print("rows = " + str(rows))
    print("cols = " + str(cols))
    for i in range(rows):
        m_a_m_b.append([])
    print(m_a_m_b)
    for j in range(rows):
        for k in range(cols):
            print(j, k)
            print("cols: {:d}  rows: {:d} ".format(cols, rows))
            m_a_m_b[j].append(0)

    print("lists have been validated!")
    for row in range(rows):
        for col in range(cols):
            for k in range(rows):
                print("[{:d}][{:d}][:d]".format(row, col, k))
                try:
                    m_a_m_b[row][col] += (m_a[row][k] * m_b[k][col])
                except IndexError:
                    print("out of indexes!")
    return m_a_m_b
