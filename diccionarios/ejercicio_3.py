"Escribir un programa que vaya solicitando al usuario que ingrese nombres."
"a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar"
"el teléfono y, opcionalmente, permitir modificarlo si no es correcto."
"b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente."
"El usuario puede utilizar la cadena ”*”, para salir del programa."

def main():
    #creamos un diccionario con datos para probarlo
    diccionario = {
        'Juan' : '1234',
        'Sergio': '5678',
        'Julian': '8910',
        'Marcos': '2222' }
    
  
    while True:
     nombre = input ("Ingrese nombre a buscar o * para salir: ")
     if nombre == "*":
         break
     if nombre in diccionario:
        print(diccionario[nombre])
        modificar = input ("Desea modificarlo? SI/NO: ")
        if modificar == "SI":
            nuevo_telefono = input ("Ingrese nuevo telefono: ")
            diccionario[nombre] = nuevo_telefono
     elif nombre not in diccionario:
            telefono = input (f"Ingrese el telefono para {nombre}: ")
            diccionario[nombre] = telefono
    
    return

main()

