from abc import ABC, abstractmethod # To create interfaces
from datetime import datetime       # To manage date and time
import os.path                      # To check if the database file exists in the folder
import pickle                       # To load/save database
from getpass import getpass         # To type passwords

# The dabase is file: veterinary_database.txt, it contains a list called "database"
# Position in database:
# [0] is a list of clients, attributes are: id, name, contact, address, list_of_pets (object)
# [1] is a list of pets, attributes are: name, species, breed, age, owner (object), veterinary_log (object)
# [2] is a list of veterinarians, attributes are: name, contact, service_provided
# [3] is a list of appointments for all pets, attributes are: date, time, pet (object), service, veterinarian
# [4] is a list of services


############# Abstract classes (Their names are in plural, children classes will have names in singular)

# Abstract class used to create people (Client and Veterinarian)
class People(ABC):
    
    @abstractmethod # Constructor
    def __init__(self):
        pass 
        
    @abstractmethod # Display the person's informartion
    def displayContactInfo(self):
        pass

# Abstract class used to create pets
class Pets(ABC):

    @abstractmethod # Constructor
    def __init__(self):
        pass
    
    @abstractmethod # Schedule appointment
    def scheduleAppointment(self):
        pass

    @abstractmethod # Cancel appointment
    def cancelAppointment(self):
        pass

    @abstractmethod # Display pet's info
    def displayPetInfo(self):
        pass

    @abstractmethod # Display veterinary log for pet
    def displayVeterinaryLog(self):
        pass

# Abstract class used to create pets
class Appointments(ABC):

    @abstractmethod # Constructor
    def __init__(self):
        pass

    @abstractmethod # Modify appointment
    def modifyAppointment(self):
        pass

    @abstractmethod # Display appointment information
    def displayAppointmentInfo(self):
        pass

############# Children classes for "Client" and "Veterinarian"

# Class used to describe clients
class Client(People):
    
    def __init__(self, name, contact, address, id): # Constructor
        self.name = name # string
        self.contact = contact # string
        self.address = address # string
        self.id = id # int
        self.list_of_pets = [] # This list contains object of type "Pet"

    def displayContactInfo(self): # Display client's information
        print(f"\nID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")
        print(f"List of pets: {self.list_of_pets}") # Method __repr__ is defined in "Pet" to display only the name in this list

    def addPet(self,newPet): # Append pet to list of pets
        self.list_of_pets.append(newPet)

    def __str__(self): # Used to display the client's information when calling "print()" on the object
        return f"ID: {self.id} - Name: {self.name} - Contact: {self.contact} - Address: {self.address} - List of pets: {self.list_of_pets}"
    
    def __repr__(self): # Used to display the client's name in a list, when the list contains "Client" objects
        return f"Client Name: {self.name}"  

# Class used to describe veterinarians
class Veterinarian(People):
    
    def __init__(self, name, contact): # Constructor
        self.name = name # string
        self.contact = contact # string
        self.service_provided = [] # list of strings
        
    def displayContactInfo(self): # Display veterinarian information
        print(f"\nName: {self.name} \nContact: {self.contact} \nService Provided: {self.service_provided}")

    def addService(self,new_service): # Add service to Vet
        self.service_provided.append(new_service)

    def __str__(self): # Used to display the vet's information when calling "print()" on the object    
        return f"Name: {self.name} - Contact: {self.contact} - Service Provided: {self.service_provided}"
    
    def __repr__(self): # Used to display the vet's name in a list, when the list contains "Veterinarian" objects
        return f"Vet Name: {self.name}"
 
 # Factory design pattern is used here to generate Clients and Veterinarians
class FactoryOfPeople():
    @staticmethod
    def createPerson(Type,**kwargs):
        if Type == "Client":
            return Client(**kwargs)
        elif Type == "Veterinarian":
            return Veterinarian(**kwargs)
        else:
            raise ValueError(f"Type {Type} doesn't exist")

############# Child class for "Appointment"(singular)
class Appointment(Appointments):
    
    def __init__(self, date, time, pet, service, veterinarian): # Constructor
        self.date = date # date object
        self.time = time # time object
        self.pet = pet # Pet object
        self.service = service # string
        self.veterinarian = veterinarian # Veterinarian object

    def modifyAppointment(self, **kwargs): # Modify appointment
        # A set of key:value is accepted as a parameter, it the key exists as an attribute of the class
        # The value is set for this attribute
        for key,value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key, value)

    def displayAppointmentInfo(self): # Display appointment's information
        return f"\nDate: {self.date}\nTime: {self.time}\nPet: {self.pet.name}\nService: {self.service}\nVeterinarian: {self.veterinarian.name}"

    def __str__(self): # Used to display the appointment's information when calling "print()" on the object    
        return f"Date: {self.date} - Time: {self.time} - Pet: {self.pet.name} - Service: {self.service} - Veterinarian: {self.veterinarian.name}\n"

    def __repr__(self): # Used to display the appointment's details, when the list contains "Appointment" objects
        return f"Date: {self.date} - Time: {self.time} - Service: {self.service} - Veterinarian: {self.veterinarian.name}\n"

