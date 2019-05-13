@echo off

set SHOW=WFG


set SHOW_PATH=E:/Google Drive/WORK/MIND_MACHINE/SHOWS/%SHOW%
set SHOW_PROMPTMOD=[%SHOW%]
set OCIO=%SHOW_PATH%\pipeline\color\8001001409.ocio
set NUKE_VER=C:\Program Files\Nuke11.3v4\Nuke11.3.exe
set WORK_PATH=%SHOW_PATH%/production/shot

title %SHOW%

DOSKEY nuke=start "nuke" /B "%NUKE_VER%" $*

cd /D E:/Google Drive/WORK/MIND_MACHINE/SHOWS/%SHOW%


DOSKEY data=cd /D E:/DATA/%SHOW%_DATA
DOSKEY home=cd /D %SHOW_PATH%
DOSKEY work=cd /D %WORK_PATH%

echo SHOW set to %SHOW_PROMPTMOD% & echo.
echo Please use commands: 
echo data - jump to data repository for this show.
echo home - jump to the base directory for this show.
echo work - jump to the /shot/ directory for this show.
echo ss ^<seq^> ^<shot^> - setup environment for working on a shot.

"%BIN_PATH%/prompt_modifier.cmd"
