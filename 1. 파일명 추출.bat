@echo off

(for /f "delims=" %%a in ('dir /b /a-d ^| findstr /v /i ".bat ^file_names.txt"') do (
    echo %%~na
)) > file_names.txt