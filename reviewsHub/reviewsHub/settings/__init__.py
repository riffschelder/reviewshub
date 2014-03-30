import os

from base import *

if os.environ['REVIEWS_HUB_ENVIRON'] == 'production':
    from production import *
else:
    from local import *
