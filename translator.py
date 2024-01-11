import os
import glob

from srtranslator import SrtFile
from srtranslator.translators.deepl_api import DeeplApi
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.selenium_utils import create_proxy, create_driver

# DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
# if DEEPL_API_KEY is None:
# 	print("No API key found. Please set the DEEPL_API_KEY using 'export' or 'set'")
# 	exit(1)

folder = "./videos/CS285/SRT"
for filepath in glob.glob(os.path.join(folder, "*.srt")):
    # translator = DeeplApi(DEEPL_API_KEY)
    translator = DeeplTranslator()

    srt = SrtFile(filepath)
    srt.translate(translator, "en", "ko")
    srt.wrap_lines()
    
    new_filename = "KOR_" + os.path.basename(filepath)
    new_filepath = os.path.join(folder, new_filename)
    srt.save(new_filepath)

    translator.quit()
    print(f"Translated and saved: {new_filepath}")