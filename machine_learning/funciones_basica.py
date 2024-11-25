import pandas as pd

# Supongamos que ya tienes un DataFrame llamado df
# df = pd.read_csv('tu_archivo.csv')

# ======================
# 1. Crear un DataFrame de ejemplo
# ======================
print("1. Crear un DataFrame de ejemplo:")
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['NY', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
print("\n")

# ======================
# 2. Insertar una nueva columna
# ======================
print("2. Insertar una nueva columna:")
df['Salario'] = [50000, 60000, 70000]  # Agregar una columna con datos
print(df)
print("\n")

# ======================
# 3. Insertar una columna en una posición específica
# ======================
print("3. Insertar una columna en una posición específica:")
df.insert(1, 'Genero', ['F', 'M', 'M'])  # Insertar la columna 'Genero' en la segunda posición
print(df)
print("\n")

# ======================
# 4. Eliminar una columna
# ======================
print("4. Eliminar una columna:")
df.drop(columns=['Salario'], inplace=True)  # Eliminar la columna 'Salario'
print(df)
print("\n")

# ======================
# 5. Eliminar una fila por índice
# ======================
print("5. Eliminar una fila por índice:")
df.drop(index=1, inplace=True)  # Eliminar la fila con índice 1
print(df)
print("\n")

# ======================
# 6. Filtrar filas basadas en una condición
# ======================
print("6. Filtrar filas basadas en una condición:")
df_filtrado = df[df['Edad'] > 30]  # Filtrar filas donde la 'Edad' es mayor a 30
print(df_filtrado)
print("\n")

# ======================
# 7. Ordenar filas por una columna
# ======================
print("7. Ordenar filas por una columna:")
df_ordenado = df.sort_values(by='Edad', ascending=False)  # Ordenar por 'Edad' en orden descendente
print(df_ordenado)
print("\n")

# ======================
# 8. Renombrar columnas
# ======================
print("8. Renombrar columnas:")
df.rename(columns={'Nombre': 'Nombre_Completo'}, inplace=True)  # Renombrar 'Nombre' a 'Nombre_Completo'
print(df)
print("\n")

# ======================
# 9. Rellenar valores nulos
# ======================
print("9. Rellenar valores nulos:")
df.loc[2, 'Ciudad'] = None  # Introducir un valor nulo en la columna 'Ciudad'
df['Ciudad'].fillna('Desconocida', inplace=True)  # Rellenar valores nulos con 'Desconocida'
print(df)
print("\n")

# ======================
# 10. Eliminar valores nulos
# ======================
print("10. Eliminar valores nulos:")
df.dropna(inplace=True)  # Eliminar filas con valores nulos
print(df)
print("\n")

# ======================
# 11. Aplicar una función a una columna
# ======================
print("11. Aplicar una función a una columna:")
df['Edad_Aumentada'] = df['Edad'].apply(lambda x: x + 1)  # Aumentar la edad en 1 año
print(df)
print("\n")

# ======================
# 12. Agregar una fila
# ======================
print("12. Agregar una fila:")
nueva_fila = pd.DataFrame({'Nombre_Completo': ['David'], 'Edad': [40], 'Ciudad': ['Seattle']})
df = pd.concat([df, nueva_fila], ignore_index=True)  # Agregar la nueva fila al DataFrame
print(df)
print("\n")
