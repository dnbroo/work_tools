; =======================================================================================
; Name ..........: JiraHelper V0.2
; Description ...: This script will automatically manage functions within H. The user will have majority control over how this works.
; AHK Version ...: AHK_A 1.1.30.1 (Unicode 32-bit) - Dec 26, 2018
; Platform ......: Windows 2000+
; Language ......: English (en-US)
; =======================================================================================

; Global ================================================================================
#SingleInstance, Force ; Allow only one running instance of script
#Persistent ; Keep script permanently running until terminated
#NoEnv ; Avoid checking empty variables to see if they are environment variables
;#Warn ; Enable warnings to assist with detecting common errors
;#NoTrayIcon ; Disable the tray icon of the script
SendMode, Input ; Recommended for new scripts due to its superior speed and reliability
SetWorkingDir, %A_ScriptDir% ; Change the working directory of the script
SetBatchLines, -1 ; Run script at maximum speed
OnExit, ExitSub ; Run a subroutine or function automatically when the script exits

;auto execution

Menu, Tray, Icon, Shell32.dll, 174 ; Change the tray icon
Menu, Tray, Tip, JIRA Helper ; Change the tooltip of the tray icon
Menu, Tray, NoStandard ; Remove all standard tray menu items
Menu, Tray, Add, Start JIRA, PreJIRA
Menu, Tray, Add, Copy JIRA Template, CopyJIRA
Menu, Tray, Add, Exit, ExitSub

global JiraString
global OneSchoolBool
global BomgarBool
global CCCBool
global DiffBrowserBool
global KBArticleFoundBool
global DiffBrowserBool
global AskTeamsBool
global ScreenshotBool
global HarBool
global UserCount
global Platform
global SchoolDistName
global SchoolDistPID
global counter
global Issue
global Step

;GUIWidth := 275, GUIHeight := 500


Return


^F2::
	Reload ; reloads the app
	Return

ExitSub:
	ExitApp ; Terminate the script unconditionally
	Return

PreJIRA:
	JiraString := ""
	JiraString := "JIRA REPLICATION STEPS`r`r"
	JiraString := JiraString "Site Name: "

	UserCount := 1
	OneSchoolBool := 0
	BomgarBool := 0
	CCCBool := 0
	DiffBrowserBool := 0
	KBArticleFoundBool := 0
	AskTeamsBool := 0
	ScreenshotBool := 0
	HarBool := 0
	Platform := "Platform"

	counter := 0
	step := 1
	Gosub, StartJIRA
	Return

StartJIRA:
	Gui, Font, s12
	Gui, +AlwaysOnTop
	Gui, Margin, 10, 10
	Gui, Add, Text, , Preliminary Questions:
	Gui, Add, Checkbox,   Checked%OneSchoolBool% vOneSchoolBool gSubmit_all, Is More Than One School Affected?
	Gui, Add, Text, , Platform:
	Gui, Add, DropDownList, vPlatform gSubmit_All,Platform||Ed|TCT|HRW
	Gui, Add, Text, , Troubleshooting Steps Taken:
	Gui, Add, Checkbox, Checked%BomgarBool% vBomgarBool gSubmit_all, Bomgar?
	Gui, Add, Checkbox, Checked%CCCBool% vCCCBool gSubmit_all, Clear cache and cookies?
	Gui, Add, Checkbox, Checked%DiffBrowserBool% vDiffBrowserBool gSubmit_all, Try a different browser?
	Gui, Add, Checkbox, Checked%KBArticleFoundBool% vKBArticleFoundBool gSubmit_all, Did you find any KB articles related? 
	Gui, Add, Checkbox, Checked%AskTeamsBool% vAskTeamsBool gSubmit_all, Did you search/ask in teams chat?
	Gui, Add, Checkbox, Checked%ScreenshotBool% vScreenshotBool gSubmit_all, Did you get a full screenshot?
	Gui, Add, Checkbox, Checked%HarBool% vHarBool gSubmit_all, HAR Log file collected/Applicable?
	Gui, Add, Text, ,Number of Affected Users:
	Gui, Add, Edit, w200 Number Center vUserCount gSubmit_all, %UserCount%
	Gui, Add, Button, w200 h40 Center Default vNextButton1 gSchoolGui, Next
	Gui, Show, AutoSize Center, JIRA Helper
	Return

