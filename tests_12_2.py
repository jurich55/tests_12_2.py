import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}  # Словарь финишеров
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Итерируемся по копии списка
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant  # Добавляем место и участника в словарь
                    place += 1
                    self.participants.remove(participant)
        return finishers  # Финишеры

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Иван', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 5)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in enumerate(cls.all_results, start=1):
            print(f'{test_value}')

    def test_turn1(self):
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')  # Проверка, что Ник последний
        self.all_results.append(result)

    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')  # Проверка, что Ник последний
        self.all_results.append(result)

    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')  # Проверка, что Ник последний
        self.all_results.append(result)

if __name__ == '__main__':
    unittest.main()