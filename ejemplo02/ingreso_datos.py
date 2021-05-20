from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Club
# Open del txt del apartado de club
archivo1 = open("data/datos_clubs.txt", 'r', encoding="utf8")

# Lectura de las lineas del archivo 
datos_club= archivo1.readlines()

# Ciclo repetitivo para ingresar los datos hacia la base de datos correspondiente
for i in range (0,len(datos_club),1): 
    d=datos_club[i].split(";") 
    p = Club(nombre=d[0], deporte=d[1], fundacion=d[2])
    session.add(p)
# Cierre de lectura del archivo  
archivo1.close() 


# Jugadores
archivo2 = open("data/datos_jugadores.txt", 'r', encoding="utf8")
# Consulta de todos los datos que existen en Club
data_club = session.query(Club).all() 
# Ciclo repetitivo para validar y guardar los datos en la base de datos correspondiente
datos_jugadores= archivo2.readlines()
for i in range (0,len(datos_jugadores),1):
    a=datos_jugadores[i].split(";")
    for club in data_club:
        if a[0] == club.nombre:
            id_club = club.id

    p = Jugador(nombre=a[3], dorsal=a[2], posicion=a[1],club_id=id_club)
    session.add(p) 
# Cierre de lectura del archivo
archivo2.close()

session.commit()

