@echo off

IF [%SHOW%]==[] (
	echo Please set the SHOW first.
	EXIT /B
	)

IF "%1"=="" (
	python "%PIPELINE_REPO%/set_shot.py"
	EXIT /B
	)

IF "%2"=="" (
	FOR /f "tokens=1,2 delims=_" %%a IN ("%1") do set SEQ=%%a&set SHOT=%%b
	) ELSE (
	set SEQ=%1
	set SHOT=%2
	)



set SHOT_PATH=%SHOW_PATH%/production/shot/%SEQ%/%SHOT%
set SHOT_PROMPTMOD=[%SEQ%_%SHOT%]

set COMP_PATH=%SHOT_PATH%/comp/nuke
set RENDER_PATH=%SHOT_PATH%/comp/render
set PRECOMP_PATH=%SHOT_PATH%/comp/precomp

TITLE %SHOW% %SEQ% %SHOT%

@echo Setting shot to: %SHOT_PROMPTMOD% & echo.
cd /d %SHOT_PATH%
dir

DOSKEY comp=cd /d %COMP_PATH% $t ls -ltr
DOSKEY render=cd /d %RENDER_PATH% $t ls -ltr
DOSKEY precomp=cd /d %PRECOMP_PATH% $t ls -ltr
DOSKEY plate=cd /d %SHOT_PATH%/plate $t ls -ltr
DOSKEY shot=cd /d %SHOT_PATH%
DOSKEY nukeme=python "%PIPELINE_REPO%/nukeme.py"

echo Please use commands: 
echo comp - jump to comp script directory for this shot.
echo render - jump to the comp renders directory for this shot.
echo precomp - jump to the precomp renders for this shot.
echo shot - jump back to the base directory for this shot.
echo nukeme - load latest nuke script from from the ./comp/nuke/ folder
echo.

%BIN_PATH%/prompt_modifier.cmd

