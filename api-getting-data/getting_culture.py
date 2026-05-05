require 'httparty'

/<author>/<Shakespeare>[..][/<lines>][,<title>][..][.<.json>]

import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

response = apis.entity.suggest(
   text = 'Shakespeare',
   TYPE = 'agent',
)
print('tolkien', response)
