import unittest

from blog import Session
from blog.Model import *


class ModelTest(unittest.TestCase):

    ID = -1

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def clean(self, clz):
        """
        Remove the test record for the model class.

        clz: The test record class.
        """
        results = self.session.query(Approval).filter(clz.id == self.ID).all()
        for result in results:
            self.session.delete(result)
        self.session.commit()

    def test_approval(self):
        self.clean(Approval)

        approval = Approval()
        approval.id = self.ID
        approval.status = 'foo'
        approval.description = 'description'

        self.session.add(approval)
        self.session.commit()

        loaded_approval = self.session.query(Approval).filter(Approval.id == self.ID).first()
        self.assertEqual(approval.id, loaded_approval.id)
        self.assertEqual(approval.status, loaded_approval.status)
        self.assertEqual(approval.description, loaded_approval.description)
        self.assertEqual(str(approval), str(loaded_approval))

        self.session.delete(loaded_approval)
        self.session.commit()

        self.clean(Approval)

    def test_author(self):
        self.clean(Author)
        self.clean(AuthorStatus)

        status = AuthorStatus()
        status.id = self.ID
        status.status = 'foo'
        status.description = 'description'
        self.session.add(status)
        self.session.commit()

        loaded_status = self.session.query(AuthorStatus).filter(Author.id == self.ID).first()
        self.assertEqual(status.id, loaded_status.id)
        self.assertEqual(status.status, loaded_status.status)
        self.assertEqual(status.description, loaded_status.description)
        self.assertEqual(str(status), str(loaded_status))

        author = Author()
        author.id = self.ID
        author.login = 'foo'
        author.password = 'bar'
        author.email = 'baz'
        author.url = 'frobble'
        author.activation_key = 'activation'
        author.status = loaded_status
        author.display_name = 'name'
        self.session.add(author)
        self.session.commit()

        loaded_author = self.session.query(Author).filter(Author.id == self.ID).first()
        self.assertEqual(author.id, loaded_author.id)
        self.assertEqual(author.login, loaded_author.login)
        self.assertEqual(author.password, loaded_author.password)
        self.assertEqual(author.email, loaded_author.email)
        self.assertEqual(author.url, loaded_author.url)
        self.assertEqual(author.activation_key, loaded_author.activation_key)
        self.assertEqual(author.status, loaded_author.status)
        self.assertEqual(author.display_name, loaded_author.display_name)
        self.assertIsNone(author.created)
        self.assertIsNotNone(loaded_author.created)
        self.assertNotEqual(str(author), str(loaded_author))

        self.clean(Author)
        self.clean(AuthorStatus)

