from abc import ABC, abstractmethod
from datetime import datetime
import os.path
import pickle

# Database:
# [0] is a list of clients, attributes are: id, name, contact, address, list_of_pets
# [1] is a list of pets, attributes are: name, species, breed, age, owner, veterinary_log
# [2] is a list of veterinarians, attributes are: name, contact, service_provided
# [3] is a list of appointments for all pets, attributes are: date, time, pet, service, veterinarian
# [4] is a list of services


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
        pass

class Pets(ABC):
    @abstractmethod
    def __init__(self,name, species, breed, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
    
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
    
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a pet), attributes are: name, contact, address, list_of_pets
    # displayContactInfo
    
    def __init__(self, name, contact, address):
        super().__init__(name, contact)
        self.address = address
        self.list_of_pets = []

    def displayContactInfo(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"contact: {self.contact}")
        print(f"address: {self.address}")
        print(f"list of pets: {self.list_of_pets}")

    def __str__(self):
        return f"Id: {self.id} - Name: {self.name} - contact: {self.contact} - address: {self.address} - list of pets: {self.list_of_pets}"
    
    def __repr__(self):
        return f"Name: {self.name}"  
class Veterinarian(People):
    
    # It should have the following methods: 
    # constructor, attributes are: name, contact, service_provided
    # displayContactInfo
    
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.service_provided = []
                
        # super().displayContactInfo()    
        
    def displayContactInfo(self):
        print(f"\nName: {self.name} \nContact: {self.contact} \nService Provided: {self.service_provided}")

    def __str__(self):        
        return f"Name: {self.name} - Contact: {self.contact} - Service Provided: {self.service_provided}"
    
    def __repr__(self):
        return self.name
 
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
        return f"\nDate: {self.date}\nTime: {self.time}\nPet: {self.pet.name}\nService: {self.service}\nVeterinarian: {self.veterinarian.name}"

    def __str__(self):
        return f"Date: {self.date} - Time: {self.time} - Pet: {self.pet.name} - Service: {self.service} - Veterinarian: {self.veterinarian.name}"

    def __repr__(self):
        return f"Date: {self.date} - Time: {self.time} - Service: {self.service} - Veterinarian: {self.veterinarian.name}"

############# Class to create pets

class Pet(Pets):
    # It should have the following methods: 
    # constructor (the constructor should force the creation of a client), attributes are: name, species, breed, age, owner, veterinary_log
    # scheduleAppointment
    # cancelAppointment
    # displayPetInfo
    # displayVeterinaryLog
    
    def __init__(self,name, species, breed, age):
        super().__init__(name, species, breed, age)
        self.owner = []
        self.veterinaryLog = [] # This is going to be a list containing objects "Appointment"

    def scheduleAppointment(self, appointmentDetails: Appointment):
        self.veterinaryLog.append(appointmentDetails)

    def cancelAppointment(self,appointmentToDelete):
        del self.veterinaryLog[appointmentToDelete-1]
    
    def displayPetInfo(self):
        print(f"Pet information: \nName: {self.name}\nSpecies: {self.species}\nBreed: {self.breed}\nAge: {self.age}\nOwner: {self.owner}")

    def displayVeterinaryLog(self):
        for log in self.veterinaryLog:
            print(f"\nDate: {log.date}\nTime: {log.time}\nService: {log.service}\nVeterinarian: {log.veterinarian}")

    def __str__(self):
        return f"Name: {self.name} - Species: {self.species} - Breed: {self.breed} - Age: {self.age} - Owner: {self.owner.name} \nVeterinary Log: {self.veterinaryLog}"

    def __repr__(self):
        return f"{self.name}"  
    
class Associate():
    @staticmethod
    def petToOwner(client: Client, *petslist: Pet):
        for pet in petslist:
            client.list_of_pets.append(pet)

    @staticmethod
    def ownerToPet(pet: Pet, client: Client):
        pet.owner = client

    @staticmethod
    def serviceToVet(vet: Veterinarian, *services):
        for service in services[0]:
            vet.service_provided.append(service)

############# Class for veterinary management system, this could use the "singleton" pattern

