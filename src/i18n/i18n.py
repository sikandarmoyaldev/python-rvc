import json
import locale
import os
from pathlib import Path

from tools.file_io import read_text

# Calculate the absolute path to the locale directory based on this file's location
_I18N_DIR = Path(__file__).parent
_LOCALE_DIR = _I18N_DIR / "locale"


def load_language_list(language):
    locale_file = _LOCALE_DIR / f"{language}.json"
    return json.loads(read_text(str(locale_file)))


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = locale.getdefaultlocale()[0]
        
        # Check existence using the absolute path
        locale_file = _LOCALE_DIR / f"{language}.json"
        
        if not locale_file.exists():
            language = "en_US"
            
        self.language = language
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return f"Use Language: {self.language}"
    