"""Unit tests for the task tracker."""
import tempfile
import unittest
from pathlib import Path

from app import add_task, complete_task, format_tasks, load_tasks


class TaskTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "tasks.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        self.assertEqual(add_task("Revise Python", self.data_file), 1)
        self.assertEqual(load_tasks(self.data_file)[0]["title"], "Revise Python")

    def test_ids_increase(self):
        add_task("First", self.data_file)
        self.assertEqual(add_task("Second", self.data_file), 2)

    def test_complete_task(self):
        add_task("Finish exercise", self.data_file)
        self.assertTrue(complete_task(1, self.data_file))
        self.assertTrue(load_tasks(self.data_file)[0]["done"])

    def test_missing_task(self):
        self.assertFalse(complete_task(99, self.data_file))

    def test_empty_list(self):
        self.assertEqual(format_tasks([]), "No tasks yet.")


if __name__ == "__main__":
    unittest.main()
