@echo off
setlocal enabledelayedexpansion

set "filename=%~1"
set "project_path=%~2"
set "basename=%~n1"
set "basename_mod=%basename%_2"
set "output_folder=%project_path%\.outputs"
set "css_folder=%project_path%\build_utils\themes"
echo %css_folder%

if not exist "%output_folder%" mkdir "%output_folder%"

if "%filename%"=="" (
  echo Missing filename argument.
  goto :eof
)

if "%project_path%"=="" (
  echo Missing project path argument.
  goto :eof
)

:: Debug Info
echo [Debug] filename = %filename%
echo [Debug] project_path = %project_path%
echo [Debug] basename = %basename%
echo [Debug] output_folder = %output_folder%

:: Dynamically List available CSS files in the "themes" folder
echo Available CSS files in "%css_folder%" folder:
set "css_list="
for %%f in ("%css_folder%\*.css") do (
    echo %%~nxf
    set "css_list=!css_list! %%~nxf"
)

:: Use gum to choose a CSS file or set a default
set "chosen_css="
for /f %%a in ('gum choose %css_list% "Use default styles.css"') do set "chosen_css=%%a"

:: If no CSS file was chosen, use the default "styles.css"
if "%chosen_css%"=="" set "chosen_css=styles.css"

:: Add LaTeX-esque image captions to all imgs
::python build_utils\convert_images.py "%project_path%\%filename%" "%output_folder%"

echo off
pandoc "%output_folder%\%basename_mod%.md" --css="%css_folder%\%chosen_css%" -o "%output_folder%\%basename_mod%.html" >nul 2>&1
echo on
echo [Debug] Converted Markdown to HTML

:: Import HTML contents from iframes
echo off
python build_utils\convert_iframes.py "%output_folder%\%basename_mod%.html" "../build_utils/themes/%chosen_css%"
echo on
echo [Debug] Converted iframes in HTML

pandoc "%output_folder%\%basename_mod%.html" --pdf-engine="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe" --pdf-engine-opt="--page-size" --pdf-engine-opt="A4" -o "%output_folder%\%basename_mod%.pdf"
echo [Debug] Converted HTML to PDF
