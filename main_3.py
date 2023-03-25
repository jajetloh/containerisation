# From https://stackoverflow.com/questions/62760929/how-can-i-run-a-streamlit-app-from-within-a-python-script

import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "main_3_streamlit.py"]
    sys.exit(stcli.main())