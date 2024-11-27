def count_substring(string, sub_string):
    respuesta = 0
    largo_string = len(string)
    largo_substring = len(sub_string)
    contador = 0
    for i in range(largo_string - largo_substring +1):
        if string[i:i+largo_substring] == sub_string:
            contador += 1
             
    return contador

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)