############# Child class for "Pet"
class Pet(Pets):
    
    def __init__(self,name, species, breed, age): # Constructor
        self.name = name # string
        self.species = species # string
        self.breed = breed # string
        self.age = age # int
        self.owner = [] # List of "Client" objects
        self.veterinaryLog = [] # List of "Appointment" objects

    def scheduleAppointment(self, appointmentDetails): # Schedule appointment
        self.veterinaryLog.append(appointmentDetails)

    def cancelAppointment(self,appointmentToDelete): # Cancel appointment
        del self.veterinaryLog[appointmentToDelete-1]
    
    def displayPetInfo(self): # Display Pet's information
        print(f"\nName: {self.name}\nSpecies: {self.species}\nBreed: {self.breed}\nAge: {self.age}\nOwner: {self.owner}")

    def displayVeterinaryLog(self): # Display the list of appointment for this pet
        for log in self.veterinaryLog:
            print([log])
            #print(f"\nDate: {log.date}\nTime: {log.time}\nService: {log.service}\nVeterinarian: {log.veterinarian}")
    
    def addOwner(self,newOwner): # Add owner to pet
        if self.owner:
            input("This pet already has an owner (Enter to return)")
            return
        else:
            self.owner = newOwner

    def __str__(self): # Used to display the client's information when calling "print()" on the object
        return f"Name: {self.name} - Species: {self.species} - Breed: {self.breed} - Age: {self.age} - Owner: {self.owner.name} \nVeterinary Log: {self.veterinaryLog}"

    def __repr__(self): # Used to display the client's name in a list, when the list contains "Client"s objects
        return f"{self.name}"  

############# Class for veterinary management system

