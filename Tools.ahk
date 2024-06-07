
#Requires Autohotkey v2
;SetWorkingDir, %A_ScriptDir% ; Change the working directory of the script
;AutoGUI creator: Alguimist autohotkey.com/boards/viewtopic.php?f=64&t=89901
;AHKv2converter creator: github.com/mmikeww/AHK-v2-script-converter
;EasyAutoGUI-AHKv2 github.com/samfisherirl/Easy-Auto-GUI-for-AHK-v2

; GLOBAL VARIABLES
; ====================
global omni := 0

; GUI FOR MAIN TOOLSET
; ====================

if A_LineFile = A_ScriptFullPath && !A_IsCompiled
{
	myGui := Constructor()
	myGui.Show("w281 h530")
}

Constructor()
{	
	; global variables
	global custom_url_pid := -1
	global custom_url_platform := "Ed"
	global phone_status := -1
	global setting_c := 1
	global setting_ac := 0
	global no_priority_days_out := 2
	global priority_days_out := 1

	; layout of GUI
	myGui := Gui()
	myGui.Opt("-DPIScale")
	myGui.SetFont(, "Segoe UI")
	myGui.Add("GroupBox", "x8 y0 w265 h107", "Custom Link")
	Edit1 := myGui.Add("Edit", "x64 y24 w197 h28 Number")
	myGui.Add("Text", "x16 y24 w30 h23 +0x200", "PID:")
	ButtonCustomURL1 := myGui.Add("Button", "x144 y64 w120 h28", "&Custom_URL")
	DropDownList1 := myGui.Add("DropDownList", "x16 y64 w123 Choose1", ["Ed", "TCT", "HRW"])
	myGui.Add("GroupBox", "x8 y112 w265 h167", "Set Phone Status")
	Radio1 := myGui.Add("Radio", "x16 y136 w101 h27", "Ready")
	Radio2 := myGui.Add("Radio", "x128 y136 w138 h27", "Case Processing")
	Radio3 := myGui.Add("Radio", "x16 y168 w101 h27", "After Call")
	Radio4 := myGui.Add("Radio", "x128 y168 w138 h27", "Outbound Call")
	Radio5 := myGui.Add("Radio", "x16 y200 w101 h27", "Personal")
	Radio6 := myGui.Add("Radio", "x128 y200 w138 h27", "Break")
	Radio7 := myGui.Add("Radio", "x16 y232 w101 h27", "Lunch")
	Radio8 := myGui.Add("Radio", "x128 y232 w138 h27", "Meeting")
	myGui.Add("GroupBox", "x8 y384 w265 h138", "Settings")
	CheckBox1 := myGui.Add("CheckBox", "x16 y408 w47 h26 +Checked", "C")
	CheckBox2 := myGui.Add("CheckBox", "x16 y437 w47 h26 +Checked", "AR")
	myGui.Add("Text", "x88 y424 w84 h26 +0x200", "No Priority:")
	myGui.Add("Text", "x88 y456 w84 h26 +0x200", "Priority:")
	myGui.Add("GroupBox", "x80 y400 w186 h96", "Days Out")
	DropDownList2 := myGui.Add("DropDownList", "x184 y424 w70 Choose1", ["2", "", "1", "2", "3", "4", "5", "6", "7"])
	DropDownList3 := myGui.Add("DropDownList", "x184 y456 w70 Choose1", ["1", "", "1", "2", "3", "4", "5", "6", "7"])
	myGui.Add("GroupBox", "x8 y288 w265 h89", "Tools")
	ButtonRosterHelper1 := myGui.Add("Button", "x16 y312 w121 h27", "Roster_Helper")
	global o_count := myGui.Add("Text", "x16 y496 w47 h23 +0x200", "0")
	ButtonMouseSpy := myGui.Add("Button", "x144 y312 w121 h27", "Mouse Spy")
	ButtonJiraHelper1 := myGui.Add("Button", "x16 y344 w121 h27", "Jira_Helper")
	myGui.Title := "🛠"

	; event handlers
	; custom url
	Edit1.OnEvent("Change", OnEventHandler)
	ButtonCustomURL1.OnEvent("Click", OnEventHandler)
	ButtonCustomURL1.OnEvent("Click", custom_link_creator)
	DropDownList1.OnEvent("Change", OnEventHandler)

	; phone status
	Radio1.OnEvent("Click", event_update_phone_status)
	Radio2.OnEvent("Click", event_update_phone_status)
	Radio3.OnEvent("Click", event_update_phone_status)
	Radio4.OnEvent("Click", event_update_phone_status)
	Radio5.OnEvent("Click", event_update_phone_status)
	Radio6.OnEvent("Click", event_update_phone_status)
	Radio7.OnEvent("Click", event_update_phone_status)
	Radio8.OnEvent("Click", event_update_phone_status)

	; c checkbox
	CheckBox1.OnEvent("Click", OnEventHandler)
	CheckBox2.OnEvent("Click", OnEventHandler)

	; priority days out
	DropDownList2.OnEvent("Change", OnEventHandler)
	DropDownList2.OnEvent("Change", setting_c_handler)
	DropDownList3.OnEvent("Change", OnEventHandler)

	; tools
	ButtonRosterHelper1.OnEvent("Click", OnEventHandler)
	ButtonRosterHelper1.OnEvent("Click", run_roster_helper)
	ButtonMouseSpy.OnEvent("Click", run_mouse_spy)
	ButtonJiraHelper1.OnEvent("Click", OnEventHandler)
	ButtonJiraHelper1.OnEvent("Click", run_jira_helper)

	; gui events
	myGui.OnEvent('Close', (*) => ExitApp())
	
	ToolTipHandler_c(*) {
		ToolTip "Caffeine"
	}
	
	; value setters
	OnEventHandler(*) {
		custom_url_pid := Edit1.Value
		custom_url_platform := DropDownList1.Value
		setting_c := CheckBox1.Value
		setting_ac := CheckBox2.Value
		no_priority_days_out := DropDownList2.Value
		priority_days_out := DropDownList3.Value
	}

	setting_c_handler(*) {

	}


	; sets our phone value
	event_update_phone_status(*){
		; event
		; 1 - ready
		; 2 - case_processing
		; 3 - after_call
		; 4 - outbound_call
		; 5 - personal
		; 6 - break
		; 7 - lunch
		; 8 - meeting

		if (Radio1.Value){
			phone_status := 1
			set_phone()
		}
		if (Radio2.Value){
			phone_status := 2
			set_phone()
		}
		if (Radio3.Value){
			phone_status := 3
			set_phone()
		}
		if (Radio4.Value){
			phone_status := 4
			set_phone()
		}
		if (Radio5.Value){
			phone_status := 5
			set_phone()
		}
		if (Radio6.Value){
			phone_status := 6
			set_phone()
		}
		if (Radio7.Value){
			phone_status := 7
			set_phone()
		}
		if (Radio8.Value){
			phone_status := 8
			set_phone()
		}
	}
	
	return myGui
}

