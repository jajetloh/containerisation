import streamlit.web.cli

# Add imports here if 'ModuleNotFoundError'
import streamlit.runtime.scriptrunner.magic_funcs

if __name__ == '__main__':
    streamlit.web.cli._main_run_clExplicit('main_3.py', 'streamlit run')