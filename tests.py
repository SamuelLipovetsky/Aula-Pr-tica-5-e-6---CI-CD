import unittest
from main import TodoList, handle_command


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_item(self):
        self.assertEqual(
            self.todo_list.add_item("Test Item 1"), "Test Item 1 added to list"
        )
        self.assertEqual(
            self.todo_list.add_item("Test Item 1"), "Test Item 1 already in list"
        )

    def test_remove_item(self):
        self.todo_list.add_item("Test Item 2")
        self.assertEqual(
            self.todo_list.remove_item("Test Item 2"), "Test Item 2 removed from list"
        )
        self.assertEqual(
            self.todo_list.remove_item("Test Item 2"), "Test Item 2 not in list"
        )

    def test_mark_item_as_completed(self):
        self.todo_list.add_item("Test Item 3")
        self.assertEqual(
            self.todo_list.mark_item_as_completed("Test Item 3"), "Test Item 3 done"
        )
        self.assertEqual(
            self.todo_list.mark_item_as_completed("Test Item 4"),
            "Test Item 4 not in list",
        )

    def test_mark_item_as_uncompleted(self):
        self.todo_list.add_item("Test Item 4")
        self.todo_list.mark_item_as_completed("Test Item 4")
        self.assertEqual(
            self.todo_list.mark_item_as_uncompleted("Test Item 4"), "Test Item 4 undone"
        )
        self.assertEqual(
            self.todo_list.mark_item_as_uncompleted("Test Item 5"),
            "Test Item 5 not in list",
        )

    def test_show_completed_items(self):
        self.todo_list.add_item("Test Item 5")
        self.todo_list.add_item("Test Item 6")
        self.todo_list.mark_item_as_completed("Test Item 5")
        self.assertEqual(self.todo_list.show_completed_items(), ["Test Item 5"])

    def test_show_uncompleted_items(self):
        self.todo_list.add_item("Test Item 7")
        self.todo_list.add_item("Test Item 8")
        self.todo_list.mark_item_as_completed("Test Item 7")
        self.assertEqual(self.todo_list.show_uncompleted_items(), ["Test Item 8"])

    def test_show_all_items(self):
        self.todo_list.add_item("Test Item 9")
        self.todo_list.add_item("Test Item 10")
        self.todo_list.mark_item_as_completed("Test Item 9")
        all_items = self.todo_list.show_all_items()
        expected = {"Test Item 9": "completed", "Test Item 10": "uncompleted"}
        self.assertEqual(all_items, expected)


class TestCommandParsing(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_command(self):
        result = handle_command(self.todo_list, "add Test Item 1")
        self.assertEqual(result, "Test Item 1 added to list")

    def test_remove_command(self):
        self.todo_list.add_item("Test Item 2")
        result = handle_command(self.todo_list, "remove Test Item 2")
        self.assertEqual(result, "Test Item 2 removed from list")

    def test_complete_command(self):
        self.todo_list.add_item("Test Item 3")
        result = handle_command(self.todo_list, "complete Test Item 3")
        self.assertEqual(result, "Test Item 3 done")

    def test_uncomplete_command(self):
        self.todo_list.add_item("Test Item 4")
        self.todo_list.mark_item_as_completed("Test Item 4")
        result = handle_command(self.todo_list, "uncomplete Test Item 4")
        self.assertEqual(result, "Test Item 4 undone")

    def test_show_completed_command(self):
        self.todo_list.add_item("Test Item 5")
        self.todo_list.mark_item_as_completed("Test Item 5")
        result = handle_command(self.todo_list, "show completed")
        self.assertEqual(result, "Completed items: ['Test Item 5']")

    def test_show_uncompleted_command(self):
        self.todo_list.add_item("Test Item 6")
        self.todo_list.add_item("Test Item 7")
        self.todo_list.mark_item_as_completed("Test Item 6")
        result = handle_command(self.todo_list, "show uncompleted")
        self.assertEqual(result, "Uncompleted items: ['Test Item 7']")

    def test_show_all_command(self):
        self.todo_list.add_item("Test Item 8")
        self.todo_list.add_item("Test Item 9")
        self.todo_list.mark_item_as_completed("Test Item 8")
        result = handle_command(self.todo_list, "show all")
        expected = "All items:\nTest Item 8: completed\nTest Item 9: uncompleted"
        self.assertEqual(result, expected)

    def test_unknown_command(self):
        result = handle_command(self.todo_list, "unknown")
        self.assertEqual(
            result,
            "Unknown command. Available commands: add, remove, complete, uncomplete, show, exit.",
        )

    def test_exit_command(self):
        result = handle_command(self.todo_list, "exit")
        self.assertEqual(result, "exit")


if __name__ == "__main__":
    unittest.main()
