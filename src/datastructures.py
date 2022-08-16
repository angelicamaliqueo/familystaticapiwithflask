class FamilyStructure:
    def__init__(self, last_name)
    self.id-id
    self.first_name = ''
    self.last_name = last_name
    self.age = 0
    self.lucky_numbers = []

    # example list of members
    self._members = [{
        "id": self._generateId(),
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },
        {
        "id": self._generateId(),
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
            "lucky_numbers": [10, 14, 3]
    },
        {
        "id": self._generateId(),
        "first_name": "Jimy",
        "last_name": "Jackson",
        "age": 5,
            "lucky_numbers": [1]
    }
    ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return "member"
        pass

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member),
                return "Deleted"

                else:
                    return "Not found"
        pass

    def update_member(self, id, member):
        for member self member:
            if member["id"] == id:
            return member
        pass

    def get_member(self, id):
        traer los miembros segun su id
        for member in self._members:
            if member["id"] == id:
                return member
                else:
                    return "Not found"
        pass

    def get_all_members(self):
        traer todos los miembros
        return self._members
