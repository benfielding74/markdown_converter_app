# Import any modules or submodules that you want to make accessible when importing your module
from .markdown_converter import convert_html_to_markdown, convert_all_html_files

VERSION = '0.1.0'

__all__ = ['convert_html_to_markdown', 'convert_all_html_files', 'VERSION']
