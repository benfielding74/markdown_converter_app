'''Module to convert single or multiple confluence HTML files to markdown'''

import os
import logging
import click
from markdownify import markdownify as md
from tqdm import tqdm

logging.basicConfig(filename='app.log',
                     filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',
                     level=logging.INFO)

def convert_html_to_markdown(html_file):
    '''Converts single html file to markdown and outputs to source dir'''
    with open(html_file, 'r', encoding="utf-8") as file:
        html_content = file.read()
        markdown_content = md(html_content)

    output_file = os.path.splitext(os.path.basename(html_file))[0] + '.md'
    output_directory = os.path.splitext(os.path.dirname(html_file))[0]
    output_path = os.path.join(output_directory, output_file)

    with open(output_path, 'w', encoding="utf-8") as file:
        file.write(markdown_content)

def convert_all_html_files(source_directory):
    '''Converts all html comtents of source dir to markdown'''
    html_files = [file for file in os.listdir(source_directory) if file.endswith('.html')]

    if len(html_files) == 0:
        print("No files to convert")

    else:
        progress_bar = tqdm(total=len(html_files), desc="Processing files", unit='file(s)')

        for html_file in html_files:
            html_file_path = os.path.join(source_directory, html_file)
            convert_html_to_markdown(html_file_path)

            progress_bar.update(1)

        progress_bar.close()
        click.echo('Conversion completed successfully.')

@click.command()
@click.option('--source', '-s', help='Source directory or file path')
def main(source):
    '''Takes input and checks if source is a dir or filepath'''
    if os.path.isdir(source):
        convert_all_html_files(source)
    elif os.path.isfile(source):
        convert_html_to_markdown(source)
        click.echo('Conversion completed successfully.')
    else:
        click.echo('Invalid source path.')


if __name__ == '__main__':
    main()
