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

############################################################
def si_hay_contenido(df):
    try:
        hay_contenido='HAY CONTENIDO EN CADA COLUMNA DEL DF'
        assert(len(df!=0))
        return hay_contenido
    except:
        no_hay_contenidO='NO HAY CONTENIDO'
        return no_hay_contenidO

print(si_hay_contenido(finanza) )


############################################################
def solo_valores_tipo_float(df):
    
    columnas=df.columns.to_list()
    global df_float
    df_float=pd.DataFrame()

    for c in columnas:
        Nº_NO_Enteros=0
        for v in df[c].values:
            try:
                nuevo_valor=float(v)
            except ValueError:
                nuevo_valor=0
            finally:
                df_float.loc[Nº_NO_Enteros,c]=nuevo_valor
                Nº_NO_Enteros+=1
    for col in columnas:
        if (df_float[col].dtype=='float64'):
            resultado_correcto='TODAS LAS VARIABLES-COLUMNAS SON DE TIPO FLOAT '
            return resultado_correcto
        else:
            resultado_erroneo='NO SON TODAS LAS VARIABLES DE TIPO FLOAT'
            return resultado_erroneo

print(solo_valores_tipo_float(finanza))
print(f'DF CON VARIABLES FLOAT: \n {df_float.head()}')