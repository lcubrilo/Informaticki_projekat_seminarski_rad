@echo off
setlocal enabledelayedexpansion

set "filename=%~1"
set "project_path=%~2"
set "basename=%~n1"
set "basename_mod=%basename%_2"
set "output_folder=%project_path%\.outputs"

if not exist "%output_folder%" mkdir "%output_folder%"

if "%filename%"=="" (
  echo Missing filename argument.
  goto :eof
)

if "%project_path%"=="" (
  echo Missing project path argument.
  goto :eof
)

:: Debug Info: Print out the variables
echo [Debug] filename = %filename%
echo [Debug] project_path = %project_path%
echo [Debug] basename = %basename%
echo [Debug] output_folder = %output_folder%

:: Add LaTeX-esque image captions to all imgs
python build_utils\convert_images.py "%project_path%\%filename%" "%output_folder%"

pandoc "%output_folder%\%basename_mod%.md" --css=styles.css -o "%output_folder%\%basename_mod%.html"
echo [Debug] Converted Markdown to HTML

:: Import HTML contents from iframes
python build_utils\convert_iframes.py "%output_folder%\%basename_mod%.html"
echo [Debug] Converted iframes in HTML

pandoc "%output_folder%\%basename_mod%.html" --pdf-engine="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe" --pdf-engine-opt="--page-size" --pdf-engine-opt="A4" -o "%output_folder%\%basename_mod%.pdf"
echo [Debug] Converted HTML to PDF
