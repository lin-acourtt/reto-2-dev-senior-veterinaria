# Reto 2 Dev Senior - Python: Veterinaria 🐍
# Gestión de Clientes y Mascotas Reto 2 - Gestión de Veterinaria usando Programación Orientada a Objetos (Terminal)

## Programa que gestiona las operaciones basicas de una veterinaria 😺🐶🦊

El presente repositorio corresponde al desarrollo de las actividades propuestas para el reto #2 del curso de Python de Dev-Senior. 

Los autores somos **Lindsey Acourtt** y **Santiago Torres**

**El objetivo de este proyecto es desarrollar una aplicacion basada en consola, en la cual podamos interactuar por terminal, enfocada en gestionar clientes y mascotas, gestionar citas, mostrar historial de servicios, etc. para una veterinaria.** 

### Menu principal

Una vez el usuario inicia el programa, se presentará el siguiente menu. El usuario debe ingresar el número de la función que desea llevar a cabo. Si ingresa algo diferente al número de una de las funciones disponibles, el usuario tendrá que intentarlo de nuevo. 

El detalle de cada función se describe  en la siguiente sección. 


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

**Funciones del programa principal 🔍 🔎**

#### Opción 1 y 2: "Registrar cliente" y "Registrar mascota

El programa pide al usuario los siguientes datos para registrar un cliente:

* Nombre
* Contacto
* Dirección

Y para registrar una mascota

* Nombre
* Especia
* Raza
* Edad

Cada cliente tendrá asigando un ID el cual se calcula automáticamente.

Cada vez que se registre un cliente nuevo, se pedirá inmediatamente asignarle una mascota. 

Cada vez que se registre una mascota nueva, se pedirá inmediatamente asignarle un dueño. El dueño puede ser un cliente que ya se encuentre registrado, o uno nuevo.

#### Opción 3, 4 y 5: "Agendar cita","Modificar cita" y "Cancelar cita"
Para cada una de estas opciones, el usuario debe ingresar el nombre de la mascota y su dueño. Si hay coincidencia, se evalúa primeramente si hay citas registradas para tal mascota.

En dado caso de que sí, el procedimiento para cada operación es el siguiente:

##### Agendar cita

Se solicitan los siguientes datos para registrar la cita:

* Tipo de servicio (cita regular, vacunas, cirugía, salón, etc.)
* Veterinario (Solo se podrán escoger los veterinarios que ofrecen el tipo de servicio seleccionado)
* Fecha
* Hora

##### Modificar cita

Se puede modificar cada uno de los aspectos de la cita individualmente (tipo de servicio, veterinario, fecha y hora), dejando la opción de quedarse con la información que se encuentra ya registrada para unos parámetros, y cambiar la información para otros.

##### Cancelar cita
Se imprime una lista de las citas encontradas para la mascota seleccionada, y se le pide al usuario cuál eliminar.
#### Opción 6: Imprimir registro veterinario de una mascota
Como en la opción anterior, se solicitan los nombres de la mascota y dueño que se desean consultar. Si hay coincidencia, se muestra una lista de las citas registradas para la mascota.
```
Choose an option: 6

Enter the pet's name to check their appointments: nino
Enter the owner's name: lindsey

Appointments for Nino:
------------------
1.
Date: 2025-02-02
Time: 10:30:00
Pet: Nino
Service: Appointment
Veterinarian: Ruby
------------------
2.
Date: 2025-01-30
Time: 14:00:00
Pet: Nino
Service: Vaccination
Veterinarian: William
------------------

Press enter to continue.
```
#### Opción 7: Imprimir información de clientes y mascotas registradas
Se muestra un registro total de los clientes registrados, junto a su información de contacto y mascotas asociadas; y también, una lista de mascotas registradas, junto a sus detalles y dueños asociados.

```
Choose an option: 7

****************** LIST OF CLIENTS ******************
-----------------------------
ID: 1
Name: Lindsey
Contact: 3111234567
Address: Barranquilla
List of pets: [Shiro, Nino]
-----------------------------
ID: 2
Name: Sharon
Contact: 1234567890
Address: Barranquilla 2
List of pets: [Melania]
-----------------------------

****************** LIST OF PETS ******************
1. Name: Shiro - Species: Cat - Breed: Grey - Age: 3 - Owner: Lindsey
2. Name: Nino - Species: Cat - Breed: Brown - Age: 2 - Owner: Lindsey
3. Name: Melania - Species: Dog - Breed: Yorkshire - Age: 7 - Owner: Sharon

Enter to return to main menu.
```

### Menú especial de administrador

