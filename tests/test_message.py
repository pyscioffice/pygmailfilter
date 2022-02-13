from unittest import TestCase
from pygmailfilter.message import Message


class MessageTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._message_dict = {
            "threadId": "abc123",
            "id": "myid123",
            "labelIds": ["important", "Label_123"],
            "payload": {
                "headers": [
                    {"name": "Subject", "value": "Test Email Subject"},
                    {"name": "From", "value": "sender@server.net"},
                    {"name": "To", "value": "me@mail.com, friend@provider.org"},
                ]
            }
        }
        cls.message = Message(message_dict=cls._message_dict)

    def test_subject(self):
        self.assertEqual(self.message.get_subject(), "Test Email Subject")

    def test_from(self):
        self.assertEqual(self.message.get_from(), "sender@server.net")

    def test_to(self):
        self.assertEqual(self.message.get_to(), ["me@mail.com", "friend@provider.org"])

    def test_email_id(self):
        self.assertEqual(self.message.get_email_id(), "myid123")

    def test_thread_id(self):
        self.assertEqual(self.message.get_thread_id(), "abc123")

    def test_label_ids(self):
        self.assertEqual(self.message.get_label_ids(), ["important", "Label_123"])

    def test_get_date(self):
        pass

    def test_get_content(self):
        pass
