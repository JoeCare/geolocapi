from django.test import TestCase
from .factorial_tests import CompanyFactory
from ..models import Company


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
