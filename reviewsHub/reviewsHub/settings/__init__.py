import os

from base import *
owl_env = os.getenv("OWL_ENV", 'local')

if os.getenv('REVIEWS_HUB_ENVIRON') == 'production':
    from production import *
else:
    from local import *
