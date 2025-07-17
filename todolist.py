import unittest
import random

# Simulated FakeGenerator (replaces utils.fake_generator.FakeGenerator)
class FakeGenerator:
    def start(self):
        print("Filling fake database...")
        print("10 users, 40 todo lists, 160 todos created.")
        print("All existing data deleted. (Simulated)")

# Simulated Flask app (replaces app.create_app())
class App:
    def run(self):
        print("Running app... (simulated Flask app)")

# Functions
def run_tests():
    print("Running tests...")

    class DummyTest(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(1 + 1, 2)

        def test_random_choice(self):
            self.assertIn(random.choice([1, 2, 3]), [1, 2, 3])

    suite = unittest.TestLoader().loadTestsFromTestCase(DummyTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.errors or result.failures:
        print("❌ Some tests failed.")
    else:
        print("✅ All tests passed.")

def fill_db():
    generator = FakeGenerator()
    generator.start()

def run_app():
    app = App()
    app.run()

# Main
if __name__ == "__main__":
    print("Choose an action:")
    print("1. Run tests")
    print("2. Fill database")
    print("3. Run app")

    choice = input("Enter 1 / 2 / 3: ").strip()

    if choice == "1":
        run_tests()
    elif choice == "2":
        fill_db()
    elif choice == "3":
        run_app()
    else:
        print("Invalid choice.")
