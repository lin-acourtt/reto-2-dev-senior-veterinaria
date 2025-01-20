from abc import ABC, abstractmethod

# Database:
# [0] is a list of clients, attributes are: name, contact, address, list_of_pets
# [1] is a list of pets, attributes are: name, species, breed, age, owner, veterinary_log
# [2] is a list of veterinarians, attributes are: name, contact, service_provided
# [3] is a list of appointments for all pets, attributes are: date, time, pet, service, veterinarian


############# Abstract classes (Their names are in plural, children classes will have names in singular)
clientes = []

class People(ABC):
    id_counter = 1
    @abstractmethod
    def __init__(self,name,contact):
        self.id = People.id_counter
        self.name = name
        self.contact = contact
        
        People.id_counter += 1 # nos va incrementando cada vez que guardamos una people. 
        
    
    @abstractmethod
    def displayContactInfo(self):
        print(f"Id people: {self.id}")
        print(f"name people: {self.name}")
        print(f"contact: {self.contact}")

class Pets(ABC):
    @abstractmethod
    def __init__(self,name, species, breed, age, owner):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner = owner
    
    @abstractmethod
    def scheduleAppointment(self):
        pass

    @abstractmethod
    def displayPetInfo(self):
        pass

    @abstractmethod
    def displayVeterinaryLog(self):
        pass

class Appointments(ABC):
    @abstractmethod
    def __init__(self,date, time, pet, service):
        self.date = date
        self.time = time
        self.pet = pet
        self.service = service

    @abstractmethod
    def modifyAppointment(self):
        pass

    @abstractmethod
    def cancelAppointment(self):
        pass

    @abstractmethod 
    def displayAppointmentInfo(self):
        pass

############# Classes for "Client" and "Veterinarian" (Use "factory method" pattern)

class Client(People):
    
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a pet), attributes are: name, contact, address, list_of_pets
    # displayContactInfo
    
    def __init__(self, name, contact, address, list_of_pets):
        super().__init__(name, contact)
        self.address = address
        self.list_of_pets = list_of_pets
        
        if not self.list_of_pets:
            self.list_of_pets = []
            
        
        # super().displayContactInfo()    
        
    def displayContactInfo(self):
        return super().displayContactInfo()    
        print(f"Address: {self.address}")
        print(f"Pets: {len(self.list_of_pets)} pets(s)")
    
    
    
    
    
    
    
class Veterinarian(People):
    
    # It should have the following methods: 
    # constructor, attributes are: name, contact, service_provided
    # displayContactInfo
    
    def __init__(self, name, contact, service_provided):
        super().__init__(name, contact)
        self.service_provided = service_provided
        
        
        # super().displayContactInfo()    
        
    def displayContactInfo(self):
        # Override to include service provided information
        super().displayContactInfo()
        print(f"Service Provided: {self.service_provided}")
        
        
    
    
    
class Factory():
    pass

############# Class to create pets

class Pet(Pets):
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a client), attributes are: name, species, breed, age, owner, veterinary_log
    # scheduleAppointment
    # displayPetInfo
    # displayVeterinaryLog
    pass

############ Class to create appointments

class Appointment(Appointments):
    # It should have the following methods: 
    # constructor, attributes are: date, time, pet, service, veterinarian
    # modifyAppointment
    # cancelAppointment
    # displayAppointmentInfo
    pass

############# Class for veterinary management system, this could use the "singleton" patter

class VeterinaryMgmtSys():
    pass


# #menu Principal
# def menu_principal():
#     while True:
#         print("=========Menu Principal ===================")
#         print("1. Registrar cliente y mascota")
#         print("2. Programacion  de cita")
#         print("3. consultar historial de servicios")
#         print("4. Salir")
#         opc = input("Seleccione una opcion: ")
#         if opc =="1":
#             registrar_cliente()
#         elif opc == "2":
#             programar_cita() 
#         elif opc == "3":
#             pass        
#         elif opc == "4":
#             break        
#         else:
#             print("Opcion no valida. Intente de nuevo")
            
            
        


# menu_principal()

