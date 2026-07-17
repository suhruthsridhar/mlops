@echo off
:menu
cls

echo       MANAGEMENT SYSTEM RUNNER

echo 1. Run Employee Management System
echo 2. Run Student Record Generator
echo 3. Exit

echo.

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" goto run_employee
if "%choice%"=="2" goto run_student
if "%choice%"=="3" goto end

echo Invalid choice! Please select 1, 2, or 3.
pause
goto menu

:run_employee
echo.
echo Running Employee Management System...
python employee.py
echo.
pause
goto menu

:run_student
echo.
echo Running Student Record Generator...
python student.py
echo.
pause
goto menu

:end
echo Goodbye!
exit