class VeterinaryMgmtSys():
    
    _instance = None
    personGenerator = FactoryOfPeople()

    def __new__(cls,*args,**kwargs): # Singleton pattern is used here to create a single instance of the veterinary management system
        if not cls._instance:
            cls._instance = super(VeterinaryMgmtSys, cls).__new__(cls)
        return cls._instance
    
    def createDatabase(self,listOfClients,listOfPets,listofVeterinarians,listOfAppointments,listOfServices):
        # Used to create the database the management system should consider to start the application
        self.listOfClients = listOfClients # List of clients (objects) that have been registed
        self.listOfPets = listOfPets # List of pets (objects) that have been registered
        self.listofVeterinarians = listofVeterinarians # List of available veterinarians (object)
        self.listOfAppointments = listOfAppointments # List of appointments (objects) that have been scheduled for all pets
        self.listOfServices = listOfServices # List of services (string) available in the veterinary

    def registerClient(self): # Option 1 in the main menu
        print("\n---------------------------------------------------")
        input("Please input the pet owner data (Enter to continue)")
        name = input("\nClient's name: ").strip()
        contact = input("Phone contact: ").strip()
        address = input("Address: ").strip()

        if self.listOfClients:
            id = self.listOfClients[-1].id + 1
        else:
            id = 1

        # Generate Client object (The list of pets will be updated once the pet is created)
        registeredClient = VeterinaryMgmtSys.personGenerator.createPerson("Client",name=name,contact=contact,address=address,id=id)
        input("\nClient successfully registered. (Enter to continue)")
        return registeredClient
    
    def registerPet(self): # Option 2 in the main menu
        input("\nPlease input the pet data (Enter to continue)")
        name = input("\nPet's name: ").strip()
        species = input("Species: ").strip()
        breed = input("Breed: ").strip()
        age = int(input("Age: ").strip())
        
        # Generate Pet object, the owner will be updated once it is generated
        registeredPet = Pet(name,species,breed,age)
        input("\nPet successfully registered. (Enter to continue)")
        return registeredPet

    def schedulePetAppmt(self): # Option 3 in the main menu
        
        if not self.listOfClients or not self.listOfPets:
            print("\nThere are not pets or clients registered")
            input("You will be returned to the main menu (Enter to continue)")
            return

        if not self.listOfServices:
            print("\nThere are not available services to schedule an appointment.")
            input("You will be returned to the main menu (Enter to continue)")
            return
        
        if not self.listofVeterinarians:
            print("\nThere are not available veterinarians to schedule an appointment.")
            input("You will be returned to the main menu (Enter to continue)")
            return

        print("\n-----------------------------------------------")
        input("Specify appointment details (Enter to continue)")
        pet = input("\nType the pet's name: ").strip()
        owner = input("Owner: ").strip()
        
        #Generate a list of pets and their owners
        petsAndOwnerRelation = False
        while petsAndOwnerRelation == False:
            for indexPet, memberpet in enumerate(self.listOfPets):
                if (pet.lower() == memberpet.name.lower()) and (owner.lower() == memberpet.owner.name.lower()):
                    petsAndOwnerRelation = True
                    break
        
        if petsAndOwnerRelation == False:
            print(f"\nThe pet {pet} and owner {owner} are not related.")
            input("You will be returned to the main menu (Enter to continue)")
            return

        # The list of available services is displayed
        print("\nList of available services:")
        for indexService, availableServices in enumerate(self.listOfServices):
            print(f"{indexService+1}. {availableServices}")
        
        service = self.listOfServices[int(input("\nSelect a service (enter the number): ").strip())-1]

        # Find veterinaries that match this service
        availableVets = []
        for indexVet, vet in enumerate(self.listofVeterinarians):
            if service in vet.service_provided:
                availableVets.append([indexVet,vet])

        if not availableVets:
            print(f"\nThere are not veterinarians for the service: {service}.")
            input("You will be returned to the main menu (Enter to continue)")
            return

        print("\nList of available veterinarians:")
        for indexAvaVet, vet in enumerate(availableVets):
            print(f"{indexAvaVet+1}. {vet[1].name}")
        
        indexVetInput = int(input("\nSelect a veterinarian (enter the number): ").strip())-1
        veterinarian = availableVets[indexVetInput][1] ## Why?

        # Continue taking the information for the appointment
        date = input("Date (AAAA-MM-DD): ").strip()
        time = input("Time (HH:MM): ").strip()
        
        # The datetime library is used to generate a datetime object for the date
        date = datetime.strptime(date, "%Y-%m-%d")
        # This line will convert the datetime object to a date-only object
        date = datetime.date(date)
        
        # The datetime library is used to generate a datetime object for the time
        time = datetime.strptime(time, "%H:%M")
        # This line will convert the datetime object to a time-only object
        time = datetime.time(time)

        appointment = Appointment(date, time, self.listOfPets[indexPet], service, veterinarian)
        self.listOfPets[indexPet].veterinaryLog.append(appointment) # Veterinary log is updated for the pet
        self.listOfAppointments.append(appointment) # General list of appointments in updated
        input(f"\nAppointment successfully registered for pet {pet}. (Enter to continue)")
        return appointment
        
    def modifyPetAppmt(self): # Option 4 in main menu
        pet_name = input("Enter the pet's name to modify its appointment: ").strip()
        pet_found = False
        
        for pet in self.listOfPets:
            if pet.name == pet_name:
                pet_found = True
                
                # Verificar si el dueño que intenta modificar la cita es el propietario de la mascota
                owner_name = input(f"Enter the owner's name for {pet.name}: ").strip()

                if owner_name.lower() != pet.owner.name.lower():
                    print(f"Error: {owner_name} is not the owner of {pet.name}. You cannot modify this appointment.")
                    return  # Salir si el dueño no es correcto
            
                print(f"Appointments for {pet.name}:")
                for i, appointment in enumerate(pet.veterinaryLog):
                    print(f"{i+1}. {appointment.displayAppointmentInfo()}")
                    
                    
                try:    
                    appointment_index = int(input("Select the appointment to modify (enter the number): ").strip()) - 1
                    appointment_to_modify = pet.veterinaryLog[appointment_index]

                    # Modify the appointment
                    print("Modify appointment details:")
                    
                    #modify date
                    new_date = input(f"Current Date: {appointment_to_modify.date}. Enter new date (YYYY-MM-DD) or preess Enter to Keep: ").strip()
                    if new_date == "":
                        new_date = appointment_to_modify.date 
                    else:
                        new_date = datetime.strptime(new_date, "%y-%m-%d")    
                        
                    #modifi time
                    new_time = input(f"Current Time: {appointment_to_modify.time}. Enter new time (HH:MM) or prees Enter to keep: ").strip()
                    if new_time =="": # no input keept the same
                        new_time = appointment_to_modify.time
                    else:    
                        new_time = datetime.strptime(new_time, "%H:%M").time()
                    
                    #modify service
                    new_service = input(f"Current Service: {appointment_to_modify.service}. Enter new service or press Enter to keep: ").strip()
                    if new_service =="":
                        new_service = appointment_to_modify.service
                        
                    #modify veterinarian
                    new_veterinarian_name = input(f"Current Veterinarian: {appointment_to_modify.veterinarian}. Enter new veterinaria or press Enter to Keep: ").strip()
                    if new_veterinarian_name == "":
                        new_veterinarian = appointment_to_modify.veterinarian
                    else:    
            # Ensure new veterinarian exists
                        new_veterinarian = None
                        for vet in self.listofVeterinarians:
                            if vet.name.lower() == new_veterinarian_name.lower():
                                new_veterinarian = vet
                                break

                        if not new_veterinarian:
                            print("Error: Veterinarian not found.")
                            return                

                    # new_date = datetime.strptime(new_date, "%Y-%m-%d")
                    # new_time = datetime.strptime(new_time, "%H:%M").time()

                    # Update the appointment
                    appointment_to_modify.modifyAppointment(date=new_date, time=new_time, service=new_service, veterinarian=new_veterinarian)
                    print("Appointment modified successfully!")
                except (ValueError, IndexError):
                    print("Invalid input. Please make sure to select a valid appointment number.")    
                break
        
        ###S: Only the appointment object is being updated... it also needs to be updated in the pet's veterinary log
        if not pet_found:
            print("Pet not found.")
    
    # Option 5
    def cancelPetAppmt(self):
        pet_name = input("Enter the pet's name to cancel its appointment: ").strip()
        pet_found = False
        for pet in self.listOfPets:
            if pet.name == pet_name:
                pet_found = True
                
                owner_name = input(f"Enter the owner's name for {pet.name}: ").strip()
                
                if owner_name.lower() != pet.owner.name.lower():
                    print(f"Error: {owner_name} is not the owner of {pet.name}. You cannot cancel this appointment.")
                    return 
                
                
                print(f"Appointments for {pet.name}:")
                for i, appointment in enumerate(pet.veterinaryLog):
                    print(f"{i+1}. {appointment.displayAppointmentInfo()}")
                    
                try:    
                    appointment_index = int(input("Select the appointment to cancel (enter the number): ").strip()) - 1
                    # Delete the appointment from the veterinary log
                    pet.cancelAppointment(appointment_index + 1)
                    print("Appointment cancelled successfully!")
                except (ValueError, IndexError):
                    print("Input invalid. Select a valid appointment number")    

                break
        
        ###S: The appointment is being deleted only in the pet's veterinary log, it should also be deleted from self.ListOfAppointments
        if not pet_found:
            print("Pet not found.")

    # Option 6
    def checkPetVeterinaryLog(self):
        pet_name = input("Enter the pet's name to check its veterinary log: ").strip()
        pet_found = False
        for pet in self.listOfPets:
            if pet.name == pet_name:
                pet_found = True
                owner_name = input(f"Enter the owner's name for {pet.name}: ").strip()

                if owner_name.lower() != pet.owner.name.lower():
                    print(f"Error: {owner_name} is not the owner of {pet.name}. You cannot access the veterinary log.")
                    return  # Salir si el dueño no es correcto
                
                print(f"Veterinary log for {pet.name}:")
                if pet.veterinaryLog:
                    for log in pet.veterinaryLog:
                        print(log.displayAppointmentInfo())
                else:
                    print("No appointments found.")
                break
    
        if not pet_found:
            print("Pet not found.")
    
    #************************************+
    def __registerVet(self): # Admin Option 1

        if not self.listOfServices:
            print("\nNo type of service registered.")
            print("Please make sure the service exists before assigning it to a veterinarian.")
            input("Press Enter to return to the admin menu.\n")
            return

        input("\nPlease input the veterinarian data: (Enter to continue)")
        name = input("\nName: ").strip()
        contact = input("Phone contact: ").strip()
        
        # Create veterinarian
        registeredVet = VeterinaryMgmtSys.personGenerator.createPerson("Veterinarian",name=name,contact=contact)
        
        # The list of available services is displayed
        selectedServices = [] # The services that will be applied to the veterinarian
        servicesForVet = self.listOfServices[:]
        while servicesForVet:
            print("\nList of available services:")
            for indexService, availableServices in enumerate(servicesForVet):
                print(f"{indexService+1}. {availableServices}")
            
            serviceToBeAdded = int(input("\nSelect a service (enter the number): ").strip())-1
            selectedServices.append(servicesForVet[serviceToBeAdded])
            del servicesForVet[serviceToBeAdded]

            if servicesForVet:
                checkpoint = input("Keep adding services? (y/n): ").strip()
                if checkpoint == "n":
                    break

        #addService = Associate()
        #addService.serviceToVet(registeredVet,selectedServices)
        registeredVet.service_provided = selectedServices
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
        serviceType = input("\nType the name of the service: ").strip()
        self.listOfServices.append(serviceType)
        input("\nService successfully registered. (Enter to continue)")
    # Admin Option 5
    def __removeServiceType(self):
        print("Available services:")
        if not self.listOfServices:
            print("No services available to remove.")
            return
        
        for index, service in enumerate(self.listOfServices, start=1):
            print(f"{index}. {service}")

        try:
            service_index = int(input("Enter the number of the service to remove: ").strip()) - 1
            if 0 <= service_index < len(self.listOfServices):
                removed_service = self.listOfServices.pop(service_index)
                print(f"Service '{removed_service}' has been successfully removed.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Admin Option 6
    def __displayListOfServices(self):
        print("List of available services:")
        if not self.listOfServices:
            print("No services available.")
        else:
            for service in self.listOfServices:
                print(f"- {service}")

    @staticmethod
    def welcomeMessage():
        print("-------------------------------------------------")
        print("                    Welcome:                     ")
        print("                🐾 Happy Paw 🐾                 ")
        print("        Veterinary Management System App         \n")
        print("With this console application you'll be able to")
        print("manage your clients and their pets, schedule and")
        print("modify appointments, as well as to manage the")
        print("veterinarians and available services.")
        print("\n")
        print("Developed by: Santiago Torres and Lindsey Acourtt")
        print("-------------------------------------------------\n")

    def main_menu(self):
        while True:
            print("========= Main Menu =========")
            print("1. Register client") 
            print("2. Register pet") 
            print("3. Schedule appointment")
            print("4. Modify appointment")
            print("5. Cancel appointment")
            print("6. Check veterinary log for a pet")
            print("7. Admin access")
            print("8. Exit")
            print("9. Tests")
            opt = input("Choose an option: ").strip()
            if opt =="1":
                #1. Register client
                client = self.registerClient()
                print("\n---------------------------------------------")
                print("\nYou will now associate pets to this client: ")
                while True:
                    pet = self.registerPet() # Create pet
                    client.addPet(pet) # Associate pet to owner
                    pet.addOwner(client) # Associate owner to pet
                    self.listOfPets.append(pet)
                    
                    checkpoint = input("Add more pets? (y/n): ").strip()
                    if checkpoint == "n":
                        break
                
                self.listOfClients.append(client)
                    
            elif opt == "2":
                #2. Register pet
                pet = self.registerPet()
                
                print("\nYou will now associate an owner to this pet: \n")
                checkpoint = input("Select existing client? (y/n)").strip()
                if checkpoint == "y":
                    print("\nList of registered clients")
                    for client in self.listOfClients:
                        print(client)
                    
                    selectedClient = int(input("\nPlease select client ID: ").strip())
                    client = next((c for c in self.listOfClients if c.id == selectedClient),None)
                else:
                    input("\nPlease create a new client: (Enter to continue)")
                    client = self.registerClient()
                    self.listOfClients.append(client)
                
                pet.addOwner(client) # Associate Owner to Pet
                client.addPet(pet) # Associate Pet to Owner
                
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
                pw = getpass(prompt="\nEnter the password to continue: ")
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
                        admin_opt = input("Choose your admin option: ").strip()
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
                            input("\nInvalid option, hit Enter to continue.")
                else:
                    print("\nIncorrect password")
                    input("Press Enter to continue.")
                    continue
            elif opt == "8":
                #8. Exit
                saveToDB = input("\nDo you want to save to database? (y/n): ").strip()
                if saveToDB == 'y':
                    f=open("veterinary_database.txt","wb")
                    database = [self.listOfClients,self.listOfPets,self.listofVeterinarians,self.listOfAppointments,self.listOfServices]
                    pickle.dump(database,f)
                    f.close()
                print("\nThanks for using this service.")
                break    
            elif opt == "9":
                self.tests()
            else:
                print("\nOption is not valid, please try again.")
                input("Enter to continue.")
    
    
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
    filename = "veterinary_database.txt"
    if os.path.exists(filename):
        f = open(filename,"rb")
        database = pickle.load(f)
        print("Database imported")
        veterinaryManagementSys.createDatabase(database[0],database[1],database[2],database[3],database[4])
        f.close()
    else:
        veterinaryManagementSys.createDatabase([],[],[],[],[])
    
    veterinaryManagementSys.welcomeMessage()
    veterinaryManagementSys.main_menu()