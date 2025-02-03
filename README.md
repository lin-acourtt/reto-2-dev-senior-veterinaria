# reto-2-dev-senior-veterinaria 🐍 
# GestióndeClientesyMascotasReto 2 - Gestión de Veterinaria usandoProgramación Orientada a Objetos (Terminal)

## Programa que gestiona las operaciones basicas de una veterinaria 😺🐶🦊

El presente repositorio corresponde en el desarrollo de las actividades propuestas para el reto #2 del curso de python. 

Los autores somos **Lindsey Acourtt** y **Santiago Torres**

##### El objetivo de este proyecto es desarrollar una aplicacion basada en consola, que podamos interactuar por terminal, enfocada en gestionar clientes y mascotas, gestionar citas, mostrar historial de servicios, etc. 

### Menu principal. (ʘᴥʘ)   
una vez el usuario inicia el programa, se presentara el siguiente menu. El usuario debe ingresar el número de la función que desea llevar a cabo. Si ingresa algo diferente al número de una de las funciones disponibles, el usuario tendrá que intentarlo de nuevo. 

El detalle de cada función se detalla en la siguiente sección. 


```
-------------------------------------------------
                    Welcome:
                🐾 Happy Paw 🐾
        Veterinary Management System App

With this console application you'll be able to
manage your clients and their pets, schedule and
modify appointments, as well as to manage the
veterinarians and available services.


Developed by: Santiago Torres and Lindsey Acourtt
-------------------------------------------------


========= Main Menu =========
1. Register client
2. Register pet
3. Schedule appointment
4. Modify appointment
5. Cancel appointment
6. Check veterinary log for a pet
7. Display clients and pet information
8. Admin access
9. Exit

Choose an option:

```

### Funciones del programa 🔍 🔎 ╚(•⌂•)╝
Sistema de Gestión Veterinaria
Este proyecto implementa un sistema para la gestión de clientes, mascotas, citas y veterinarios, con la capacidad de registrar, modificar y visualizar información de manera eficiente.

Clases principales

```
People
__init__: Inicializa la persona con la información básica.
displayContactInfo: Muestra la información de contacto de la persona.

Pets
__init__: Inicializa la mascota.
scheduleAppointment: Programa una cita para la mascota.
cancelAppointment: Cancela la cita programada.
displayPetInfo: Muestra la información de la mascota.
displayVeterinaryLog: Muestra el historial veterinario de la mascota.

Appointments
__init__: Inicializa una cita.
modifyAppointment: Modifica una cita existente.
displayAppointmentInfo: Muestra la información de la cita.

Client
__init__: Inicializa un cliente.
displayContactInfo: Muestra la información de contacto del cliente.
addPet: Añade una mascota al cliente.
__str__: Representación en cadena del cliente.
__repr__: Representación más detallada del cliente.

Veterinarian
__init__: Inicializa al veterinario.
displayContactInfo: Muestra la información de contacto del veterinario.
addService: Añade un servicio a la lista del veterinario.
__str__: Representación en cadena del veterinario.
__repr__: Representación más detallada del veterinario.

FactoryOfPeople
createPerson: Crea una nueva persona.

Appointment
__init__: Inicializa una cita.
modifyAppointment: Modifica una cita existente.
displayAppointmentInfo: Muestra la información de la cita.
__str__: Representación en cadena de la cita.
__repr__: Representación más detallada de la cita.

Pet
__init__: Inicializa una mascota.
scheduleAppointment: Programa una cita para la mascota.
cancelAppointment: Cancela una cita programada.
displayPetInfo: Muestra la información de la mascota.
displayVeterinaryLog: Muestra el historial veterinario.
addOwner: Asocia un propietario a la mascota.
__str__: Representación en cadena de la mascota.
__repr__: Representación más detallada de la mascota.

VeterinaryMgmtSys
__new__: Implementa el patrón Singleton para garantizar una sola instancia del sistema.
createDatabase: Crea la base de datos del sistema.
registerClient: Registra un cliente en el sistema.
registerPet: Registra una mascota en el sistema.
schedulePetAppmt: Programa una cita para una mascota.
modifyPetAppmt: Modifica una cita para una mascota.
cancelPetAppmt: Cancela una cita para una mascota.
checkPetVeterinaryLog: Verifica el historial veterinario de una mascota.
__registerVet: Registra un veterinario en el sistema.
__removeVet: Elimina un veterinario del sistema.
__displayListOfVets: Muestra la lista de veterinarios registrados.
__registerServiceType: Registra un tipo de servicio.
__removeServiceType: Elimina un tipo de servicio.
__displayListOfServices: Muestra la lista de servicios disponibles.
__displayPrivateData: Muestra información privada del sistema.
welcomeMessage: Muestra el mensaje de bienvenida al sistema.
main_menu: Muestra el menú principal de opciones para el usuario.

```


### Librerias usadas

```
las librerias usadas son:
from abc import ABC, abstractmethod  ->> To create interfaces
from datetime import datetime        ->> To manage date and time
import os.path                       ->> To check if the database file exists in the folder
import pickle                        ->> To load/save database
from getpass import getpass          ->> To type passwords


```


