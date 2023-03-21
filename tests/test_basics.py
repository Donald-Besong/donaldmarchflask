import unittest
import sys

sys.path.insert(1, '.')
from app import create_app, db
from flask import current_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()
        #print("*** setting up **")

    def tearDown(self):
         db.session.remove()
         #db.drop_all()
         #self.app_context.pop()
         print(" tear down")

    # def test_app_exists(self):
        # self.assertFalse(current_app is None)

    # def test_app_is_testing(self):
        # self.assertTrue(current_app.config['TESTING'])
    def test(self):
        pass #self.setUp()
    
unittest.main()
