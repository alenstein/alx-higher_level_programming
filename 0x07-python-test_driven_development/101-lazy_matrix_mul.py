import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        a = np.array(m_a)
        b = np.array(m_b)
        result = np.matmul(a, b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("m_a and m_b must be a list of lists of integers or floats:"
                        " m_a must be a list of lists or m_b must be a list of lists,"
                        " m_a can't be empty or m_b can't be empty,"
                        " each row of m_a must be of the same size or each row of m_b must be of the same size,"
                        " m_a should contain only integers or floats or m_b should contain only integers or floats")
