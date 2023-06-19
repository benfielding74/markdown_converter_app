# Markdown Converter App

## Description

This is a command line which has a single purpose, to convert exported Confluence HTML files to Markdown for easier local editing. It is written in Python utilising the [Markdownify](<https://pypi.org/project/markdownify/>) module. You must have 'Export Space' permissions in Confluence to export your workspace or individual files to your local machine.

## Installation

The tool can be run in two ways:

  Clone the repo and install the dependencies. You must have Python and Pip installed on your machine:
  
  ```bash

  git clone https://github.com/benfielding74/markdown_converter_app.git
  cd markdown_converter_app
  pip install .

  ```

  Or there is a binary in the root folder. Move or copy the binary to your $PATH and set permissions with `chmod +x markdownconverter`.

## How to use

Your Confluence HTML export will download in a `.zip` file. Unzip this file to a convenient location, this will act as your source directory. If using the binary then run:

`markdownconverter -s <path to source directory or individual file>`

Or if running the package:

```bash

cd markdown_converter
python3 -m markdown_converter -s <path to source directory or path for file>

```

This will create the `.md` files within your source directory using the same name as the `.html` files and links will remain intact to any media within the source folder.

## Next steps

In tests I have found issues with markdownify handling tables and panels, so I would like to implement additional code to deal with this. I would also like to implement a test suite.