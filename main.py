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
    def cancelAppointment(self):
        pass

    @abstractmethod
    def displayPetInfo(self):
        pass

    @abstractmethod
    def displayVeterinaryLog(self):
        pass

class Appointments(ABC):
    def __init__(self,date, time, pet, service, veterinarian):
        self.date = date
        self.time = time
        self.pet = pet
        self.service = service
        self.veterinarian = veterinarian

    @abstractmethod
    def modifyAppointment(self):
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
class FactoryOfPeople():
    @staticmethod
    def createPerson(Type,**kwargs):
        if Type == "Client":
            return Client(**kwargs)
        elif Type == "Veterinarian":
            return Veterinarian(**kwargs)
        else:
            raise ValueError(f"Type {Type} doesn't exist")

############ Class to create appointments
class Appointment(Appointments):
    # It should have the following methods: 
    # constructor (this is inherited), attributes are: date, time, pet, service, veterinarian
    # modifyAppointment
    # displayAppointmentInfo
    def modifyAppointment(self, **kwargs):
        for key,value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key, value)

    def displayAppointmentInfo(self):
        return f"\nDate: {self.date}\nTime: {self.time}\nPet: {self.pet}\nService: {self.service}\nVeterinarian: {self.veterinarian}"

############# Class to create pets

class Pet(Pets):
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a client), attributes are: name, species, breed, age, owner, veterinary_log
    # scheduleAppointment
    # cancelAppointment
    # displayPetInfo
    # displayVeterinaryLog
    
    def __init__(self,name, species, breed, age, owner):
        super().__init__(name, species, breed, age, owner)
        self.veterinaryLog = [] # This is going to be a list containing objects "Appointment"

    def scheduleAppointment(self, appointmentDetails: Appointment):
        self.veterinaryLog.append(appointmentDetails)

    def cancelAppointment(self,appointmentToDelete):
        del self.veterinaryLog[appointmentToDelete-1]
    
    def displayPetInfo(self):
        return f"\nPet information: \nName: {self.name}\nSpecies: {self.species}\nBreed: {self.breed}\nAge: {self.age}\nOwner: {self.owner}"

    def displayVeterinaryLog(self):
        for log in self.veterinaryLog:
            print(f"\nDate: {log.date}\nTime: {log.time}\nService: {log.service}\nVeterinarian: {log.veterinarian}")

############# Class for veterinary management system, this could use the "singleton" pattern

class VeterinaryMgmtSys():
    _instance = None

    def __new__(cls,*args,**kwargs):   
        if not cls._instance:
            cls._instance = super(VeterinaryMgmtSys, cls)._new_(cls)
        return cls._instance
    
    # Remaining functions
    def createDatabase(self,listOfClients,listOfPets,listofVeterinarians,listOfAppointments):
        self.listOfClients = []
        self.listOfPets = []
        self.listofVeterinarians = []
        self.listOfAppointments = []
        # [0] is a list of clients, attributes are: name, contact, address, list_of_pets
        # [1] is a list of pets, attributes are: name, species, breed, age, owner, veterinary_log
        # [2] is a list of veterinarians, attributes are: name, contact, service_provided
        # [3] is a list of appointments for all pets, attributes are: date, time, pet, service, veterinarian