Este es un menú especial al que solo se puede acceder ingresando la contraseña correcta. En este, se puede hacer la gestión de los veterinarios disponibles en la clínica, y los tipos de servicios asociados a cada uno de ellos. Si no existe información de veterinarios disponibles, las operaciones del menú principal de gestión de citas no serán posibles.

```
*** Admin menu ***
1. Register veterinarian
2. Remove veterinarian
3. Display list of veterinarians
4. Register type of service
5. Remove type of service
6. Display list of services
7. Display the whole registry
8. Return

Choose your admin option:
```

#### Opción 1 (admin): Registrar veterinario

Cada veterinario está asociado a mínimo un servicio, así que si no hay servicios registrados, no se puede registrar un veterinario. Para registrar un tipo de servicio, se usa la opción 4 del menú. 

Al registrar un veterinario, se piden los siguientes datos:

* Nombre
* Contacto
* Tipo de servicio (Solo se pueden escoger los servicios disponibles)

#### Opción 2 (admin): Eliminar veterinario

Se usa para eliminar veterinarios. 

#### Opción 3 (admin): Mostrar veterinarios registrados

La información de los veterinarios se muestra de este modo:

```
Choose your admin option: 3

**********************

List of Veterinarians:

1. Name: Ruby - Contact: 2831836783 - Service Provided: ['Appointment', 'Salon']
2. Name: John - Contact: 1982441243 - Service Provided: ['Surgery', 'Salon']
3. Name: William - Contact: 9871206348 - Service Provided: ['Appointment', 'Surgery', 'Vaccination']

Press enter to continue.
```

#### Opción 4 (admin): Registrar servicio

Sencillamente se pide el nombre del servicio y este queda inmediatamente registrado.

#### Opción 5 (admin): Eliminar servicio

Se usa para eliminar servicios. Además, se buscan los veterinarios que tienen dicho servicio asociado y se eliminan de su registro. 

#### Opción 6 (admin): Mostrar lista de servicios

Muestra todos los servicios registrados.
```
Choose your admin option: 6

***************************

List of available services:

- Appointment
- Surgery
- Vaccination
- Salon

Press enter to continue.
```
#### Opción 7 (admin): Mostrar registro completo

Esta opción es similar a la que imprime la información de clientes y mascotas registradas, pero también muestra los veterinarios, servicios y todas las citas agendadas.

```
Choose your admin option: 7

*********************************************************

Registered data

----------
Clients
----------
ID: 1 - Name: Lindsey - Contact: 3111234567 - Address: Barranquilla - List of pets: [Shiro, Nino]
ID: 2 - Name: Sharon - Contact: 1234567890 - Address: Barranquilla 2 - List of pets: [Melania]

----------
Pets
----------

Name: Shiro - Species: Cat - Breed: Grey - Age: 3 - Owner: Lindsey
Veterinary Log: [Date: 2025-01-27 - Time: 10:00:00 - Service: Surgery - Veterinarian: William
]

Name: Nino - Species: Cat - Breed: Brown - Age: 2 - Owner: Lindsey
Veterinary Log: [Date: 2025-02-02 - Time: 10:30:00 - Service: Appointment - Veterinarian: Ruby
, Date: 2025-01-30 - Time: 14:00:00 - Service: Vaccination - Veterinarian: William
]

Name: Melania - Species: Dog - Breed: Yorkshire - Age: 7 - Owner: Sharon
Veterinary Log: [Date: 2025-02-10 - Time: 12:30:00 - Service: Salon - Veterinarian: John
]

----------
Appointments
----------
Date: 2025-01-27 - Time: 10:00:00 - Pet: Shiro - Service: Surgery - Veterinarian: William

Date: 2025-02-02 - Time: 10:30:00 - Pet: Nino - Service: Appointment - Veterinarian: Ruby

Date: 2025-01-30 - Time: 14:00:00 - Pet: Nino - Service: Vaccination - Veterinarian: William

Date: 2025-02-10 - Time: 12:30:00 - Pet: Melania - Service: Salon - Veterinarian: John


----------
Veterinarians
----------
Name: Ruby - Contact: 2831836783 - Service Provided: ['Appointment', 'Salon']
Name: John - Contact: 1982441243 - Service Provided: ['Salon']
Name: William - Contact: 9871206348 - Service Provided: ['Appointment', 'Vaccination']

----------
Services
----------
Appointment
Vaccination
Salon

*********************************************************

Press enter to continue.
```

### Base de datos

Por medio del uso de la librería pickle se logra la persistencia de datos, por lo que al iniciar la aplicación, se puede volver a cargar la información con la que se había trabajado anteriormente. Esta base de datos se guarda en el archivo `veterinary_database.txt`.

### Versión de Python

Desarrollado en Python 3.13.0.

### Funciones del programa 
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


