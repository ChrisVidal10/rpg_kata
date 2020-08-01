from Models.character import Character

class TestCharacter:

    def setup_method(self):
        self.character = Character()

    def test_create_character(self):
        
        #Then
        assert 100 == self.character.health
        assert 1 == self.character.level
        assert True == self.character.alive 

    def test_take_damage(self):

        #When
        self.character.take_damage(60)

        #Then
        assert 40 == self.character.health

    def test_take_damage_exceeds_health(self):

        #When
        self.character.take_damage(10000)

        #Then
        assert 0 == self.character.health

    def test_dead_if_not_have_health(self):

        #When
        self.character.take_damage(10000)

        #Then
        assert False == self.character.alive


    def test_take_health(self):
        
        #Given
        self.character.take_damage(10)

        #When
        self.character.take_health(10)

        #Then
        assert 100 == self.character.health

    def test_take_health_only_if_alive(self):

        #Given
        self.character.take_damage(100)

        #When
        self.character.take_health(100)

        #Then
        assert 0 == self.character.health

    def test_take_health_cannot_raise_max_value(self):

        #When
        self.character.take_health(10000)

        #Then
        assert 1000 == self.character.health
