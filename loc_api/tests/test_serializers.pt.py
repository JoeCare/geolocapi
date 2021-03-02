from ..serializers import CompanySerializer
from .factorial_tests import CompanyFactory
from .test_models import TestCase


class CompanySerializerTest(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        company = CompanyFactory()
        for field_name in [
            'id', 'name', 'description', 'website', 'street_line_1', 'street_line_2',
            'city', 'state', 'zipcode'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(company, field_name)
            )
