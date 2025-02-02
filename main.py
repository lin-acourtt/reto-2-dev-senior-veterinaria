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
        print(f"ID: {self.id}")
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
        return f"Name: {self.name} - Species: {self.species} - Breed: {self.breed} - Age: {self.age} - Owner: {self.owner.name}"

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

    def __str__(self): # Used to display the pet's information when calling "print()" on the object
        return f"Name: {self.name} - Species: {self.species} - Breed: {self.breed} - Age: {self.age} - Owner: {self.owner.name} \nVeterinary Log: {self.veterinaryLog}"

    def __repr__(self): # Used to display the pet's name in a list, when the list contains "Pet"s objects
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
        # Used to create the database the management system should consider to start the application with
        self.listOfClients = listOfClients # List of clients (objects) that have been registed
        self.listOfPets = listOfPets # List of pets (objects) that have been registered
        self.listofVeterinarians = listofVeterinarians # List of available veterinarians (object)
        self.listOfAppointments = listOfAppointments # List of appointments (objects) that have been scheduled for all pets
        self.listOfServices = listOfServices # List of services (string) available in the veterinary

    def registerClient(self): # Option 1 in the main menu
        print("\n---------------------------------------------------")
        input("Please input the pet owner data (Enter to continue)")
        
        # The user will be given 3 opportunities to enter valid data
        attempt = 1
        while attempt <= 3:
            name = input("\nClient's name: ").strip()
            name = name.capitalize()
            contact = input("Phone contact: ").strip()
            address = input("Address: ").strip()
            if (not name) or (not contact) or (not address):
                input("\nFields can't be empty. (Enter to continue)\n")
            else:
                break
            attempt += 1
        
        if attempt == 4:
            input("\nYou have entered invalid data 3 times. Returning to main menu.\n")
            return

        if self.listOfClients: 
            id = self.listOfClients[-1].id + 1 # If the database is not empty, the next ID should be incremented in 1
        else:
            id = 1 # If the database starts empty, the ID should be 1

        # Generate Client object (The list of pets will be updated once the pet is created)
        registeredClient = VeterinaryMgmtSys.personGenerator.createPerson("Client",name=name,contact=contact,address=address,id=id)
        input("\nClient successfully registered. (Enter to continue)")
        return registeredClient
    
    def registerPet(self): # Option 2 in the main menu
        input("\nPlease input the pet data (Enter to continue)")

        # The user will be given 3 opportunities to enter valid data
        attempt = 1
        while attempt <= 3:
            name = input("\nPet's name: ").strip()
            name = name.capitalize()
            species = input("Species: ").strip()
            species = species.capitalize()
            breed = input("Breed: ").strip()
            breed = breed.capitalize()
            if (not name) or (not species) or (not breed):
                input("\nFields can't be empty. (Enter to continue)\n")
            else:
                break
            attempt += 1
        
        if attempt == 4:
            input("\nYou have entered invalid data 3 times. Returning to main menu.\n")
            return
        
        # The user will be given 3 opportunities to enter valid data
        attempt = 1
        while attempt <= 3:
            try:
                age = int(input("Age: ").strip())
                if age < 0: # An error will be considered as well if the entered number is below 0
                    raise ValueError
            except:
                print("Invalid data, please try again.\n")
                attempt += 1
            else:
                break

        if attempt == 4:
            input("\nYou have entered an invalid age 3 times. Returning to main menu.\n")
            return      
        
        # Generate Pet object, the owner will be updated once it is generated
        registeredPet = Pet(name,species,breed,age)
        input("\nPet successfully registered. (Enter to continue)")
        return registeredPet

    def schedulePetAppmt(self): # Option 3 in the main menu
        
        if not self.listOfClients or not self.listOfPets:
            print("\n----------------------------------------")
            print("\nThere are not pets or clients registered")
            input("You will be returned to the main menu (Enter to continue)\n")
            return

        if not self.listOfServices:
            print("\n------------------------------------------------------------")
            print("\nThere are not available services to schedule an appointment.")
            input("You will be returned to the main menu (Enter to continue)\n")
            return
        
        if not self.listofVeterinarians:
            print("\n-----------------------------------------------------------------")
            print("\nThere are not available veterinarians to schedule an appointment.")
            input("You will be returned to the main menu (Enter to continue)\n")
            return

        print("\n-----------------------------------------------")
        input("Specify appointment details (Enter to continue)")
        pet = input("\nType the pet's name: ").strip()
        petFound = next((p for p in self.listOfPets if p.name == pet.capitalize()),None)

        if not petFound:
            input(f"\nPet: {pet.capitalize()} not found. Returning to main menu. (Enter)\n")
            return
        pet = pet.capitalize()

        owner = input("Owner: ").strip()
        ownerFound = next((c for c in self.listOfClients if c.name == owner.capitalize()),None)

        if not ownerFound:
            input(f"\nClient: {owner.capitalize()} not found. Returning to main menu. (Enter)\n")
            return
        owner = owner.capitalize()

        #Generate a list of pets and their owners
        petsAndOwnerRelation = False
        
        for indexPet, memberpet in enumerate(self.listOfPets):
            if (pet.lower() == memberpet.name.lower()) and (owner.lower() == memberpet.owner.name.lower()):
                petsAndOwnerRelation = True
                break        
        
        if petsAndOwnerRelation == False:
            print(f"\nThe pet {pet.capitalize()} and owner {owner.capitalize()} are not related.")
            input("You will be returned to the main menu (Enter to continue)")
            return

        # The list of available services is displayed
        print("\nList of available services:")
        for indexService, availableServices in enumerate(self.listOfServices):
            print(f"{indexService+1}. {availableServices}")
        
        while True:
            try:
                selectedService = int(input("\nSelect a service, 0 to cancel (enter the number): ").strip()) - 1
                if (selectedService <-1) or (selectedService >= len(self.listOfServices)):
                    raise ValueError # If the selected service index is a number lower than -1 or greater that the amount of services, an exception should be considered
            except:
                input("\nInvalid input, try again. (Enter to continue)\n")
            else:
                if selectedService == -1: # Cancel operation
                    input("\nAppointment not scheduled. (Enter to continue)\n")
                    return
                else:
                    service = self.listOfServices[selectedService]
                    break
        
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
        
        while True:
            try:
                indexVetInput = int(input("\nSelect a veterinarian, 0 to cancel (enter the number): ").strip())-1
                if (indexVetInput <-1) or (indexVetInput >= len(availableVets)):
                    raise ValueError # If the selected veterinarian is not an idex in the list of available services
            except:
                input("\nInvalid input, try again. (Enter to continue)\n")
            else:
                if indexVetInput == -1: # Cancel operation
                    input("\nAppointment not scheduled. (Enter to continue)\n")
                    return
                else:
                    veterinarian = availableVets[indexVetInput][1] ## Why?
                    break

        # Continue taking the information for the appointment
        while True:
            try:
                date = input("Date (AAAA-MM-DD): ").strip()
                time = input("Time (HH:MM): ").strip()
                
                # The datetime library is used to generate a datetime object for the date
                date = datetime.strptime(date, "%Y-%m-%d")
                # The datetime library is used to generate a datetime object for the time
                time = datetime.strptime(time, "%H:%M")
                
            except:
                cancel = input("\nIncorrect formats, please try again (Any key to continue, 0 to cancel)\n")
                if cancel == '0':
                    input("\nAppointment not scheduled. (Enter to continue)\n")
                    return
            else:
                # This line will convert the datetime object to a date-only object
                date = datetime.date(date)
                # This line will convert the datetime object to a time-only object
                time = datetime.time(time)
                break

        appointment = Appointment(date, time, self.listOfPets[indexPet], service, veterinarian)
        self.listOfPets[indexPet].veterinaryLog.append(appointment) # Veterinary log is updated for the pet
        self.listOfAppointments.append(appointment) # General list of appointments in updated
        input(f"\nAppointment successfully registered for pet {pet}. (Enter to continue)")
        return appointment
        
    def modifyPetAppmt(self): # Option 4 in main menu

        if not self.listOfAppointments:
            print("\n----------------------------------------")
            print("\nThere are not appointments scheduled.")
            input("You will be returned to the main menu (Enter to continue)\n")
            return
        
        pet_name = input("\nEnter the pet's name to modify its appointment: ").strip()

        # Look for pets with the same name
        pets_with_same_name = [pet for pet in self.listOfPets if pet.name.lower() == pet_name.lower()]

        if not pets_with_same_name:
            print("\nNo pets found with that name.\n")
            input("Returning to main menu. (Enter to continue)\n")
            return

        # If there is more that one pet with the same name, we ask for the owner name
        if len(pets_with_same_name) > 1:
            owner_name = input("Multiple pets with the same name found. Please enter the owner's name: ").strip()

            # Get the pets that match with the owner name typed by user
            pets_with_owner = [pet for pet in pets_with_same_name if pet.owner.name.lower() == owner_name.lower()]

            if not pets_with_owner:
                print(f"\nPet {pet_name.capitalize()} not found for owner {owner_name.capitalize()}.\n")
                input("Returning to main menu. (Enter to continue)\n")
                return
        else:
            # If there is only one pet with the selected name, that one will be used without asking for owner name.
            pets_with_owner = pets_with_same_name

        # We extract the pet infomration from the list
        pet = pets_with_owner[0]
        print("----------------------------------------------------")
        print(f"\nSelected pet: {pet.name} (Owner: {pet.owner.name})")

        if not pet.veterinaryLog:
            input("\nNo appointments found for this pet. (Enter to continue)\n")
            return

        print(f"\nAppointments for {pet.name}:")
        print("------------------")
        for i, appointment in enumerate(pet.veterinaryLog):
            print(f"{i + 1}. {appointment.displayAppointmentInfo()}")
            print("------------------")

        try:
            appointment_index = int(input("\nSelect the appointment to modify (enter the number): ").strip()) - 1
            appointment_to_modify = pet.veterinaryLog[appointment_index]

            # Modify the appointment
            print("Modify appointment details:")

            # Modify date
            new_date = input(f"Current Date: {appointment_to_modify.date}. Enter new date (YYYY-MM-DD) or press Enter to Keep: ").strip()
            if new_date == "":
                new_date = appointment_to_modify.date 
            else:
                new_date = datetime.strptime(new_date, "%Y-%m-%d").date()

            # Modify time
            new_time = input(f"Current Time: {appointment_to_modify.time}. Enter new time (HH:MM) or press Enter to keep: ").strip()
            if new_time == "":  # No input, keep the same
                new_time = appointment_to_modify.time
            else:
                new_time = datetime.strptime(new_time, "%H:%M").time()

            # Modify service

            # The list of available services is displayed
            print("\nList of available services:")
            for indexService, availableServices in enumerate(self.listOfServices):
                print(f"{indexService+1}. {availableServices}")

            selectedService = input(f"\nSelect a service, current service: {appointment_to_modify.service}. Type the number or press Enter to keep: ").strip()
            
            if selectedService == "":
                new_service = appointment_to_modify.service
            else:
                new_service = self.listOfServices[int(selectedService)-1]

            # Modify veterinarian

            # Find veterinaries that match this service
            availableVets = []
            for indexVet, vet in enumerate(self.listofVeterinarians):
                if new_service in vet.service_provided:
                    availableVets.append([indexVet,vet])

            if not availableVets:
                print(f"\nThere are not veterinarians for the service: {new_service}.")
                input("You will be returned to the main menu (Enter to continue)")
                return

            print(f"\nList of available veterinarians for serivice '{new_service}':")
            for indexAvaVet, vet in enumerate(availableVets):
                print(f"{indexAvaVet+1}. {vet[1].name}")
            
            selectedVet = input(f"\nSelect a veterinarian, current vet: {appointment_to_modify.veterinarian.name}, type the number or press Enter to keep:  ").strip()

            if selectedVet == "":
                new_veterinarian = appointment_to_modify.veterinarian
            else:
                new_veterinarian = availableVets[int(selectedVet)-1][1]
            
            # So far we have the information of the appointment in the pets veterinary log's index: appointment_to_modify = pet.veterinaryLog[appointment_index]
            # We also need the index of the same appoint but in the registry of all appointments: self.listOfAppointments

            for idxTotalRegistry,objTotalRegistry in enumerate(self.listOfAppointments):
                if id(objTotalRegistry) == id(appointment_to_modify):
                    indexToModify = idxTotalRegistry

            # Update the appointment in the total registry
            self.listOfAppointments[indexToModify].modifyAppointment(date=new_date, time=new_time, service=new_service, veterinarian=new_veterinarian)

            # Update the appointment in the pet's veterinary log
            appointment_to_modify.modifyAppointment(date=new_date, time=new_time, service=new_service, veterinarian=new_veterinarian)
            input("\nAppointment modified successfully! (Enter to return to menu)\n")
        except: # (ValueError, IndexError):
            input("\nSomething failed. Cancelling operation. (Enter to continue)\n")    
    
    # Option 5
    def cancelPetAppmt(self):
        
        if not self.listOfAppointments:
            print("\n----------------------------------------")
            print("\nThere are not appointments scheduled.")
            input("You will be returned to the main menu (Enter to continue)\n")
            return
        
        pet_name = input("\nEnter the pet's name to cancel an appointment: ").strip()
        
        list_of_pet_names = [p.name.lower() for p in self.listOfPets]

        if pet_name.lower() in list_of_pet_names:
            # Generate list of clients
            list_of_pet_owner_names = [c.name.lower() for c in self.listOfClients if (pet_name.lower() in [p.name.lower() for p in c.list_of_pets])]
            
            owner_name = input("Enter the owner's name: ").strip()
            
            if owner_name.lower() in list_of_pet_owner_names:
                
                pet_obj_list = [p for p in self.listOfPets if (p.name.lower() == pet_name.lower() and p.owner.name.lower() == owner_name.lower())]
                pet_obj = pet_obj_list[0]

                if pet_obj.veterinaryLog:
                    print(f"\nAppointments for {pet_obj.name}:")
                    print("------------------")
                    for i, appointment in enumerate(pet_obj.veterinaryLog):
                        print(f"{i + 1}. {appointment.displayAppointmentInfo()}")
                        print("------------------")
                    
                    try:
                        appointment_index = int(input("\nSelect the appointment to cancel (enter the number): ").strip()) 
                        if 0 < appointment_index <= len(pet_obj.veterinaryLog):
                            # Before cancelling the appointment, we need to find it in the total registry
                            for idxTotalRegistry,objTotalRegistry in enumerate(self.listOfAppointments):
                                if id(objTotalRegistry) == id(pet_obj.veterinaryLog[appointment_index-1]):
                                    indexToRemove = idxTotalRegistry
                            
                            # Remove the appointment from the total registry
                            del self.listOfAppointments[indexToRemove]
                            # Remove the appointment from the pets veterinary log
                            pet_obj.cancelAppointment(appointment_index)
                            input("\nAppointment cancelled successfully! Press enter to return to the main menu.\n")
                        else:
                            raise ValueError
                    except (ValueError, IndexError):
                        input("\nInvalid input. Aborting operation. Enter to return to main menu.\n")
                        return 
                else:
                    input(f"\nVeterinary log not found for pet: '{pet_obj.name}'. Press enter to return.")
                    return
            else:
                input(f"\nOwner: {owner_name.capitalize()} not found for pet: {pet_name.capitalize()}. Returning to main menu. Enter to continue.\n")
                return
        else:
            input(f"\nPet '{pet_name.capitalize()}' not found. (Enter to return)")
            return

    # Option 6
    def checkPetVeterinaryLog(self):
        if not self.listOfAppointments:
            print("\n----------------------------------------")
            print("\nThere are not appointments scheduled.")
            input("You will be returned to the main menu (Enter to continue)\n")
            return
        
        pet_name = input("\nEnter the pet's name to check their appointments: ").strip()
        
        list_of_pet_names = [p.name.lower() for p in self.listOfPets]

        if pet_name.lower() in list_of_pet_names:
            # Generate list of clients
            list_of_pet_owner_names = [c.name.lower() for c in self.listOfClients if (pet_name.lower() in [p.name.lower() for p in c.list_of_pets])]
            
            owner_name = input("Enter the owner's name: ").strip()
            
            if owner_name.lower() in list_of_pet_owner_names:
                
                pet_obj_list = [p for p in self.listOfPets if (p.name.lower() == pet_name.lower() and p.owner.name.lower() == owner_name.lower())]
                pet_obj = pet_obj_list[0]

                if pet_obj.veterinaryLog:
                    print(f"\nAppointments for {pet_obj.name}:")
                    print("------------------")
                    for i, appointment in enumerate(pet_obj.veterinaryLog):
                        print(f"{i + 1}. {appointment.displayAppointmentInfo()}")
                        print("------------------")
                    
                    input("\nPress enter to continue.")
                else:
                    input(f"\nVeterinary log not found for pet: '{pet_obj.name}'. Press enter to return.")
                    return
            else:
                input(f"\nOwner: {owner_name.capitalize()} not found for pet: {pet_name.capitalize()}. Returning to main menu. Enter to continue.\n")
                return
        else:
            input(f"\nPet '{pet_name.capitalize()}' not found. (Enter to return)")
            return
    
    #************************************+
    def __registerVet(self): # Admin Option 1

        if not self.listOfServices:
            print("\nNo type of service registered.")
            print("Please make sure the service exists before assigning it to a veterinarian.")
            input("Press Enter to return to the admin menu.\n")
            return

        input("\nPlease input the veterinarian data: (Enter to continue)")
        # The user will be given 3 opportunities to enter valid data
        attempt = 1
        while attempt <= 3:
            name = input("\nName: ").strip()
            name = name.capitalize()
            contact = input("Phone contact: ").strip()
            if (not name) or (not contact):
                input("\nFields can't be empty. (Enter to continue)\n")
            else:
                break
            attempt += 1
        
        if attempt == 4:
            input("\nYou have entered invalid data 3 times. Returning to main admin menu.\n")
            return
        
        # Create veterinarian
        registeredVet = VeterinaryMgmtSys.personGenerator.createPerson("Veterinarian",name=name,contact=contact)
        
        # The list of available services is displayed
        selectedServices = [] # The services that will be applied to the veterinarian
        servicesForVet = self.listOfServices[:]
        while servicesForVet:
            print("\nList of available services:")
            for indexService, availableServices in enumerate(servicesForVet):
                print(f"{indexService+1}. {availableServices}")
            
            try:
                serviceToBeAdded = int(input("\nSelect a service, or 0 to cancel the registration of this veterinarian (enter the number): ").strip())-1
                if (serviceToBeAdded <-1) or (serviceToBeAdded>=len(servicesForVet)):
                    raise ValueError # Typing a not valid int should be handled as an exception
            except:
                input("\nInvalid input, try again. (Enter to continue)\n")
            else:
                if serviceToBeAdded == -1: # Cancel operation
                    print(f"\nThe veterinarian {registeredVet.name} was not registered. (Enter to continue)\n")
                    return
                else:
                    selectedServices.append(servicesForVet[serviceToBeAdded])
                    del servicesForVet[serviceToBeAdded]

                    if servicesForVet:
                        checkpoint = input("\nKeep adding services? (y/n): ").strip()
                        if checkpoint == "n":
                            break
                    else:
                        input("\nNo more available services. (Enter to continue)\n")
                        break

        registeredVet.service_provided = selectedServices
        self.listofVeterinarians.append(registeredVet)
        print("\nVeterinarian successfully registered.")
        print(f"Veterinarian: {registeredVet.name}, services: {registeredVet.service_provided}")
        input("Enter to continue.\n")
        return registeredVet
    # Admin Option 2
    def __removeVet(self):
        
        if not self.listofVeterinarians:
            input("\nNo veterinarians to remove. Enter to return.")
            return

        print("\n**********************")
        print("\nList of Veterinarians:\n")
        for i, vet in enumerate(self.listofVeterinarians, start=1):
            print(f"{i}. {vet.name} - {vet.contact}")

        try:
            vet_index = int(input("\nSelect the veterinarian to remove (enter the number): ")) - 1
            if 0 <= vet_index < len(self.listofVeterinarians):
                removed_vet = self.listofVeterinarians.pop(vet_index)
                input(f"\nVeterinarian '{removed_vet.name}' has been successfully removed. Enter to return.")
            else:
                raise ValueError
        except (ValueError, IndexError):
            input("\nInvalid input. You will be returned to the admin menu.")  
            return  

    # Admin Option 3
    def __displayListOfVets(self):
        
        if not self.listofVeterinarians:
            input("\nNo veterinarians to remove. Enter to return.")
            return

        print("\n**********************")
        print("\nList of Veterinarians:\n")
        for i, vet in enumerate(self.listofVeterinarians, start=1):
            print(f"{i}. {vet}")
        
        input("\nPress enter to continue.")
        return
    
    # Admin Option 4
    def __registerServiceType(self):
        # The user will be given 3 opportunities to enter valid data
        attempt = 1
        while attempt <= 3:
            serviceType = input("\nType the name of the service: ").strip()
            serviceType = serviceType.capitalize()
            if (not serviceType):
                input("\nField can't be empty. (Enter to continue)\n")
            else:
                break
            attempt += 1

        if attempt == 4:
            input("\nYou have entered invalid data 3 times. Returning to main admin menu.\n")
            return
        
        self.listOfServices.append(serviceType)
        input("\nService successfully registered. (Enter to continue)")

    # Admin Option 5
    def __removeServiceType(self):
        
        if not self.listOfServices:
            input("\nNo services available to remove. Press enter to return.")
            return
        
        print("\n*******************")
        print("\nAvailable services:")
        for index, service in enumerate(self.listOfServices, start=1):
            print(f"{index}. {service}")

        try:
            service_index = int(input("\nEnter the number of the service to remove: ").strip()) - 1
            if 0 <= service_index < len(self.listOfServices):
                removed_service = self.listOfServices.pop(service_index)
                
                # Besides removing the service from the list of services, it is also necessary to remove 
                # the service from the veterinarians that have it assigned.

                for vet in self.listofVeterinarians:
                    if removed_service in vet.service_provided:
                        vet.service_provided.remove(removed_service)

                input(f"\nService '{removed_service}' has been successfully removed. Press enter to continue.")
            else:
                raise ValueError
        except ValueError:
            input("\nInvalid input. You will be returned to the admin menu.")
            return

    # Admin Option 6
    def __displayListOfServices(self):
        
        if not self.listOfServices:
            input("\nNo services available. You will be returned to the main menu.")
            return
        else:
            print("\n***************************")
            print("\nList of available services:\n")
            for service in self.listOfServices:
                print(f"- {service}")
            
            input("\nPress enter to continue.")
            return
        
    def __displayPrivateData(self):
        print("\n*********************************************************")
        print("\nRegistered data")
        print("\n----------")
        
        print("Clients")
        print("----------")
        for client in self.listOfClients:
            print(client)
        
        print("\n----------")
        print("Pets")
        print("----------")
        for pet in self.listOfPets:
            print(f"\n{pet}")
        
        print("\n----------")
        print("Appointments")
        print("----------")
        for appointment in self.listOfAppointments:
            print(appointment) 
        
        print("\n----------")
        print("Veterinarians")
        print("----------")
        for vet in self.listofVeterinarians:
            print(vet)
        
        print("\n----------")
        print("Services")
        print("----------")
        for service in self.listOfServices:
            print(service)
        
        print("\n*********************************************************")
        input("\nPress enter to continue.")

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
            print("\n========= Main Menu =========")
            print("1. Register client") 
            print("2. Register pet") 
            print("3. Schedule appointment")
            print("4. Modify appointment")
            print("5. Cancel appointment")
            print("6. Check veterinary log for a pet")
            print("7. Display clients and pet information")
            print("8. Admin access")
            print("9. Exit")
            opt = input("\nChoose an option: ").strip()
            if opt =="1":
                #1. Register client
                client = self.registerClient()

                if not client: # Client not genereated due to invalid input
                    continue

                print("\n---------------------------------------------")
                print("\nYou will now associate pets to this client: ")
                while True:
                    pet = self.registerPet() # Create pet
                    
                    if not pet: # Pet not genereated due to invalid input
                        self.listOfClients.append(client)
                        print("----- Pet not registered -----")
                        print(f"The client registration for {client.name} will end here.")
                        print("If you wish to add pets for this client, please use option '2. Register pet'")
                        input("on the main menu. (Enter to continue)\n")
                        break

                    client.addPet(pet) # Associate pet to owner
                    pet.addOwner(client) # Associate owner to pet
                    self.listOfPets.append(pet)
                    
                    checkpoint = input("\nAdd more pets? (y/n): ").strip()
                    if (checkpoint != "y"):
                        invalid = ""
                        if checkpoint != "n":
                            invalid = "Invalid input. "
                        print(f"\n{invalid}The client registration for {client.name} will end here.")
                        print("If you wish to add more pets, please use option '2. Register pet'")
                        input("on the main menu. (Enter to continue)\n")
                        self.listOfClients.append(client)
                        break
                    
            elif opt == "2":
                #2. Register pet
                pet = self.registerPet()

                if not pet: # Pet not genereated due to invalid input
                    continue
                
                print("\nYou will now associate an owner to this pet: \n")
                
                if self.listOfClients: # If the list of client is already populated, ask the user to select one of them
                    checkpoint = input("Select existing client? (y/n)").strip()
                    if checkpoint == "y":
                        print("\nList of registered clients")
                        for client in self.listOfClients:
                            print(client)

                        while True:
                            try:
                                selectedClient = int(input("\nPlease select client ID or 0 to create a new client anyway: ").strip())
                                if (selectedClient < 0) or (selectedClient > len(self.listOfClients)):
                                    raise ValueError
                            except:
                                input("\nInvalid input. (Enter to continue)\n")
                            else:
                                break
                        
                        if selectedClient > 0:
                            client = next((c for c in self.listOfClients if c.id == selectedClient),None)
                        elif selectedClient == 0: # Client will be generated if the selected ID is 0
                            client = self.registerClient()

                            if not client: # Client not genereated due to invalid input
                                input(f"\nRemoving information for pet {pet.name} (Enter to continue)\n")
                                continue # The warning is already inside the registerClient() method
                    
                            self.listOfClients.append(client)

                    else: # Client will be generated if different than "y"
                        print("\nResponse was different from 'yes', generating new client.")
                        client = self.registerClient()

                        if not client: # Client not genereated due to invalid input
                            input(f"\nRemoving information for pet {pet.name} (Enter to continue)\n")
                            continue

                        self.listOfClients.append(client)
                else: # Client will be generated if self.listOfClients is empty
                    client = self.registerClient()

                    if not client: # Client not genereated due to invalid input
                        input(f"\nRemoving information for pet {pet.name} (Enter to continue)\n")
                        continue

                    self.listOfClients.append(client)
                
                pet.addOwner(client) # Associate Owner to Pet
                client.addPet(pet) # Associate Pet to Owner

                print(f"\nClient: '{client.name}' and Pet: '{pet.name}' successfully associated.")
                input("(Enter to continue)")
                
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
            elif opt == '7':
                #7. Display clients and pet information
                print("\n****************** LIST OF CLIENTS ******************")
                print("-----------------------------")
                for client in self.listOfClients:
                    client.displayContactInfo()
                    print("-----------------------------")
                print("\n****************** LIST OF PETS ******************")
                for petCounter, pet in enumerate(self.listOfPets,start=1):
                    print(f"{petCounter}. {pet.displayPetInfo()}")
                input("\nEnter to return to main menu.")
            elif opt == "8":
                #8. Admin access

                # Request for password
                pw = getpass(prompt="\nEnter the password to continue: ")
                if pw == "dev-senior":
                    while True:
                        print("\n*** Admin menu ***")
                        print("1. Register veterinarian")
                        print("2. Remove veterinarian")
                        print("3. Display list of veterinarians")
                        print("4. Register type of service")
                        print("5. Remove type of service")
                        print("6. Display list of services")
                        print("7. Display the whole registry")
                        print("8. Return")
                        admin_opt = input("\nChoose your admin option: ").strip()
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
                        elif admin_opt == '7':
                            #7. Display the whole registry
                            self.__displayPrivateData()
                        elif admin_opt == "8":
                            #8. Return
                            break
                        else:
                            input("\nInvalid option, hit Enter to continue.")
                else:
                    print("\nIncorrect password")
                    input("Press Enter to continue.")
                    continue
            elif opt == "9":
                #8. Exit
                saveToDB = input("\nDo you want to save to databas NOOOOOOO (y/n): ").strip()
                if saveToDB == 'y':
                    f=open("veterinary_database.txt","wb")
                    database = [self.listOfClients,self.listOfPets,self.listofVeterinarians,self.listOfAppointments,self.listOfServices]
                    pickle.dump(database,f)
                    f.close()
                print("\nThanks for using this service.\n")
                break    
            else:
                print("\nOption is not valid, please try again.")
                input("Enter to continue.")
    

if __name__ == "__main__":

    # Create the object for the management system
    veterinaryManagementSys = VeterinaryMgmtSys()

    # Create database for the management system (empty for now)
    useDB = input("Use DB?: ")
    filename = "veterinary_database.txt"
    if os.path.exists(filename) and useDB == "y":
        f = open(filename,"rb")
        database = pickle.load(f)
        print("Database imported")
        veterinaryManagementSys.createDatabase(database[0],database[1],database[2],database[3],database[4])
        f.close()
    else:
        veterinaryManagementSys.createDatabase([],[],[],[],[])
    
    veterinaryManagementSys.welcomeMessage()
    veterinaryManagementSys.main_menu()