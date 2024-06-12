# Work Tools
This application was made to allow for automation throughout my daily job. Automates small tasks that need to be done several times throughout the course of a single day. 

<img src="https://github.com/dnbroo/work_tools/raw/main/images/tools_image" width="150">

## Features

&nbsp;&nbsp;✅ **Custom Link Generation** for login platforms  
&nbsp;&nbsp;✅ Avaya Soft Phone Control  
&nbsp;&nbsp;✅ **Feedback and Audio** for reminders and alerts  
&nbsp;&nbsp;✅ Additional Helper Tool Launching  
&nbsp;&nbsp;✅ Plan Of Action setter with **automatic date configuration**  
&nbsp;&nbsp;✅ Daily work tracker for keeping track of work completed  
&nbsp;&nbsp;✅ **Hotkey support**  

### Custom Link Generation
Allows us to quickly create custom links for our clients. This feature works because the beginning URL's stay the same. Each school has a special identifier in our system that only needs to be appended to the URL. 

### Avaya Soft Phone Control
This feature allows us to set our phone status with the click of a button. Its extremely fast and works very efficiently. It also has audio reminders and audio alerts when breaks or lunches are over allowing you to remember when scheduled times are over. 

### Additional Helper Tool Launching
On top of this application, I have built a number of other applications that help us comb through rostering data using the `OneRoster` or `SFF` form factor. 

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Roster Helper
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/dnbroo/work_tools/raw/main/images/roster_helper.gif" width="800">  
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Features  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Allows for **instantanious** user lookups using large data set CSV values (over 1m+ entries)(BigO(n^2)).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Allows to grab any class data for a found user.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Dropped troubleshooting time down from 10-15 minutes to ~30 seconds.    

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jira Helper
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description here

### Plan of Action Setter with Automatic Date Configuration
This allows us to *automagically* set Plans of Action (POAs) within Salesforce. The convenient drop down boxes allows us to set how many days out we want it to be. It will automatically set the correct date in business days and account for weekends. 
> Note: Currently only weekends are supported. Holidays and scheduled times off are not accounted for.

### A Built in work tracker that keeps track of work completed for the day
No more are the days of pieces of paper and pencils with tally marks scattered randomly in a convenient spot. No more will you have to worry if you've grabbed 6 or 8 cases for the day. Using this tracker you can use a simple hotkey to add +1 to the tracker so that you can rest assured knowing that your case history is conveniently stored in a safe place. 

### Hotkey Support
This was built to accustom several working methods including being used with a steam deck or even with a laptop on the go. The hotkeys allow you to control the application globally with a simple key press.
| Key | Function |
|--|--|
| Ctrl + F1 | Allows the app to be rebuilt (for dev purposes) |
| Ctrl + Shift + O | Adds 1 to our daily work tracker |
| Ctrl + Shift + P | Sets our non-priority case POA |
| Ctrl + Shift + Alt + P | Sets our non-priority case POA (with no previous POA set) |
| Ctrl + Shift + L | Sets our priority case POA |
| Ctrl + Shift + Alt + L | Sets our priority case POA (with no previous POA set) |
| Ctrl + F5 | Sets our phone to ready |
| Ctrl + F6 | Sets our phone to case processing |
| Ctrl + F7 | Sets our phone to break |
| Ctrl + F8 | Sets our phone to lunch |
| Ctrl + F9 | Sets our phone to personal |
| Ctrl + F10 | Sets our phone to outbound call |
| Ctrl + F11 | Sets our phone to after call |
