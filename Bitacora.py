import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

def capturar_nombre_del_rol():
  nombre_del_rol = input("Por favor, introduce el nombre del rol: ")
  return nombre_del_rol

def capturar_fecha_de_creacion():
  fecha_de_creacion = input("Indique la fecha de creación del requerimiento (formato YYYY-MM-DD): ")
  try:
    fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")
  except ValueError:
    print("La fecha de creación no es válida. Por favor, introduce una fecha en formato YYYY-MM-DD.")
    fecha_de_creacion = capturar_fecha_de_creacion()
  return fecha_de_creacion

def capturar_numero_de_posicion():
  numero_de_posicion = input("Indique el número del rol: ")
  return numero_de_posicion

def capturar_fecha_de_inicio():
  fecha_inicio_del_rol = input("Indique la fecha en la que debe iniciar esta persona: ")
  return fecha_inicio_del_rol

def capturar_solicitante():
  solicitante = input("Indique el nombre de la persona que solicita el cargo: ")
  return solicitante

def capturar_pais():
  pais = input("Indique el país: ")
  return pais

def capturar_compania():
  compania = input("Indique la compañía: ")
  return compania

def capturar_sede():
  sede = input("Indique la sede: ")
  return sede

def capturar_vinculacion():
  vinculacion = input("Indique el tipo de vinculación: ")
  return vinculacion

def capturar_numero_posiciones():
  numero_posiciones = input("¿Cuántas posiciones tenemos?: ")
  return numero_posiciones

def capturar_fecha_actual():
  fecha_actual = datetime.today()
  return fecha_actual

def calcular_dias_transcurridos(fecha_de_creacion, fecha_actual):
  """
  Calcula la cantidad de días transcurridos entre dos fechas.

  Args:
    fecha_de_creacion: La fecha de creación del rol (formato YYYY-MM-DD).
    fecha_actual: La fecha actual (obtenida con datetime.today()).

  Returns:
    La cantidad de días transcurridos entre las dos fechas.
  """

  # Convertir las fechas a objetos datetime
  # fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")

  # Restar las dos fechas
  diferencia = fecha_actual - fecha_de_creacion

  # Obtener la cantidad de días
  dias_transcurridos = diferencia.days

  return dias_transcurridos

# Ejemplo de uso
nombre_del_rol = capturar_nombre_del_rol()
fecha_de_creacion = capturar_fecha_de_creacion()
numero_de_posicion = capturar_numero_de_posicion()
fecha_inicio_del_rol = capturar_fecha_de_inicio()
solicitante = capturar_solicitante()
pais = capturar_pais()
compania = capturar_compania()
sede = capturar_sede()
vinculacion = capturar_vinculacion()
numero_posiciones = capturar_numero_posiciones()
fecha_actual = capturar_fecha_actual()
dias_transcurridos = calcular_dias_transcurridos(fecha_de_creacion, fecha_actual)

# Imprimir la información capturada
print(f"Nombre del rol: {nombre_del_rol}")
print(f"Fecha de creación: {fecha_de_creacion}")
print(f"Número de posición: {numero_de_posicion}")
print(f"Fecha de inicio: {fecha_inicio_del_rol}")
print(f"Solicitante: {solicitante}")
print(f"País: {pais}")
print(f"Compañía: {compania}")
print(f"Sede: {sede}")
print(f"Vinculación: {vinculacion}")
print(f"Número de posiciones: {numero_posiciones}")
print(f"Fecha actual: {fecha_actual}")
print(f"Días transcurridos: {dias_transcurridos}")
