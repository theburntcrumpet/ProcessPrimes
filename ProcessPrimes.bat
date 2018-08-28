@ECHO OFF
del C:\ProcessPrimes /Q
echo Installing Chocolatey
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo Installing Python and Git
cmd /C "choco install git python notepadplusplus -y"

IF NOT EXIST C:\ProcessPrimes GOTO CLONE
GOTO PULL

:benchmark
echo Running the benchmark
cmd /C "cd C:\ProcessPrimes && python ProcessPrimes.py"
cmd /C "START notepad++ C:\ProcessPrimes\ProcessPrimes.log"
exit

:CLONE
echo Cloning repository
cmd /C "cd C:\ && git clone https://github.com/theburntcrumpet/ProcessPrimes.git"
GOTO benchmark

:PULL
echo Updating repository
cmd /C "cd C:\ProcessPrimes && git pull"
GOTO benchmark