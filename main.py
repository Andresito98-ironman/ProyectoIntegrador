"""
Archivo main.py
Ejecuta el flujo principal del programa utilizando las funciones de funciones.py
"""

import funciones

def main():
    # Mostrar mensaje de bienvenida
    funciones.mostrar_bienvenida()

    # Operaciones matemáticas
    num1 = 12
    num2 = 6
    print("Suma:", funciones.calcular_operacion(num1, num2, "suma"))
    print("Promedio:", funciones.calcular_operacion(num1, num2, "promedio"))
    print("Multiplicación:", funciones.calcular_operacion(num1, num2, "multiplicacion"))

    # Validación de correos
    correo_valido = "usuario@ejemplo.com"
    correo_invalido = "usuarioejemplo.com"
    print(f"¿'{correo_valido}' es válido?:", funciones.validar_correo(correo_valido))
    print(f"¿'{correo_invalido}' es válido?:", funciones.validar_correo(correo_invalido))

if __name__ == "__main__":
    main()
