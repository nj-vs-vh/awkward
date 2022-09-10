# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import awkward as ak


def to_cupy(array):
    """
    Converts `array` (many types supported) into a CuPy array, if possible.

    If the data are numerical and regular (nested lists have equal lengths
    in each dimension, as described by the #type), they can be losslessly
    converted to a CuPy array and this function returns without an error.

    Otherwise, the function raises an error.

    If `array` is a scalar, it is converted into a CuPy scalar.

    See also #ak.from_cupy and #ak.to_numpy.
    """
    with ak._util.OperationErrorContext(
        "ak.to_cupy",
        dict(array=array),
    ):
        from awkward._connect.cuda import import_cupy

        cupy = import_cupy()
        return ak._util.to_arraylib(cupy, array, True)
