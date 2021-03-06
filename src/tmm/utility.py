from tmm.mathsrc.matrix import *

__author__ = "Ved Shah"
__status__ = "Development"

ERROR_DICT = {
    0: "Your specified and actual matrix dimensions differ",
    1: "Matrix Multiplcation condition is not satisfied",
    2: "Number of Columns in matrix 1 is not equal to number of rows in matrix 2",
    3: "Your matrices are not 0-1 matrices",
    4: "The inverse doesn't exist",
    5: "Invalid Input."

}


def matrix_builder(request, mindex, entry_index, isSquare=False):
    """
    This function takes the html inputs for the size and shape of the matrix and
    instantiates an object of the class Matrix with the desired number of rows and
    columns. It can also instantiate square matrices if so desired.

    Arguments:
        request {HTML request} -- POST/GET request from HTML form
        mindex {string} -- Queries the HTML request at mindex_rows and mindex_columns
        entry_index {string} -- Queries the HTML request at mindex_entry

    Keyword Arguments:
        isSquare {bool} -- Parameter to inform if the matrix needs to be a square (default: {False})

    Returns:
        tuple -- (matrix object, string of matrix entry)
    """
    temp_rows = request.POST[mindex + '_rows']

    if input_checker(temp_rows) == False:
        return False, False
    else:
        m_row_no = int(temp_rows)

        if isSquare:
            temp_columns = request.POST[mindex + '_rows']
        else:
            temp_columns = request.POST[mindex + '_columns']

        if input_checker(temp_columns) == False:
            return False, False
        else:
            m_col_no = int(temp_columns)
            m = Matrix(m_row_no, m_col_no)
            m_entries = request.POST[entry_index + '_entry'].strip()

            return m, m_entries


def clean(s, isInt=False):
    """
    This function takes the string input from the HTML text area
    field and converts those entries into a list of floating-point numbers or integers
    (for bitwise operations) which will be used to intialize the matrices.

    This function assumes the string only has number values separated by space.

    Arguments:
        s [str] -- The string to be convereted into a list of floating-point numbers
        must be space separated and can be on newlines.

        isInt [boolean] -- It tells the function if the values returned need to be
        integers or not

    Returns:
        list -- Python list of floating-point numbers from the string
    """
    temp = s.split()
    for i in range(0, len(temp)):
        if isInt:
            temp[i] = int(temp[i])
        else:
            temp[i] = float(temp[i])
    return temp


def matrix_to_list(m):
    """
    This function takes a matrix argument and reformats it to a list of string.
    Its purpose is to make it possible for the matrix to be displayed appropriately
    on a html webpage

    Arguments:
        m [matrix] -- The matrix that needs to be reformated into a list of strings

    Returns:
        list -- Python list of strings from floating-point numbers
    """
    matrix_string = []
    for i in range(1, m.get_row_no() + 1):
        s = ""
        for j in range(1, m.get_col_no() + 1):
            s += str(m.get_value(i, j)) + "    "
        matrix_string.append(s.rstrip())
    return matrix_string


def order_checker(m1, m2, m1_entries, m2_entries):
    """
     This Function takes the html request and two matrices and makes sure that that the
    order of each of the matrix is consistent with the order of the entered values

    Arguments:
        m1 {Matrix} -- Matrix 1
        m2 {Matrix} -- Matrix 2 or None for one matrix
        m1_entries {str} -- The string of characters to input into m1
        m2_entries {str} -- The string of characters to input into m2 or None
        for one matrix

    Returns:
        boolean -- True if everything is consistent and False
    """

    # Sanity chcek for input and actual dimensions of m1
    m1_row_no = m1_entries.count("\n") + 1
    total = len(m1_entries.split())
    if total % m1_row_no == 0:
        m1_col_no = total // m1_row_no

        if m2 is not None:
            # Sanity chcek for input and actual dimensions of m2
            m2_row_no = m2_entries.count("\n") + 1
            total2 = len(m2_entries.split())
            if total2 % m2_row_no == 0:
                m2_col_no = total2 // m2_row_no

                return (m1.get_row_no() == m1_row_no
                        and m1.get_col_no() == m1_col_no
                        and m2.get_row_no() == m2_row_no
                        and m2.get_col_no() == m2_col_no)
            else:
                return False
        else:
            return (m1.get_row_no() == m1_row_no
                    and m1.get_col_no() == m1_col_no)
    else:
        return False


def input_checker(s):
    """
    This function takes a string input and returns false if it contains one or more non terminal spaces.
    If not, the function returns an integer.

    Args:
        s (string): string which needs to be checked

    Returns:
        boolean: False if the string contains one or more non terminal spaces
        int: Value of the number in the string if the string does not contain any non terminal spaces
    """
    s = s.strip()
    temp = s.split()
    if len(temp) > 1:
        return False
    else:
        return int(s)
