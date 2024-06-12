# Work Tools
This application was made to allow for automation throughout my daily job. Automates small tasks that need to be done several times throughout the course of a single day. 

<img src="https://github.com/dnbroo/work_tools/raw/main/images/tools_image" width="150">

## &nbsp;&nbsp;Features

&nbsp;&nbsp;&nbsp;&nbsp;✅ **Custom Link Generation** for login platforms  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Avaya Soft Phone Control  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Feedback and Audio** for reminders and alerts  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Additional Helper Tool Launching  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Plan Of Action setter with **automatic date configuration**  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Daily work tracker for keeping track of work completed  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Hotkey support**  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Display Input Switcher**  

### Custom Link Generation
Allows us to quickly create custom links for our clients. This feature works because the beginning URL's stay the same. Each school has a special identifier in our system that only needs to be appended to the URL. 

### Avaya Soft Phone Control
This feature allows us to set our phone status with the click of a button. Its extremely fast and works very efficiently. It also has audio reminders and audio alerts when breaks or lunches are over allowing you to remember when scheduled times are over. 

### Additional Helper Tool Launching
On top of this application, I have built a number of other applications that help us comb through rostering data using the `OneRoster` or `SFF` form factor. 

#### Roster Helper
<img src="https://github.com/dnbroo/work_tools/raw/main/images/roster_helper.gif" width="800">     
 
We comb through a lot of data while on calls. This can lead to 10-15 minutes of awkward conversation while we attempt to dig through rostering files from large schools and see what potential issues are arrising. Using this tool, we are able to scrape data 1000x more effectively. It can search three different user critera and if it finds a match it will output their information in an easy to read structure. From there you can search a different user or pull connecting class data with the same user.   

##### &nbsp;&nbsp;Features  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Allows for **instantanious** user lookups using large data set CSV values (over 1m+ entries processed in under 1 second).  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Allows to grab any class data for a found user.    
&nbsp;&nbsp;&nbsp;&nbsp;✅ Dropped troubleshooting time down from 10-15 minutes to ~30 seconds.    
  
#### Jira Helper
Let's face it. Developers ask for a lot of information. So much in fact that I implemented this tool to be able to quickly and effeciently gather any necessary information so that we can escalate tickets to our development team for further processing. This also allows for templated submissions which makes it easier for readability and quick information gathering. Using this tool allows us to submit a Jira ticket faster than 60% using conventional methods.
##### &nbsp;&nbsp;Features  
&nbsp;&nbsp;&nbsp;&nbsp;✅ Quick and Effecient write ups for development.   
&nbsp;&nbsp;&nbsp;&nbsp;✅ Easier readability since the template will be the same 9 times out of 10.     
&nbsp;&nbsp;&nbsp;&nbsp;✅ Always on top for certain sections that requires us to click through the websites while writing up replication steps.   

  
### Plan of Action Setter with Automatic Date Configuration
This allows us to *automagically* set Plans of Action (POAs) within Salesforce. The convenient drop down boxes allows us to set how many days out we want it to be. It will automatically set the correct date in business days and account for weekends. 
> &nbsp;&nbsp;Note: Currently only weekends are supported. Holidays and scheduled times off are not accounted for.
  
  
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
| Ctrl + F21 | Sets input of external monitor to work computer |
| Ctrl + F22 | Sets input of external monitor to personal computer |
