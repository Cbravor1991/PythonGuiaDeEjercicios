from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score

import pandas as pd

'''SE GENERA CARGO SALIARIO CARGO ANALAISTA ETCETERA'''
data = {
    'Edad': [28, 35, 30, 45, 25],
    'Salario': [60000, 80000, 70000, 90000, 50000],
    'Cargo': ['Analista', 'Gerente', 'Analista', 'Director', 'Asistente'],
    'Años en la Empresa': [2, 5, 4, 10, 1],
    'Promoción': ['No', 'Sí', 'No', 'Sí', 'No']
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['Cargo'], drop_first=True)

print(df_encoded)

X = df_encoded.drop('Promoción', axis=1)
y = df_encoded['Promoción']
y = y.map({'Sí': 1, 'No': 0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Definir el modelo XGBoost
xgb_model = xgb.XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    use_label_encoder=False,
    verbosity=0
)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy', accuracy)



'''EJEMPLO CON LABEL ENCODDING: sE CODIFICA CON 1 O 0 SI ES SI O NO'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb

# Crear un DataFrame con más de dos categorías
df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'Marta', 'Luis', 'Pedro', 'Sofia'],
    'Cargo': ['Gerente', 'Asistente', 'Analista', 'Asistente', 'Gerente', 'Interno'],
    'Promoción': ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí']
})

print("DataFrame Original:")
print(df)

# Crear el codificador
label_encoder = LabelEncoder()

# Aplicar Label Encoding a 'Cargo' y 'Promoción'
df['Cargo'] = label_encoder.fit_transform(df['Cargo'])
df['Promoción'] = label_encoder.fit_transform(df['Promoción'])

print("\nDataFrame con Label Encoding:")
print(df)

# Excluir la columna 'Nombre'
df = df.drop('Nombre', axis=1)

print("\nDataFrame después de excluir 'Nombre':")
print(df)

# Separar características (X) y variable objetivo (y)
X = df.drop('Promoción', axis=1)
y = df['Promoción']

print("\nCaracterísticas (X):")
print(X)

print("\nVariable Objetivo (y):")
print(y)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Crear el modelo XGBoost
xgb_model = xgb.XGBClassifier(
    objective='binary:logistic',  # Para clasificación binaria
    eval_metric='logloss',         # Métrica de evaluación
    use_label_encoder=False,
    verbosity=0
)

# Entrenar el modelo
xgb_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = xgb_model.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)

'''EJEMPLO CON MEAN ENCODING'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb

# Crear un DataFrame con más de dos categorías
df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'Marta', 'Luis', 'Pedro', 'Sofia'],
    'Cargo': ['Gerente', 'Asistente', 'Analista', 'Asistente', 'Gerente', 'Interno'],
    'Promoción': ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí']
})

print("DataFrame Original:")
print(df)

'''AGREGA UNA COLUMNA DE CARGO_ENCODEDCON EL PROMEDIO'''

# Aplicar Mean Encoding a 'Cargo'
mean_encoding = df.groupby('Cargo')['Promoción'].apply(lambda x: x.map({'Sí': 1, 'No': 0}).mean())
df['Cargo_encoded'] = df['Cargo'].map(mean_encoding)

print("\nDataFrame con Mean Encoding para 'Cargo':")
print(df)

# Excluir la columna 'Nombre' y la columna original 'Cargo'
df = df.drop(['Nombre', 'Cargo'], axis=1)

print("\nDataFrame después de excluir 'Nombre' y 'Cargo':")
print(df)

# Separar características (X) y variable objetivo (y)
X = df.drop('Promoción', axis=1)
y = df['Promoción']

print("\nCaracterísticas (X):")
print(X)

print("\nVariable Objetivo (y):")
print(y)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Crear el modelo XGBoost
xgb_model = xgb.XGBClassifier(
    objective='binary:logistic',  # Para clasificación binaria
    eval_metric='logloss',         # Métrica de evaluación
    use_label_encoder=False,
    verbosity=0
)

# Entrenar el modelo
xgb_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = xgb_model.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)

print("\nPrecisión del modelo XGBoost:")
print(f"{accuracy:.4f}")
