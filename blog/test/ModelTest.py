import unittest

from blog import Session
from blog.Model import *


class ModelTest(unittest.TestCase):

    ID = -1

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def clean(self, clz, remove_id):
        """
        Remove the test record for the model class.

        clz:        The test record class.
        remove_id:  The id of the record to remove.
        """
        results = self.session.query(clz).filter(clz.id == remove_id).all()
        for result in results:
            self.session.delete(result)
        self.session.commit()

    def create_approval(self, new_id):
        self.clean(Approval, new_id)

        approval = Approval()
        approval.id = new_id
        approval.status = 'foo'
        approval.description = 'description'

        self.session.add(approval)
        self.session.commit()
        return approval

    def create_author_status(self, new_id):
        self.clean(AuthorStatus, new_id)

        status = AuthorStatus()
        status.id = new_id
        status.status = 'foo'
        status.description = 'description'
        self.session.add(status)
        self.session.commit()
        return status

    def test_approval(self):
        approval = self.create_approval(self.ID)
        loaded_approval = self.session.query(Approval).filter(Approval.id == self.ID).first()
        self.assertEqual(approval.id, loaded_approval.id)
        self.assertEqual(approval.status, loaded_approval.status)
        self.assertEqual(approval.description, loaded_approval.description)
        self.assertEqual(str(approval), str(loaded_approval))

        self.session.delete(loaded_approval)
        self.session.commit()

        self.clean(Approval, self.ID)

    def test_author(self):
        status = self.create_author_status(self.ID)

        self.clean(Author, self.ID)

        author = Author()
        author.id = self.ID
        author.login = 'foo'
        author.password = 'bar'
        author.email = 'baz'
        author.url = 'frobble'
        author.activation_key = 'activation'
        author.status = status
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
        self.assertEqual(author.created, loaded_author.created)
        self.assertEqual(str(author), str(loaded_author))

        self.clean(Author, self.ID)
        self.clean(AuthorStatus, self.ID)

    def test_author_status(self):
        status = self.create_author_status(self.ID)

        loaded_status = self.session.query(AuthorStatus).filter(AuthorStatus.id == self.ID).first()
        self.assertEqual(status.id, loaded_status.id)
        self.assertEqual(status.status, loaded_status.status)
        self.assertEqual(status.description, loaded_status.description)
        self.assertEqual(str(status), str(loaded_status))

        self.clean(AuthorStatus, self.ID)
