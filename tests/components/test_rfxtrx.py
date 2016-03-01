"""
tests.components.test_rfxtrx
~~~~~~~~~~~~~~~~~~~~~~~~~

Tests Rfxtrx component.
"""
# pylint: disable=too-many-public-methods,protected-access
import unittest

from homeassistant.components import rfxtrx as rfxtrx
from unittest.mock import patch

from tests.common import get_test_home_assistant


class TestSun(unittest.TestCase):
    """ Test the sun module. """

    def setUp(self):
        """ setup hass """
        self.hass = get_test_home_assistant(0)

    def tearDown(self):
        """ Stop down stuff we started. """
        rfxtrx.RECEIVED_EVT_SUBSCRIBERS = []
        rfxtrx.RFX_DEVICES = {}
        self.hass.stop()

    def test_default_config(self):
        """ Test config """
        import RFXtrx as rfxtrxmod

        rfxobject =\
            rfxtrxmod.Core("", transport_protocol=rfxtrxmod.DummyTransport)

        with patch('RFXtrx.Core',
                   return_value=rfxobject):
            self.assertTrue(rfxtrx.setup(self.hass, {
                'rfxtrx': {
                    'device': '/dev/serial/by-id/usb' +
                              '-RFXCOM_RFXtrx433_A1Y0NJGR-if00-port0'}
            }))
