#IMPORTAR LIBRERIAS DE ENCRIPTACION (HASLIB) Y DE DATA (PANDAS)
import hashlib
import pandas as pd

#FUNCION PARA ENCRIPTAR TEXTO
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

#LEER ARCHIVO CSV CON PANDAS https://www.kaggle.com/spscientist/students-performance-in-exams
df=pd.read_csv('StudentsPerformance.csv')
#CREAR LISTA PARA ALMACENAR REGISTROS SHA256
hash1=[]

#LOOP QUE RECORRE TODOS LOS VALORES DE UN CAMPO DEL DATASET Y LO ENCRIPTA
for row in df["gender"]:
	hash1.append(encrypt_string(str(row)))

# SE COLOCAN ESTOS VALORES EN UNA COLUMNA NUEVA DEL DATASET
df['hash']=hash1

#IMPRIME LAS PRIMERAS 5 FILAS DEL DATASET 
print(df.head(5))
