"""
Archivo funciones.py
Contiene las funciones principales del proyecto integrador:
- mostrar_bienvenida
- calcular_operacion
- validar_correo
"""

def mostrar_bienvenida():
    """Imprime un mensaje de bienvenida en consola."""
    print("Bienvenido al proyecto integrador de Fundamentos de Programación.")

def calcular_operacion(num1: float, num2: float, tipo: str) -> float:
    """
    Realiza una operación matemática entre dos números.
    Parámetros:
        num1 (float): primer número
        num2 (float): segundo número
        tipo (str): tipo de operación ("suma", "promedio", "multiplicacion")
    Retorna:
        float: resultado de la operación
    """
    if tipo == "suma":
        return num1 + num2
    elif tipo == "promedio":
        return (num1 + num2) / 2
    elif tipo == "multiplicacion":
        return num1 * num2
    else:
        raise ValueError("Tipo de operación no válido.")

def validar_correo(correo: str) -> bool:
    """
    Verifica si un correo electrónico es válido.
    Parámetros:
        correo (str): cadena de texto
    Retorna:
        bool: True si es válido, False en caso contrario
    """
    return "@" in correo and "." in correo
