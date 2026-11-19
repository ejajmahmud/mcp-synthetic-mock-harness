"""Tests for Mock Harness."""
import unittest
from mcp_synthetic_mock_harness.core import SyntheticMockHarness, MockResponse

class TestSyntheticMockHarness(unittest.TestCase):
    def test_mocking_and_assertions(self):
        h = SyntheticMockHarness()
        h.register_mock("echo", lambda a: MockResponse(a.get("msg", "")))
        res = h.invoke("echo", {"msg": "hello"})
        self.assertEqual(res, "hello")
        h.assert_called("echo", times=1)

        with self.assertRaises(KeyError):
            h.invoke("unregistered", {})