SchoolGui:
	Gui, Destroy

	counter := %UserCount%

	if(Platform = "Platform"){
		MsgBox, , Error, Missing Platform Field. Please Try Again.
		GoSub, StartJIRA
		Return
	}

	if(Platform = "Ed")
		JiraString := JiraString "Ed (https://www.hmhco.com/ui/login/)`r`r"

	if(Platform = "TCT")
		JiraString := JiraString "TCT (https://www-k6.thinkcentral.com/ePC/start.do)`r`r"

	if(Platform = "HRW")
		JiraString := JiraString "HRW (https://my.hrw.com/index.jsp)`r`r"

	Gui, Font, s12
	Gui, +AlwaysOnTop +LastFound -Resize -DPIScale
	Gui, Margin, 10, 10

	if(OneSchoolBool = 0)
		Gui, Add, Text, , School Name:
	if(OneSchoolBool = 1)
		Gui, Add, Text, , District Name:

	Gui, Add, Edit,  w350 vSchoolDistName gSubmit_all,
	Gui, Add, Text, w225, PID:
	Gui, Add, Edit,  w350 vSchoolDistPID gSubmit_all,
	Gui, Add, Button, w350 Default gAppendSchool, Next
	Gui, Show, , School Info

	Return

GrabUserGui:

	Gui, Destroy

	if(counter < UserCount)
	{
		Gui, +AlwaysOnTop -DPIScale
		Gui, Font, s12
		Gui, Add, Text, , Please enter user info here:
		Gui, Add, Text, , Platform:
		Gui, Add, DropDownList, w250 vR4 gSubmit_All,Platform||Ed|TCT|HRW
		Gui, Add, Text, , UN:
		Gui, Add, Edit,  w300 vR1 gSubmit_All,
		Gui, Add, Text, , Type:
		Gui, Add, DropDownList, w250 vR2 gSubmit_All,Select Type||Administrator|Teacher|Student
		Gui, Add, Text, , PID:
		Gui, Add, Edit, w300 vR3 gSubmit_All,
		Gui, Add, Button, w100 h35 gReset, Reset
		Gui, Add, Button, w300 Default gAppendUser, Next
		;Gui, Add, Button, % " x" 10 " y" 200 " w" 100 " h" 30, Back
		Gui, Show, , Jira
		counter++
		Return
	}

	GoSub, TroubleshootingAndOutcomes
	Return

Reset: ;CLEARS 2ND GUI FIELDS
	
	;This will reset the variables
	R1 := ""
	R2 := ""
	R3 := ""
	R4 := ""
	R5 := ""
	
	;This clears the edit fields
	GuiControl,,R1,
	GuiControl,,R2,|Select Type||Administrator|Teacher|Student
	GuiControl,,R3,
	GuiControl,,R4, |Platform||Ed|TCT|HRW
	Return
	
AppendSchool:
	Gui, Destroy
	
	if(OneSchoolBool = 0)
		JiraString := JiraString "School Name: "
	if(OneSchoolBool = 1)
		JiraString := JiraString "District Name: "
	
	JiraString := % JiraString . SchoolDistName
	JiraString := JiraString "`rPID: "
	JiraString := % JiraString . SchoolDistPID
	JiraString := JiraString "`r`rIssue:`r"
	
	Gui, Font, s12
	Gui, +AlwaysOnTop +LastFound -Resize -DPIScale
	Gui, Margin, 10, 10
	Gui, Add, Text, , Issue:
	Gui, Add, Edit,  w350 h200 vIssue gSubmit_all,
	Gui, Add, Button, w200 Default gAppendIssue, &Next
	Gui, Show, , School Info
	Return

AppendIssue:
	Gui, Destroy
	JiraString := % JiraString . Issue
	JiraString := JiraString "`r`r"
	JiraString := JiraString "User Information:`r"
	GoSub, GrabUserGui
	Return

AppendUser:
	if(R4 = "Ed")
		JiraString := JiraString " - Ed: https://support-app.br.hmheng.io/`r"

	if(R4 = "TCT")
		JiraString := JiraString " - TCT: http://admin-k6.thinkcentral.com/ePCAdmin/login`r"

	if(R4 = "HRW")
		JiraString := JiraString " - HRW: http://support.hrw.com/menu_page.jsp`r"

	JiraString := JiraString " - Username: "
	JiraString := JiraString R1
	JiraString := JiraString "`r"
	JiraString := JiraString " - Role: "
	JiraString := JiraString R2
	JiraString := JiraString "`r"
	JiraString := JiraString " - PID: "
	JiraString := JiraString R3
	JiraString := JiraString "`r`r"

	;This will reset the variables
	R1 := ""
	R2 := ""
	R3 := ""
	R4 := ""
	R5 := ""

	;This clears the edit fields
	GuiControl,,R1,
	GuiControl,,R2,|Select Type||Administrator|Teacher|Student
	GuiControl,,R3,
	GuiControl,,R4, |Platform||Ed|TCT|HRW

	Gosub, GrabUserGui
	Return

