import pandas as pd

finanza=pd.read_csv('finanzas2020[1].csv', sep='\t')
#print(finanza)

def existencia_archivo_con_12_columnas(df):
    if len(df.columns)==12:
        resultado_correcto="NO HAY ERRORES, EL ARCHIVO EXISTE y SE PUEDE LEER, y EL Nº DE COLUMNAS ES 12, SÍ O SI"
        return resultado_correcto
    else:
        resultado_erroneo="NO TIENE 12 COLUMNAS"
        return resultado_erroneo

print(existencia_archivo_con_12_columnas(finanza))
