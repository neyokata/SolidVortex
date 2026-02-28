# test_solidvortex.py
"""
Tests for SolidVortex module.
"""

import unittest
from solidvortex import SolidVortex

class TestSolidVortex(unittest.TestCase):
    """Test cases for SolidVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidVortex()
        self.assertIsInstance(instance, SolidVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
