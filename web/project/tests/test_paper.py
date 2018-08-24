# project/test_papers.py

import os
import unittest

from project import app, db

TEST_DB = 'test.db'


class PapersTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()


    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Scratch Paper App', response.data)
        self.assertIn(b'Add Paper', response.data)

    def test_main_page_query_results(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertIn(b'Add a New Paper', response.data)

    def test_add_paper(self):
        response = self.app.post(
            '/add',
            data=dict(name='nose2 test 1',
                      location='this is a test'),
            follow_redirects=True)
        self.assertIn(b'New paper, nose2 test 1, added!', response.data)

if __name__ == "__main__":
    unittest.main()
