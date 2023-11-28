#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices
    Args:
        m_a : first matrix
        m_b: second matrix
    Returns:
        A new matrix
    """
    result = np.dot(m_a, m_b)
    return result
