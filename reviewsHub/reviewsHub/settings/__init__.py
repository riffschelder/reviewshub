import os

from base import *

if os.getenv('REVIEWS_HUB_ENVIRON') == 'production':
    from production import *
else:
    from production import *
