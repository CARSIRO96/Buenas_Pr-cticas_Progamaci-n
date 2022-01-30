#TODO: ABRIR CON VISUAL ESTUDIO U OTRO DÍA
######################################################################################
###################################### LIBRERÍAS ######################################
######################################################################################
import pytest
import main
import pandas as pd

######################################################################################
###################################### VARIABLES ######################################
######################################################################################

archivo_prueba_error=pd.read_csv('prueba_erronea.csv')
archivo_prueba_correct=pd.read_csv('prueba_correcta.csv')
archivo_vacio=[]

error_existencia_de_archivos="NO TIENE 12 COLUMNAS"
correcto_input_existencia_de_archivos="NO HAY ERRORES, EL ARCHIVO EXISTE y SE PUEDE LEER, y EL Nº DE COLUMNAS ES 12, SÍ O SI"

hay_contenido='HAY CONTENIDO EN CADA COLUMNA DEL DF'
no_hay_contenidO='NO HAY CONTENIDO'

todas_cols_tipo_float='TODAS LAS VARIABLES-COLUMNAS SON DE TIPO FLOAT '

######################################################################################
###################################### TESTs ######################################
######################################################################################

def test_existencia_archivos():
    assert main.existencia_archivo_con_12_columnas(archivo_prueba_error)==error_existencia_de_archivos
    assert main.existencia_archivo_con_12_columnas(archivo_prueba_correct)==correcto_input_existencia_de_archivos

def test_si_hay_contenido():
    assert main.si_hay_contenido(archivo_prueba_correct)==hay_contenido
    assert main.si_hay_contenido(archivo_vacio)==no_hay_contenidO


def test_tipo_float():
    assert main.solo_valores_tipo_float(archivo_prueba_correct)==todas_cols_tipo_float
