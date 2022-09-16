# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print("1) ¿Quién fue el creador de windows?")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
if respuesta_1 == "Bill Gates":
    print("respuesta correcta")
