import pandas as pd

# Supongamos que ya tienes un DataFrame llamado df
# df = pd.read_csv('tu_archivo.csv')

# ======================
# 1. Imprimir columnas específicas
# ======================
print("1. Imprimir columnas específicas:")
print(df[['columna1', 'columna2']])
print("\n")

# ======================
# 2. Imprimir las primeras o últimas filas
# ======================
print("2. Imprimir las primeras o últimas filas:")
print("Primeras 5 filas:")
print(df.head(5))
print("Últimas 3 filas:")
print(df.tail(3))
print("\n")

# ======================
# 3. Imprimir filas que cumplan con una condición
# ======================
print("3. Imprimir filas que cumplan con una condición:")
filtro = df[df['columna'] > valor]  # Reemplaza 'columna' y 'valor' con tus datos
print(filtro[['columna1', 'columna2']])
print("\n")

# ======================
# 4. Imprimir valores únicos de una columna
# ======================
print("4. Imprimir valores únicos de una columna:")
print(df['columna'].unique())
print("\n")

# ======================
# 5. Imprimir la información de un DataFrame
# ======================
print("5. Imprimir la información de un DataFrame:")
print(df.info())
print("\n")

# ======================
# 6. Obtener estadísticas descriptivas de columnas
# ======================
print("6. Obtener estadísticas descriptivas de columnas:")
print(df[['columna1', 'columna2']].describe())
print("\n")

# ======================
# 7. Imprimir una fila específica por su índice
# ======================
print("7. Imprimir una fila específica por su índice:")
print(df.loc[indice])  # Reemplaza 'indice' con el índice de la fila que quieres ver
print("\n")

# ======================
# 8. Imprimir filas y columnas específicas
# ======================
print("8. Imprimir filas y columnas específicas:")
print(df.loc[fila_inicio:fila_fin, ['columna1', 'columna2']])  # Reemplaza los índices y columnas con tus datos
print(df.iloc[fila_inicio:fila_fin, [indice_columna1, indice_columna2]])  # Reemplaza con índices numéricos
print("\n")

# ======================
# 9. Imprimir columnas con datos calculados
# ======================
print("9. Imprimir columnas con datos calculados:")
df['Nueva_Columna'] = df['columna1'] + df['columna2']  # Ejemplo de columna calculada
print(df[['Nombre', 'Nueva_Columna']])
print("\n")

# ======================
# 10. Imprimir con formato específico
# ======================
print("10. Imprimir con formato específico:")
print(df[['columna1', 'columna2']].round(2))  # Formatear con dos decimales
print("\n")
