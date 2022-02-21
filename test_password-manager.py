import unittest
from user import User
from credentials import Credential

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        '''
        The setup method will run before each test case
        '''
        self.new_user = User('Lemmy','12345678')
        self.new_credential = Credential('Codewars', 'LemmyMwaura', '12345678')

    def tearDown(self):
        '''
        The teardown method does the cleanup after each test has run.
        '''
        for user in User.user_list:
            user.delete_user
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the objects are initialized properly.
        User('Lemmy','12345678')
        Credential('Codewars', 'LemmyMwaura', '12345678')
        '''
        self.assertEqual(self.new_user.user_name,"Lemmy")
        self.assertEqual(self.new_user.password,"12345678")
        self.assertEqual(self.new_credential.social_account_name,"Codewars")
        self.assertEqual(self.new_credential.social_username,"LemmyMwaura")
        self.assertEqual(self.new_credential.social_password,"12345678")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user objects
        to our user_list
        '''
        self.new_user.save_user()
        self.another_new_user = User('Cindy','87654321')
        self.another_new_user_again = User('Brandon','abcdefgh')
        self.another_new_user.save_user()
        self.another_new_user_again.save_user()
        self.assertEqual(len(User.user_list), 3)

    def test_delete_user(self):
        '''
        test_delete_user test case to test if the user object is removed from
        the user list.
        '''
        self.new_user.save_user()
        self.new_user.delete_user()

    def test_delete_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user objects
        to our user_list
        '''
        self.another_new_user = User('Cindy','87654321')
        self.another_new_user_again = User('Brandon','abcdefgh')
        self.new_user.save_user()
        self.another_new_user.save_user()
        self.another_new_user_again.save_user()

        self.new_user.delete_user()
        self.another_new_user.delete_user()
        self.another_new_user_again.delete_user()
        self.assertEqual(len(User.user_list), 0)

    def test_add_user(self):
        '''
        test_add_user checks the number of user objects that have been instantiated.
        '''
        self.another_new_user = User('Cindy','87654321')
        self.another_new_user_again = User('Brandon','abcdefgh')
        self.assertEqual(User.number_of_users, 3)

if __name__ == '__main__':
    unittest.main()