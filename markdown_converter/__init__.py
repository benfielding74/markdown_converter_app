# Import any modules or submodules that you want to make accessible when importing your module
from .main import convert_html_to_markdown, convert_all_html_files

VERSION = '1.0.0'

__all__ = ['convert_html_to_markdown', 'convert_all_html_files', 'VERSION']
