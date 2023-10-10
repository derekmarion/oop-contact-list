class ContactList:
    def __init__(self, name, contacts) -> None:
        self._name = name
        self._contacts = contacts

    @property
    def get_contacts(self):
        return self._contacts
    
    @get_contacts.setter
    def add_contact(self, contact):
        self._contacts.append(contact)
        self._contacts = sorted(self._contacts, key=lambda d: d['name'])

    @get_contacts.setter
    def remove_contact(self, name):
        for contact in self._contacts:
            if contact['name'] == name:
                self._contacts.remove(contact)

    def find_shared_contacts(self, contact_list):
        shared_contacts = []
        for contact_1,contact_2 in zip(self._contacts, contact_list._contacts):
            if contact_1['name'] == contact_2['name']:
                shared_contacts.append(contact_1)
        return shared_contacts
        

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)

