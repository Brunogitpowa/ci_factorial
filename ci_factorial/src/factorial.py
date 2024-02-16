"""
Este módulo contiene una implementación de la función factorial.
"""

def factorial(n):

    """
    Calcula el factorial de un número.
    """

    if n in {0, 1}:  # fusionar las comparaciones con 'in'
        return 1
    return n * factorial(n - 1)
    