TroubleshootingAndOutcomes:
	
	JiraString := JiraString "Troubleshooting Steps Taken:`r"

	if(BomgarBool = 0){
		JiraString := JiraString " - Bomgar: No`r"
	} else {
		JiraString := JiraString " - Bomgar: Yes`r"
	}

	if(CCCBool = 0){
		JiraString := JiraString " - Cleared Cache and Cookies: No`r"
	} else {
		JiraString := JiraString " - Cleared Cache and Cookies: Yes`r"
	}

	if(DiffBrowserBool = 0){
		JiraString := JiraString " - Tried Different Browser: No`r"
	} else {
		JiraString := JiraString " - Tried Different Browser: Yes`r"
	}

	if(KBArticleFoundBool = 0){
		JiraString := JiraString " - KB Article Found: No`r"
	} else {
		JiraString := JiraString " - KB Article Found: Yes`r"
	}
	
	if(AskTeamsBool = 0){
		JiraString := JiraString " - Search/Ask on Teams: No`r"
	} else {
		JiraString := JiraString " - Search/Ask on Teams: Yes`r"
	}

	if(ScreenshotBool = 0){
		JiraString := JiraString " - Full Screenshot Captured: No`r"
	} else {
		JiraString := JiraString " - Full Screenshot Captured: No`r"
	}

	if(HarBool = 0){
		JiraString := JiraString " - Har File Captured: No`r`r"
	} else {
		JiraString := JiraString " - Har File Captured: Yes`r`r"
	}

	GoSub, ReplicationGui

	Return

ReplicationGui:
	JiraString := JiraString "Replication Steps:`r"
	Gui, 2:Font, s12
	Gui, 2:+AlwaysOnTop -SysMenu -DPIScale
	Gui, 2:Add, Text, w100, Step %step%:
	Gui, 2:Add, Edit, w600 vCurrentStep gSubmit_All, %R5%
	Gui, 2:Add, Button, w100 Default gJiraStepper, Next
	Gui, 2:Add, Button, w100, Save
	Gui, 2:Show, , Replication
	Return

JiraStepper: ; This will continue to grab JIRA steps until quit.
	JiraString := JiraString "`r"
	JiraString := JiraString Step
	JiraString := JiraString ": "
	JiraString := JiraString CurrentStep

	GuiControl,, Step, Step %Step%:
	GuiControl,, CurrentStep,
	Gui, 2:

	Step++
	Return

2ButtonSave:
	JiraString := JiraString "`r"
	JiraString := JiraString "`r"
	JiraString := JiraString "Expected Results: "
	JiraString := JiraString "`r"
	JiraString := JiraString "`r"
	JiraString := JiraString "Actual Results: "
	clipboard = %JiraString%
	Gui, 2:Destroy
	MsgBox, , Success, Success! The JIRA Replication Steps have been copied to your clipboard!,
	Return

Submit_All: ;this submits the values into variables as soon as a change is made
	Gui, Submit, NoHide
	Return

ButtonNext:
	Return

GuiClose:
	Gui, Destroy
	Gui, 2:Destroy
	Return

CopyJIRA:
	copyString := ""
	copyString := copyString "JIRA REPLICATION STEPS`r`r"
	copyString := copyString "Site Name: `r`r"
	copyString := copyString "School Name(s): (If issue only affects certain school sites and not whole District)`r"
	copyString := copyString "PID: `r`r"
	copyString := copyString "Issue: `r`r"
	copyString := copyString "User(s) Affected(PID associated to the account(s) Must also be included): `r`r"
	copyString := copyString "Troubleshooting done and outcomes: `r`r"
	copyString := copyString "Replication Steps(Every Click should be a step): `r"
	copyString := copyString "`tBomgar? `r"
	copyString := copyString "`tClear cache and cookies? `r"
	copyString := copyString "`tTry different browser? `r"
	copyString := copyString "`tDid you find any KB articles related? `r"
	copyString := copyString "`tDid you search/ask in teams chat? `r"
	copyString := copyString "`tFull screenshot? `r"
	copyString := copyString "`tHAR Log file collected? `r`r"
	copyString := copyString "Expected Result: `r`r"
	copyString := copyString "Actual Result: "
	clipboard = %copyString%
	Return