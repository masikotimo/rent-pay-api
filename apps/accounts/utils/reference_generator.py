import random
import string

def generate_tenant_reference():
    """Generate a unique tenant reference number in format: TN-XXXXX"""
    chars = string.ascii_uppercase + string.digits
    reference = 'TN-' + ''.join(random.choices(chars, k=5))
    return reference