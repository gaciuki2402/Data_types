import json
class Library_Details():
    def libraryDataCollection(self):
        self.Details=[]
        self.registration_number=input("Enter the registration number:").upper() #tu01
        print(self.registration_number)

        library_assigned_books={
            "TU01":{
                "Name":"Grace",
                "course":"MCS",
                "books":{
                    "Kidagaa":{
                        "ISBN":"2123",
                        "date of Assignment":"23/4/2020",
                        "author":"Ken Walibora",
                        "pages":350
                    },

                    "Across the Brigde": {
                        "ISBN": "2163",
                        "date of Assignment": "21/4/2020",
                        "author": "John Kiriamiti",
                        "pages": 1087
                    },
                }
            },
            "TU02": {
                "Name": "Irene",
                "course": "MCS",
                "books": {
                    "Son of Fate": {
                        "ISBN": "2121",
                        "date of Assignment": "03/4/2020",
                        "author": "Ken Walibora",
                        "pages": 1200
                    },

                    "The river and the source": {
                        "ISBN": "2143",
                        "date of Assignment": "11/4/2020",
                        "author": "Akoko",
                        "pages": 1500
                    },
                }
            }
        }
        lib=json.dumps(library_assigned_books[self.registration_number],indent=4)
        print(lib)

g1=Library_Details()
g1.libraryDataCollection()


