from abc import ABC, abstractmethod

# Database:
# [0] is a list of clients, attributes are: name, contact, address, list_of_pets
# [1] is a list of pets, attributes are: name, species, breed, age, owner, veterinary_log
# [2] is a list of veterinarians, attributes are: name, contact, service_provided
# [3] is a list of appointments for all pets, attributes are: date, time, pet, service, veterinarian


############# Abstract classes (Their names are in plural, children classes will have names in singular)

class People(ABC):
    @abstractmethod
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    
    @abstractmethod
    def displayContactInfo(self):
        pass

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
    pass
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a pet), attributes are: name, contact, address, list_of_pets
    # displayContactInfo
class Veterinarian(People):
    pass
    # It should have the following methods: 
    # constructor, attributes are: name, contact, service_provided
    # displayContactInfo
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