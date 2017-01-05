"""
Runs the website
"""
from app import website
import os
import sys

# Cheaty, cheaty hack to assume utf8 instead of ascii
reload(sys)
sys.setdefaultencoding('utf8')

# Run the actual site
runningOnHeroku = 'PORT' in os.environ
if runningOnHeroku:
	website.run(debug=False, host="0.0.0.0", port=os.environ['PORT'])
else:
	website.run(debug=True, port=5000)