; FUNCTIONS
; ====================

test_function(*) {
	MsgBox custom_url_pid
}

custom_link_creator(*) {

	if(custom_url_pid = ""){
		MsgBox "You must enter a PID into the field. Please try again."
		Return
	}

	; ed
	if(custom_url_platform = 1){
		A_Clipboard := Format("https://www.hmhco.com/one/login/?connection={:d}", custom_url_pid)
		Return
	}

	; tct
	if(custom_url_platform = 2){
		A_Clipboard := Format("https://www-k6.thinkcentral.com/ePC/start.do?orgID={:d}", custom_url_pid)
		Return
	}

	; hrw
	if(custom_url_platform = 3){
		A_Clipboard := Format("https://my.hrw.com/index.jsp?state=yy&district={:d}", custom_url_pid)
		Return
	}

	MsgBox "Error creating custom link"
	Return

}

set_phone() {

	; event
	; 1 - ready
	; 2 - case_processing
	; 3 - after_call
	; 4 - outbound_call
	; 5 - personal
	; 6 - break
	; 7 - lunch
	; 8 - meeting

	switch
	{
		case phone_status == 1: set_phone_ready()
		case phone_status == 2: set_phone_case_processing()
		case phone_status == 3: set_phone_after_call()
		case phone_status == 4: set_phone_outbound_call()
		case phone_status == 5: set_phone_personal()
		case phone_status == 6: set_phone_break()
		case phone_status == 7: set_phone_lunch()
		case phone_status == 8: set_phone_meeting()
	}
	return
}

set_phone_ready() {
	align_avaya()
	MouseClick "Left", 40, 69 ;clicks auto in
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		start_c()
	}
}

set_phone_case_processing() {
	align_avaya()
	phone_aux_menu(11)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		start_c()
	}
}

set_phone_after_call() {
	return
	;align_avaya()
	;MouseClick "Left", 140, 69 ;clicks aftercall
	;CoordMode "Mouse", "Screen"
	;sleep_time := Random 2000, 60000
	;Sleep sleep_time
}

set_phone_outbound_call() {
	align_avaya()
	phone_aux_menu(17)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		start_c()
	}
}

set_phone_personal() {
	align_avaya()
	phone_aux_menu(7)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		end_c()
	}
}

set_phone_break() {
	align_avaya()
	phone_aux_menu(1)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		end_c()
	}
}

set_phone_lunch() {
	align_avaya()
	phone_aux_menu(2)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		end_c()
	}
}

set_phone_meeting() {
	align_avaya()
	phone_aux_menu(3)
	CoordMode "Mouse", "Screen"

	if(setting_c) {
		start_c()
	}
}

phone_aux_menu(num) {
	MouseClick "Left", 72, 19 ; clicks bubble
	Sleep 100
	Send "+{Tab 2}" ; tabs to aux menu
	Send "{Enter}" ; enters aux menu

	Loop num { ; loops tab to get to case processing time
		Send "{Tab}"
		Sleep 20
	}

	Send "{Enter}" ; selects it
}

align_avaya() {
	WinActivate "Avaya one-X Agent"
	WinMove 882,900,,, "Avaya one-X Agent"
	CoordMode "Mouse", "Window"
}

start_c() {
	If not ProcessExist("c.exe")
		Run "c.exe"
}

end_c() {
	If ProcessExist("c.exe")
		ProcessClose "c.exe"
}

run_mouse_spy(*) {
	Run "MouseSpy.ahk"
}

run_jira_helper(*) {
	Run "JiraHelper.ahk"
}

run_roster_helper(*) {
	Run A_ComSpec
	Sleep 100
	Send 'python "C:\Users\BrewerD\Documents\AHK\ahk_tools\rosterHelper.py"'
	Send "{Enter}"
}

; HOTKEYS 
; ====================

^F1:: {
	Reload
}

^+o:: {
	global omni
	omni := omni + 1
	o_count.Text := omni
}