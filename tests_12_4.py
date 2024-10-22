import unittest
import logging
from testt import Runner, Tournament


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    encoding='utf-8', format='%(levelname)s: %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Run Boy Run", -5)  # Передаем отрицательное значение скорости for _ in range(10):
            runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(12345)  # Передаем что-то кроме строки в name
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        runner1 = Runner("Le Monde")
        runner2 = Runner("Skyfall")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()

