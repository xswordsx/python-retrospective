class Person:
    _object_set = set()

    @property
    def object_set():
        return _object_set[:]

    @property
    def name(self):
            return self._name

    @name.setter
    def name(self, value):
            if isinstance(value, str):
                    self._name = value

    @property
    def birth_year(self):
            return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
            if isinstance(value, int):
                    self._birth_year = value
            else:
                    self._birth_year = 2013

    @property
    def gender(self):
            return self._gender

    @gender.setter
    def gender(self, value):
            if value == "M" or value == "F":
                    self._gender = value

    @property
    def mother(self):
            return self._mother

    @staticmethod
    def parentChecker(self, value):
            return self is not value and type(value) == type(self)

    def is_direct_successor(self, other):
        if(other is not None
           and other is self.mother
           or other is self.father
           or self is other.mother
           or self is other.father):
            return True
        return False

    @mother.setter
    def mother(self, value):
            if parentChecker(self, value) and value.gender == "F":
                    self._mother = value

    @property
    def father(self):
            return self._father

    @father.setter
    def father(self, value):
            if parentChecker(self, value) and value.gender == "M":
                    self._father = value

    def __init__(self, name="Unknown", gender="M", birth_year=2013,
                 father=None, mother=None):
            self.name = name
            self.birth_year = birth_year
            self.gender = gender
            self._mother = mother
            self._father = father
            self._brothers = list()
            self._sisters = list()
            Person._object_set.add(self)

    def get_lil_guys(self, gender):
        storageList = set()
        for person in Person._object_set:
            if(person.mother == self.mother or
               person.father == self.father):
                if person.gender == gender:
                    storageList.add(person)
        if(self in storageList):
            storageList.remove(self)
        return list(storageList)

    def get_sisters(self):
        sisterList = Person.get_lil_guys(self, "F")
        return sisterList

    def get_brothers(self):
        brotherList = Person.get_lil_guys(self, "M")
        return brotherList

    def children(self, gender=None):
            returningSet = set()
            for person in Person._object_set:
                if person.mother == self or person.father == self:
                    if gender is not None:
                        if person.gender == gender:
                            returningSet.add(person)
                    else:
                        returningSet.add(person)
            return list(returningSet)

    def add_child(self, child):
        if self is not child:
            if self.birth_year - child.birth_year >= 18:
                if self.gender == "M":
                    child.father = self
                else:
                    child.mother = self

    def add_parent(self, parent):
        if self is not parent:
            if parent.birth_year - self.birth_year >= 18:
                if parent.gender == "M":
                    self.father = parent
                else:
                    self.mother = parent
