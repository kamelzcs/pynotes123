#! /bin/bash
python web/template.py --compile templates && dev_appserver.py .