class VeterinaryMgmtSys():
    _instance = None

    personGenerator = FactoryOfPeople()

    def __new__(cls,*args,**kwargs):   
        if not cls._instance:
            cls._instance = super(VeterinaryMgmtSys, cls).__new__(cls)
        return cls._instance
    
    # Remaining functions
    def createDatabase(self,listOfClients,listOfPets,listofVeterinarians,listOfAppointments,listOfServices):
        self.listOfClients = listOfClients
        self.listOfPets = listOfPets
        self.listofVeterinarians = listofVeterinarians
        self.listOfAppointments = listOfAppointments
        self.listOfServices = listOfServices
        # [0] is a list of clients, attributes are: id, name, contact, address, list_of_pets
        # [1] is a list of pets, attributes are: name, species, breed, age, owner, veterinary_log
        # [2] is a list of veterinarians, attributes are: name, contact, service_provided
        # [3] is a list of appointments for all pets, attributes are: date, time, pet, service, veterinarian
        # [4] is a list of services

    # Option 1
    def registerClient(self):
        input("Please input the pet owner data: ")
        name = input("Name: ")
        contact = input("Phone contact: ")
        address = input("Address: ")

        registeredClient = VeterinaryMgmtSys.personGenerator.createPerson("Client",name=name,contact=contact,address=address)
        #self.listOfClients.append(registeredClient)
        return registeredClient
    
    # Option 2
    def registerPet(self):
        input("Please input the pet data: ")
        name = input("Name: ")
        species = input("Species: ")
        breed = input("Breed: ")
        age = input("Age: ")
        #owner = input("Owner: ") # Change to ask if the owner is new or existing

        registeredPet = Pet(name,species,breed,age)
        #self.listOfPets.append(registeredPet)
        return registeredPet

    # Option 3
    def schedulePetAppmt(self):
        input("Specify appointment details -->")
        pet = input("For which pet?: ").strip()
        owner = input("Owner: ").strip()
        
        #Generate a list of pets and their owners
        petsAndOwnerRelation = False
        while petsAndOwnerRelation == False:
            for indexPet, memberpet in enumerate(self.listOfPets):
                if (pet.lower() == memberpet.name.lower()) and (owner.lower() == memberpet.owner.name.lower()):
                    petsAndOwnerRelation = True
                    break
        
        # This should be a try/except, maybe?
        if petsAndOwnerRelation == True:
            # Continue taking the information for the appointment
            date = input("Date (AAAA-MM-DD): ").strip()
            time = input("Time (HH:MM): ").strip()
            
            date = datetime.strptime(date, "%Y-%m-%d")
            # This line will convert the datetime object to a date object
            date = datetime.date(date)
            
            time = datetime.strptime(time, "%H:%M")
            # This line will convert the datetime object to a time object
            time = datetime.time(time)

            print("Select a service:")
            for indexService, availableServices in enumerate(self.listOfServices):
                print(f"{indexService+1}. {availableServices}")
            
            service = self.listOfServices[int(input("Type of service (enter the number): ").strip())-1]
            
            # Find veterinaries that match this service
            availableVets = []
            for indexVet, vet in enumerate(self.listofVeterinarians):
                if service in vet.service_provided:
                    availableVets.append([indexVet,vet])

            print("Select a veterinarian:")
            for indexAvaVet, vet in enumerate(availableVets):
                print(f"{indexAvaVet+1}. {vet[1].name}")
            
            indexVetInput = int(input("Vet (enter the number): ").strip())-1
            veterinarian = availableVets[indexVetInput][1]

            appointment = Appointment(date, time, self.listOfPets[indexPet], service, veterinarian)
            self.listOfPets[indexPet].veterinaryLog.append(appointment)
            self.listOfAppointments.append(appointment)
            return appointment
        else:
            print("Pet and owner are not related.")
    
    # Option 4
    def modifyPetAppmt(self):
        pass
    
    # Option 5
    def cancelPetAppmt(self):
        pass

    # Option 6
    def checkPetVeterinaryLog(self):
        pass
    
    #************************************+
    # Admin Option 1
    def __registerVet(self):
        input("Please input the veterinarian data-->")
        name = input("Name: ")
        contact = input("Phone contact: ")
        
        registeredVet = VeterinaryMgmtSys.personGenerator.createPerson("Veterinarian",name=name,contact=contact)
        
        # Add service to the vet, modify this part
        # to allow only available services
        service_provided = []
        while True:
            service = input("Service: ")
            service_provided.append(service)
            checkpoint = input("Keep adding services? (y/n): ")
            if checkpoint == "n":
                break

        addService = Associate()
        addService.serviceToVet(registeredVet,service_provided)

        self.listofVeterinarians.append(registeredVet)
        return registeredVet
    # Admin Option 2
    def __removeVet(self):
        pass
    # Admin Option 3
    def __displayListOfVets(self):
        pass
    # Admin Option 4
    def __registerServiceType(self):
        serviceType = input("Type the name of the service: ")
        self.listOfServices.append(serviceType)
        print("Service successfully registered.")
    # Admin Option 5
    def __removeServiceType(self):
        pass
    # Admin Option 6
    def __displayListOfServices(self):
        pass


    def main_menu(self):
        while True:
            print("========= main menu ===================")
            print("1. Register client") # This is supposed to force the registration of a pet as well
            print("2. Register pet") # This is supposed to force the registration of its owner as well
            print("3. Schedule appointment")
            print("4. Modify appointment")
            print("5. Cancel appointment")
            print("6. Check veterinary log for a pet")
            print("7. Admin access")
            print("8. Exit")
            print("9. Tests")
            opt = input("Choose an option: ")
            if opt =="1":
                #1. Register client
                client = self.registerClient()

                print("You will now associate pets to this client: ")
                # Temporary list of pets
                tempPetList = []
                while True:
                    # Modify to check for existing pets
                    pet = self.registerPet()
                    # Associate Pet to Owner
                    joinPetOwner = Associate()
                    joinPetOwner.petToOwner(client,pet)
                    # Associate Owner to Pet
                    joinPetOwner.ownerToPet(pet,client)
                    tempPetList.append(pet)
                    checkpoint = input("Add more pets? (y/n): ")
                    if checkpoint == "n":
                        break
                
                self.listOfClients.append(client)
                for tempPet in tempPetList:
                    self.listOfPets.append(tempPet)
            elif opt == "2":
                #2. Register pet
                pet = self.registerPet()
                
                print("You will now associate an owner to this pet: ")
                
                # Modify to check for existing owners
                client = self.registerClient()
                # Associate Owner to Pet
                joinPetOwner = Associate()
                joinPetOwner.ownerToPet(pet,client)
                # Associate Pet to Owner
                joinPetOwner.petToOwner(client,pet)
                    
                self.listOfClients.append(client)
                self.listOfPets.append(pet)
                
            elif opt == "3":
                #3. Schedule appointment
                self.schedulePetAppmt()
                pass   
            elif opt == "4":
                #4. Modify appointment
                self.modifyPetAppmt()
                pass
            elif opt == "5":
                #5. Cancel appointment
                self.cancelPetAppmt()
                pass     
            elif opt == "6":
                #6. Check veterinary log for a pet
                self.checkPetVeterinaryLog()
                pass    
            elif opt == "7":
                #7. Admin access

                # Request for password
                pw = input("Enter the password: ")
                if pw == "dev-senior":
                    while True:
                        print("*** Admin menu ***")
                        print("1. Register veterinarian")
                        print("2. Remove veterinarian")
                        print("3. Display list of veterinarians")
                        print("4. Register type of service")
                        print("5. Remove type of service")
                        print("6. Display list of services")
                        print("7. Return")
                        admin_opt = input("Choose your admin option: ")
                        if admin_opt == "1":
                            #1. Register veterinarian
                            self.__registerVet()
                        elif admin_opt == "2":
                            # 2. Remove veterinarian
                            self.__removeVet()
                        elif admin_opt == "3":
                            #3. Display list of veterinarians
                            self.__displayListOfVets()
                        elif admin_opt == "4":
                            #4. Register type of service
                            self.__registerServiceType()
                        elif admin_opt == "5":
                            #5. Remove type of service
                            self.__removeServiceType()
                        elif admin_opt == "6":
                            #6. Display list of services
                            self.__displayListOfServices()
                        elif admin_opt == "7":
                            #5. Return
                            break
                        else:
                            print("Invalid option.")
                else:
                    print("\nIncorrect password")
                    print("Press Enter to continue.")
                    continue
            elif opt == "8":
                #8. Exit
                print("Thanks for using this service.")
                break    
            elif opt == "9":
                self.tests()
            else:
                print("Option is not valid, please try again.")
    
    
    def tests(self):
        print("Registered data")
        print("----------")
        print("Clients")
        for client in self.listOfClients:
            print(client)
        print("----------")
        print("Pets")
        for pet in self.listOfPets:
            print(pet)
        print("----------")
        print("Veterinarians")
        for vet in self.listofVeterinarians:
            print(vet)
        print("----------")
        print("Appointments")
        for appointment in self.listOfAppointments:
            print(appointment) 
        print("----------")
        print("Services")
        for service in self.listOfServices:
            print(service)

if __name__ == "__main__":

    # Create the object for the management system
    veterinaryManagementSys = VeterinaryMgmtSys()

    # Create database for the management system (empty for now)
    if os.path.exists("veterinary_database.txt"):
        f = open("veterinary_database.txt","rb")
        database = pickle.load(f)
        print("Database imported")
        veterinaryManagementSys.createDatabase(database[0],database[1],database[2],database[3],[4])
        f.close()
    else:
        veterinaryManagementSys.createDatabase([],[],[],[],[])
    
    veterinaryManagementSys.main_menu()
            
        


# main_menu()

