from django.test import SimpleTestCase
from django.db.utils import OperationalError
from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2OError


# 데이터베이스 연결 시뮬레이션
@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandTests(SimpleTestCase):
    # db 연결에 한방에 성공했을 때
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)

    # db 연결에 지연 됐을 때
    @patch('time.sleep')
    @patch('django.db.utils.ConnectionHandler.__getitem__')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OError] \
            + [OperationalError]*5 + [True]
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)
        