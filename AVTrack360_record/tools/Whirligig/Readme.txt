--------------------Whirligig release notes (These release notes refer to the full version and might not always apply to the free version)---------------------------------------
3.92 Default build update
Whirligig has been updated to 3.92 and includes several updates. The highlights are listed below.

- Optimised code for better performance.

- Updated Unity3D and all plugins.

- You can now choose you're own    backgrounds.

- Moved Streaming and youtube playback to its own menu.

- Improved the Desktop mirroring options.

- Added Oculus touch support.

- Improved the current rooms.

- Lots of bug fixes.

I’ve worked hard to make this update the most stable version of Whirligig so far. However if you have issues or any questions please contact me either through the Steam discussions page or whirligig.xyz

I hope you enjoy Whirligig and continue to find it a worthwhile player.


3.92
-Optimisation.
-Fixed SaveLoad auto selecting.
-Fixed issue when there are a large number of drive on a system so you can easily scroll down the list.
-Fixed some commandline stuff.

3.91
-Made it select VLC video lan if media foundation is selected and Windows 7 is being used.
-Set Media foundation to be the default option for playback.
-Made it select VLC video lan if media foundation is selected and Windows 7 is being used.
-Set Media foundation to be the default option for playback.
-Rebuilt some of the menus so that they all better and don't contain confusing icons such as glueUI and mirror.
-Worked on the Touch detection and fixed some little issues relating to it.
-Rebuilt the Menu to be more compatible for touch.
-Fixed issue with Media foundation not jumping to the location that is in the save.
-Fixed the loading of the correct Gamma for videos that haven't be seen yet.

3.9
Last update before Christmas.

Unity3D updated to 5.50f3.

Video plugins updated.

Video path menu update. The Streaming has been removed from the Video Path menu and the options rearranged with descriptions of each of the Video paths when hovered over.

Steaming - Youtube menu added. Currently accessible through the buttons menu and the gamepad mapping. This gives this feature a better location and will make adding features easier in the future.

Easy creation presets added to Desktop mirroring menu.

I hope you like this update and if you have any problems let me know.


3.8971
An update to the Unity build and the AVpro plugin.

3.897
Hi

This is an early release of the latest version of Whirligig. I wanted to release this now as I think I've got the Touch controls working to at least a usable stage and I want to provide this to you knowing that I won't be able to release another version for at least another week. During that week I'll be working hard on making the Touch controls more usable and fully testing it for a default release.

It also includes some bug fixes, plugin updates and room updates.

This version hasn't gone through the testing process I usually do and with adding a new controller system it might add more bugs that remove them. I hope not. If you do find issues let me know and I'll do my best to fix from for the next release. One issue I'm aware of is that when you reset the controllers they will appear briefly. This will be fixed in the next update.

Bug fixes

Fixed films always starting at 00:01.

The progress disappears straight away when playing films.

Fixed issue with reducing the the radius to below 3. This was introduced in the last beta when fixing the low fps in the menu.

The latest Oculus SDK disables the gamepad inputs when not using the Oculus. This has caused any use of the controllers with other headsets to not work. I've built in a new gamepad system which hopefully will replace this. The only difference will be that when the game window is not in focus the gamepads won't work. This is standard for the majoity of Unity apps.

Rooms

I've replaced the bedroom and living room with better placement and better maps.

Touch Control support
The touch controls react to movement of the controls. If the controls aren't moving for a few seconds it will default back to the head control system. The laser pointer will also link to which ever controller is moving first so you can just use one controller if you want to. The trigger button is select and the side trigger is switch controllers.

Models/textures by Carbon Games http://carbongames.com


Updating to the Beta

If you haven't used betas before they are pretty easy to do. To change to a beta right click on Whirligig in Steam, click on propities, select the beta tab and select the latet beta from the dropdown menu. The player will then update to the latest beta.

If you find that this breaks Whirligig for you you can reset Whirligig back to it's default settings. To do this follows the instructions in here.
http://steamcommunity.com/app/451650/discussions/0/154642901285181817/


I hope you like this version of Whirligig and think want to support it please leave some nice reviews. If you have problems or any suggestion let me know and I'll do my best to add and fix them :)

Now go and enjoy Whirligig

Over and out

Phil


3.895
Optimisation of code increasing the framerate in the menu.
You can now add your own backgrounds in the background menu.

3.89
Fixed Progress not working over OuterGlow.
Added the Cinema master.


3.882
Fixed Volume increase not working.
Fixed rotation of background lock only working 180 degrees.
Added rtsp support for VLC.
Fixed the Laser jumping Vive controllers when grips are activated.

3.881
This is a small update to fix a bug with the background in front problem. I've found the issue and fixed it and also made it so if the background is a jpg it doesn't allow for being in front as that serves no perpose.

I've also enabled the ability to play back rtsp files.

I've also update the Unity3d Build 5.4.2f2. This could have a big impact and needs testing properly so I'm only realising this as a beta at the moment.


3.88
This update includes quite a few bug fixes that are too many to mention. Hopefully I haven’t added more. Also some improvements. Here is a list of the most noticeable ones.

Reprogrammed the position reset for the Vive which hopefully should fix issues with still seeing the grid when in seating mode.

Custom format now works properly with the VLC VideoLan video path.

Backgrounds now has the option to lock the background to the tilt and have the background in front of the video which is useful for with pngs with Alphas.

Added png with alphas support for backgrounds.

Added custom forward and backward skipping (mappable to Gamepad and changeable in options)

Added time to Vive controls.

Added a new very simple menu.

Feedback and suggestions are always welcome on the Steam discussions forum.



3.872
Bug fixes mostly. I'm going to say bug fixes but I have no idea what ones, I'm just working through them.

3.871
Removed the Mouse is defocused message. It seems to be working  as it should now so I'm removing it for now in a hope I won't have to add it back in again.
Fixed Menu switch changing the menu select option.

3.87
Updated AVpro. 
AVpro is the video plugin that I use to play back Directshow. The two main parts of this update has allowed me to add changing audio tracks to the Directshow and Media Foundation and also the plugin now has GPU set to default for Media Foundation. For this reason I've decided to give the Media Foundation side of the plugin a go as well relacing the currently Media Foundation plugin. So what does this mean. See the list of updates below.

Audio track selection on all Video paths.

Media Foundation plugin changed over to the AVpro plugin hopefully improving performance and in turn fixed some glitchy issues with the previous Media Foundation implementation.

Oculus SDK updated to 1.8

Menu system improvements. This includes an overhaul of the way the menu images are loaded in, where the settings for the menus options locations are set and adds the ability to have different positions for menu items for each playback type and different MenuOBJ.obj objects for each menu option. This makes skinning the player much more flexible. The publisher has been updated to reflect this also.

Fixed bug from previous beta which causes the gamepad and other controls to not work in some of the menus.


3.86

Audio track selection.
I've started to add support for  videos with multiple audio tracks. I say started as the only plugin that fully supports this is the VLC one so I've added the support there and got the hooks into the other plugins for when they add them which should be soon. If you want to change the audio track open the settings and you'll now see a button next to the volume, select that to cycle through them. This option is also mappable to the xbox one controller. This is as an early stage and only works with the VLC video path but hopefully should be a good start to implementation across the board.

Explorer updates
-When you hovering over files and folder the full name is displayed at the bottom. This helps with files and folders with long names.
-Added the ability to sort the list of files by date or by alphabetically. Also you can now reverse the order.

Youtube and support for Streaming
The VLC plugin side of the player has had a rudimentary youtube playback system. I've worked on improving this and also added the ability to playback http video locations. The location of this is currently in the Video paths part of settings. I will probably move this as it doesn't make a great deal of sense that it is here.

The way this works is that a file is created on your system within the last explorer location with the extension .stm. This is a basic text file and contains the streaming location or Youtube code (the last bit of the youtube link which looks a bit like this o5KQL_50ZHk). This then acts like a video file so can be moved using your windows explorer and shared with others if you want. As the player sort of sees it like a video file all its settings are saved in the same way.

Backgrounds
Backbrounds have been updated to allow more backgrounds without more code. What this means is that it's one more step on the road to allow you to easily load your own backgrounds. You can do this manually if you want. I won't give a full explaination here but just go into here:
C:\Program Files (x86)\Steam\SteamApps\common\Whirligig\production\Backgrounds
or where ever you Whirligig files are installed and have a look. Currently there are slots for 36 backgrounds if ou want to add your own.

Bug fixes and changes.
As always I've fixed some bugs made some changes and probably added some more bugs. Let me know what you think, if you come across any issues and if you have any ideas. I'll continue to work my way through my list of updates and I won't stop until 

3.853
Added Ability to change Audio track with VLC video path. This is currently avaiable to map to Gamepad buttons or in the Settings menu.
Explorer update which shows the full name of files and folders when hovered over.
Fixed issue with none Oculus or Vive HMD's not working properly, hopefully.
added hevc file type to exceptable list.


3.852
Fixed issue with Rooms not working with DirectShow and Media foundation.
Fixed issue with changing the Stereo options in the Adujustment menu.
Fixed issue with hidden menu.


3.85
Added option to turn off mouse control which unlocks the cursor.
Added new menu for backgrounds. This is the first addition that will be developed into allowing you to save and load your own.
Changed the way the drives are detected in the explorer hopefully fixing issues with drives not showing up.
Change the way that loop works for files with an in out range.
Change f2 shortcut so it doesn't hide and reveal the menu as this is an option in the settings menu. Now it reveals the settings menu.
Updated AVpro plugin, Unity plugin ns UMP plugin.
Added Menu menu. You can now change the menus to different ones. Currently there are three available. More will come in time.
Fixed some bugs relating to the use of the publisher with the Whirligig.
Added a Saturation, Brightness, Contrast and Gamma settings options.
Subtitles now work in rooms and Curved Cinema.


3.83
Subtitle bug fix.
Publisher use bug fixes.
Timed crosshair for published hotspots added.

3.82
This is quite a big update and hopefully should make things much easier for everyone in the future. You may also notice I've jumped a few points in the versioning. This is to jump over the Media foundation/Directshow versions which are now supported property and more permanently in this version. The biggest addition to this update it that I've fully integrated the Media foundation and VLC plugins into the player. This means that if you want you no longer need to have the LAV codecs installed. This also has the addition of being able to use the VLCVideoLan plugin to play back youtube videos. On top of that there is now a new Directshow plugin installed. This plugin should be quicker and will also mean better support in the future. I've also noticed that with this plugin update gpu decoding seems to now work. To do this open up LAV video, in the decoding options change it to NVIDIA CUVID (I've only tested it with Nvidia video cards). There are several other updates as well. I'll list them as best I can below.

Video plugin path opened to include Directshow, Media foundation and VLCVideoLan.

Text in main menu replace to utilise the Unity UI system. This hopefully should now mean better support for non English characters. I would like to test this properly so anyone out there with examples please let me know.

Network operation of the player. You can now operate the player using network commands. This is usefully if your demonstrating VR video at a conference.

Fisheye has been rotated 90 degrees by default. The tilt will be the same so still set to 0 but the Fisheye is rotated directly in front of you. This was requested and looking at the majority of content out there seems the more common option. To get back to before simply tilt the dome back 90 degrees.

Single pass rendering is enabled. hopefully this will help improve performance.

Settings menu added to the Vive controller underside.


3.75
This is a mid update and has been released to test bases elements with specific users. The new intergartion of the plugins needs far more testing including testing on the other updates.

New AVpro plugin updated. For directshow.
New MPMP plugin updated. For media foundation.
New UMP plugin updated. For VLC VideoLan.

New setings file of universal options.

New network controls for controlling the player over a network. (needs better intergration.)

New mirror option that allows for a different FOV. (needs better intergration.)

3.74
There are quite a few new things in here so I'll devide them up and explain each one.

Subtitle support
You can now have subtitles with your films. If you have a film and want to have subtitles then simply acompany the film with an srt file so for example. Alice in Wonderland.mp4 and the subtitle file Alice in Wonderland.srt

The subtitles will play automatically but you can turn them off with a xbox mapped button or by using the new menus.

------------------------------
New Menu
I've been adding loads of features over the development of the player but a lot of the features have been somewhat hidden. I've now created a new settings menu that has all these features making it easy to access them and easy for me to add more to them. So firstly to access this menu use the cog icon on the main display. Each menu explained.

General
Background glow. Turn off and on the background glow for cinema films.
Loop. Turn loop on and off.
Swap Eyes. The standard for stereo is left right but this allows you to swap those eyes.
Mirror display. Mirror the display to the monitor off and on.
Glue UI. Glue the UI to the hmd.
Subtitles. If there are subtitles turn them off and on.
Volume. Turn volume up and down.
Stereo Separation. Increase or decrease stereo seperation of a 3D film.
SuperSamping. Increase or decrease SuperSamping.

Position
This menu allows you to move the camera position around. Currently simple Backward, Forward, Up, Down, Left, Right.

Adjust
Here you can access all the controls you need to adjust the projection and playback of the video. So a quick list:
Stereo options. Mono, Over Under, Side by Side.
Projection Type. Fisheye, Barrel, Cinema, Curved, Custom, Rooms.
Tilt.
FOV.
Radius.
Rotation.

Misc
Here you can change the video plugin to VLC or DirectShow and also load a youtube link. This is quite early stages so it might crash when using the VLC plugin. The player always starts in DirectShow mode as that is very stable.
------------------------------

The explorer has also had an update and can now be operated with the arrow keys, dpad, vive touch and the Oculus remote control. Bassically as soon as you use these the standard crosshair will be taken over and you will be able to navigate up and down the lists with those keys removing the need to look at the files you want. It wasn't a straightforward introduction and if there are any issues let me know. 

A big but small change is that the play pause button now plays and pauses. What this means is that the video will now play with the menus up and you can use all the menus as the video plays. I will be adding an option to go back to the old way but this seemed to be an obvious and useful change espically with the new menus. Let me know what you think of this change.

Other updates include bug fixes to the Vive controller and probably other stuff but I can't fully remember. If I think of anything I'll add it again here.

So let me know what you think of all the updates. I'm going to continue to add things. This is currently only been released as a beta as I want to to some proper bug checking before updating the main build. If you find any bugs let me know.

Thanks for using Whirligig and I hope you continue to enjoy it.

All the best

Phil



3.73
MPMP Plugin added. This is a very large update as this brings VLC support which also brings a load of possibilities for the future. These include better native codec support, faster playback of videos and youtube playback.

A Settings menu has been added. This is a new area to encompass the settings I've left off the main display. So although these settings were already available in other ways they now have a place to change them in their own menu. So in the settings menu which is the icon that looks like a cog on the main UI you will find a slider to adjust the stereo separation, a slider to adjust the SuperSampling, a toggle to switch between the new VLC support and the Directshow support (also available as a mappable xbox button), a text field where you can put in a Youtube code and a button to load it.

VLC Support in detail
The VLC support option allows you to change the player to use the VLC library over the previous directshow plugin. This mean that there are a whole load more codecs available without having to install the DirectShow codecs. On top of that you may well find better playback with the VLC option. I hope to make this the default and the directshow to be the other option but currently the VLC support misses a couple of important features. The first is the fact it doesn't know that a file has failed to load so if it doesn't work it won't tell you, the second is that some files when you try to load them crash the player (the player always starts using DirectShow unless you are using the Youtube feature described below), the third is that some videos look garbled when they shouldn't and the forth is that it doesn't load properly and requires you to play the video before you can scrub and skip to different parts of the video. These are being worked on and I hope to have fixes for them soon. I thought though that the benifits outwayed the negitives to not release it in beta form.

Youtube support
So I've added Youtube support as the VLC plugin (MPMP Unity plugin) brings that to the table and so I've put it in. It's in its infancy but can be used. To use it do one of two things. Open the settings menu, paste the Youtube URL code into the youtube box and hit load. Currently this loads the video into the player where the previous video is so any changes you make will be saved into the previous videos settings and when you load the youtube video the only thing that will change is the start and end time and when playing you will see the youtube video. The second and preferred way is to create an empty file (a text file is fine) with the Youtube code followed by a .you as the name so for example the file name for https://www.youtube.com/watch?v=o5KQL_50ZHk would be:

o5KQL_50ZHk.you

This then can be stored wherever you like and will load the video that the code is for. To get the code it's just the last bit of a youtube video.

By creating a file it means that you can change and save the settings of it like  any other video.

This is early days for this feature and the VLC MPMP plugin and I've got a lot to work on making it stable and easy to use but I thought I would give it out to you so you can have a look and see what you think.

I hope you like it.

Know bugs.
when loading the Youtube video the aspect ratio doesn't get set right. To get it to work again just try changing the stretch and it should re adjust it.
Some video files when using VLC crash the player. The player always start in Directshow support so restart should bring Whirligig back to life.
To scrub a video when using VLC play it first. You will then be able to scrub it like any other video.
Some videos display incorrectly using VLC and look completely garbled.

3.72
Updated to UNITY 5.4.0F1
Remote press button holds now so that you can easily scroll up and down.
Next Media and Previous Media added to the options for the xbox controller.
Add .ts and .tp now support.
Glue to HMD now glues the Explorer and over menus to it as well.
Fixed small scale not setting the menu distance properly.
The cursor is now hidden when the menu is hidden.
Fixed issue with the menus not changing when loading presets.
Added 10 more Save slots.
Fixed crosshair while save slots are present so it is over the slots and not on a separate plane.
If a film is no longer found then the save slot will disappear.
Added clear to save slots so you can tidy up those slots.
Changed the buttons of and the way they work on presets so they look nicer.
Added name on presets so you know which one you're loading,clearing,saving.
Added clear to presets.
Added video outer glow option for Cinema and Cinema Curved. This is accessible by the keyboard 'z' and is mappable to the xbox controller.
Fixed the over menu option. The old menu didn't work when going to it as it was setup wrong.



3.711
A very quick update that fixes the issue with presets and saves not working when Whirligig is outside of program files, again.

3.71
A very quick update that fixes the issue with presets and saves not working when Whirligig is outside of program files.

3.7
Added warning when trying to use the Mouse on Oculus Rift.
Updated some UI elements.
Added an ability to change the supersampling using the '[' and ']'. This is a new feature and is put in to give an idea of how to properly integrated it in the future. If it a go and see what it feels like. It will reset back to 0 when the player restarts. Expect this to be better integrated in future versions.
Rooms menu now added. When you select rooms you will now have the button option instead of the left right options.
Continued improvements to the look of the UI buttons, wider for left and right play back forward buttons improved etc.

3.69
UI update.
Added a new room, bedroom.
Rebuilding of the UI system to make it more straight forward to update and change.

To be honest there are load of updates here relating to the UI. I've been working on a new UI and hopefully this is a marked improvement on the previous version. Because this is a big change I've gone through and redesigned the whole way the UI works so that it now loads each of the UI systems for the Cinema, Barrel, Custom format and Rooms from different locations allow each one to have different designs. This is the beginning of improving the whole UI loading system. I've also removed a hacked element of code that loaded in a black frame between each still as it would cause an access violation error if I didn't have it in. So generally a big change and hopefully will allow me to make more improvements for the future.



3.65
Presets added. I've added this as both a button on the UI and a shortcut. You can now save up to 6 presets and load them whenever you want.
Updated to Unity 5.4.0b21.
Added a more robust reset if needed. If you pres control,alt,f9 you can now reset the player back to its original installed settings.
Updated the Room aspect ratio to actually work now. Before it would only be set to the size of the screen but now it will set the Aspect Ratio to the size of the screen. Also as a result you can now use the stretch option to resize the screen if needed.
Fixed a couple of bugs relating to the browser loading or not loading the first time you click.

3.61
Remote Update.

3.6
-Replaced the Input system with the Oculus input system. With any luck this will allow the Oculus remote to be used and fix issues with scrolling menus. The input system also works the same on Both 360 and xbox one controllers so no longer a need to have an option of them both. So I've removed the ability to choose a controller in the edit gamepad.
-With the update to the input controls I've been able to add the trigger buttons as more options on in the Gamepad Options.
-Whirligig now remembers the stereo option when skipping between different formats.
-UI updates. I've worked on a way to have multiple UI's. What this means at the moment is the 'h' on the keyboard (also a gamepad option) will change the UI to a different colour. I know this doesn't sound that good at the moment but it's actually completely changing the whole UI so in theory there could be several ui's, simple ones, all options etc. Also these are skinable so people can make their own if they feel inclined.
-Updated the hotspot options (for people using the publisher) so that the first hotspot can be the whole screen.


3.53
Add selection menu for Custom formats.
Add selection Menu for Formats.
Fixed bugs for publisher.
Included Oculus SDK back in.
Included VRidge support. Now VRidge is detected as an Oculus and allows for reseting the viewport.
Removed auto detect for position at start. It's in frount so should just be that unless you want to reset it to point another way.
Reduced the size of the textures for smoother loading. Most textures are loaded in from external png's for skinning ability.
Add a new custom format Samsung Gear 360. Thanks again to Andrew Hazelden  http://www.andrewhazelden.com/blog/ for making it.

3.52
Updated to Unity 5.4.0b19.
Oculus is now using OpenVR and because of this I've had to rewrite the reset position.
Vive Room set to seated. I think this will help with removing the chaperone. It does on mine at least :)

3.51
Updated to Unity 5.4.0b18.
Fixed missing Vive Panels.
Changed Oculus SDK to openVR as the cursor Locking is broken. This is actually quite a big change and might be bad news for some. I will continue to test the beta relating to this.
optimsed Gamepad save.


3.5

I might of jumped up a version a bit quick here but I'm sure I'll work it out as I go along. So what updates are there in this weekly update bonanza.

-A new custom format has been added to the custom format list. LG360 support. Many thanks to Andrew Hazelden  http://www.andrewhazelden.com/blog/ for making it. Check out his great tools for VR 360 production.

-An ability to change video seperation. Keyboard commands are 'v' and 'b'. You can also add the shortcut to the gamepad. I have to admit the keyboard is getting pretty cluttered. I am looking at adding a keyboard options window also.

-Vive controller now works with just one controller.

-Vive controller is default right handed. If you want left handed turn off the laser controller which will switch the Vive laser to the left hand and then back on again.

-Sleep Vive controller. Pressing the grip will turn off the Vive controller panels and laser, pressing again will turn them back on again.

-Desktop (No VR) mode works with the Mouse. There is still an issue with the save slots which can only be accessed with the menu off. Hopefully fixed in next version.

-Explorer look has been change to have white text and dark background. Hopefully this is considered an improvement. I felt that the bright drop downs where a bit jarring. I also wanted to make it feel more part of the player.

-Gamepad look also changed to feel like the Explorer.

-Scrollbars in both the gamepad and explorer have been worked on so that they are easier to grabish. The colliders were incorrectly generating so that they weren't in the right place. Hopefully this will make it feel more stable.

-Hide and show menu now assignable to a gamepad control.

-Added play, rewind and forward to the menu. Although yo can easily play a video by hitting outside of the menu area this might help people new to the player to understand the controllers.

-When changing an option in the menu with the crosshair that menu option gets selected. This is useful for a couple of reason one being that you can then use the left and right keys, d-pad to change the option. It also allows you to use the keyboard to type the number in you want to set it two.

-f9 Doesn't reset to the original menu any more but resets the options for the video you are currently watching. The default settings are Cinema, Tilt 0, Rotate 0, Scale 0, Distance 0, Stretch 0. I will be looking at building a more robust reset for really big errors but at the moment this should help just to reset the video to something you can see.

-Scaling/Radius really small no longer pushes the menu outside the sphere. It makes the Menu smaller which makes it a bit harder to use but you should still be able to see it.


OK I think that's it for this weekly update. I've added a few larger updates and smaller ones and I've tested the update a bit to make sure it works. However if you found yourself having problems you can revert back to the previous version in the beta drop down in Whirligig properties.

If you like the updates and find Whirligig useful please give good reviews. If you aren't happy and want things to work differently let me know in the discussion groups so I can work out how to make it better. The stereo separation, Vive control support updates and a few other bug fixes all came from there :)

Again happy Whirligiging. I hope you continue to enjoy using the player and I hope to continue to improve it.

All the best

Phil






3.4
A big UI update.

-Unity3d Updated to 5.4.0b17
-SteamVR plugin updated to 1.1.0
-Brand new explorer replacing the old one completely.
-In HMD Gamepad Options.
-Bug fixes to confused ini files.
-Gamepad update to help with problem not detecting gamepad. The default gamepad is now Xbox one without Auto Detect. I removed this as it was causing problems. Hopefully this should help alleviate gamepad d-pad problems.
-Mouse support. The UI system now has mouse support. This means that all the options on the UI are now selectable with the mouse. This should hopefully really improve the usabilty of Whirligig. This does pose one big problem which is that I have lock the mouse in the view otherwise you end up clicking outside of the view. This may be a problem for some who are used to being able to select outside of the program. I am going to see what the feedback is and see what to do from there.
-Added Icons to the menu to allow people without the Vive controller to be able to select those options.
-Added Gamepad Edit as a new icon.
-Updated documentation to reflect changes.
-Updated the start screen with changes.
-Aspect ratios for 3D over under films should be auto detected properly now.
-Curved and flatscreen aspect ratio script has been re written and the models for these have been replaced. This means that they will appear bigger but that the size represents the height in meters of the screen. This will benefit updates in the future.
-A new custom format has been added 'Facebook Pyramid'. Thank you Andrew Hazelden http://www.andrewhazelden.com/blog/ :).
-The trailer has been updated.

Known Bugs
-Gamepad and Explorer are going to be a bit wierd in the desktop mode as the mouse is stil controlling the movement while trying to select options. It will be fix in the next update hopefully.
-The explorer doesn't always select the correct drive. I don't know why yet. You can simple click a different drive and back again.
-Dropdowns in the Gamepad options will select the option if clicked to the left of the dropdown to close.
-If the wrong gamepad is selected the d-pad will access will be mixed around. Xbox one and 360 have different mapping so need to be selected correctly to get the dpad working properly.

3.24
Fixed Zoom and Volume cross over issue.
Updated Help screen.


3.231
Fixed issue with menus failing to load.
Added zoom in and out with Gamepad keys or 'q' zoom in 'a' zoom out.
Fixed white screen if media fails to load.
Added screen that when video fails to load there is information that might help to fix it.
changed the ini system so that the extension is help in the file name. This means you can have different settings for an image and a video of the same name.
Fixed issue with the location being taken from the ini file rather than the file that is being loaded.
updated the back and forward buttons to improve user experience.
Added a way to reset to the original screen 'f9'. In the case when the player breaks or get confused or simple that you want to return to the original screen 'f9' will reset to the screen.

3.22
Gamepad option now has a way to select 360,one,other or none. For people having trouble with the gamepad setup.
If a video fails there is now an error message that appears as well as saying fail.
Restricted access to folders without permission. An error message appears saying you don't have permission.
Fixed a error in the command line setup.


3.21
Updated Unity to Unity 5.4.0b13 (64-bit).
If Whirligig is installed into a steam folder outside of the program folder still save the presets for the video ini's in the Roaming folder. This will mean your settings will not be removed each time you update.

3.2
Updated Rooms.
Fix to menu not remembering custom formats.
Preparation for SteamVR release.



3.21
Updated Unity OVR thing to 1.3. I don't know what it does but maybe it will fix the sound not coming through the headphones of the oculus now.
Editing the ini importer so that you can have an ini with only the changes you wish to make accompanying the video file.

3.2
This is going to be a difficult one to list as a lot has happened. I've basically going to do it from memory and will most likely miss stuff out.

Active in this build
---------------------
Oculus Runtime 1.3 support added.
SteamVR and Oculus now in the same build.
Unity 5.4.0b10 updated.
Menu redesign.
Dome changed to Fisheye
Fisheye OU added.
OU, SBS removed from menu.
Stereo options added so you can select the ou and sbs options.
Fixes to the Custom format.
Explorer now transparent.
Xbox controller fixed. Hopefully.
Moved the menu slightly back to improve VR viewing.
Moved it forward in desktop mode for the same reason.


Things getting ready for SteamVR Release (These are changes that don't effect this build but are in them).
------------------------------------------------------------------------------------------------------------
Vive controller support added.
Menu options appear on one of the Vive controllers and selecting with the other controller.
If vive controllers aren't there attach the cursor to the head.
select options in the menu with the cursor.
Change the position of the video on the progress bar with the cursor.


That's I think mostly it. It is a big update so if there are bugs let me know. There will be more releases of the free version but they won't include some of the features of the free version. The SteamVR version will be about 4 euros I think.

3.1
The Whirligig format has been born .wlg Why I hear you cry, Why WHY WHY!!!!! Well I wanted it and the use may well help development in the future. The first thing that the wlg format allows is to reference another video file and give it different settings but be in it's own thing. I've added the ability to set a frame ranges for a video. What this means is that you can have several referenced wlg files that look at the same video and have different frame ranges. This can help if you want to say, make a game. The second thing which I haven't added yet is the ability to have files  which give different properties to Whirligig. I intend in the near future to add a Webcam.wlg and Spout.wlg option which will stream webcam and spout stuff to the player. Adding a file type will setes me quite a way down that road.

Fixed hotspot sbs and mono not loading correctly.

Updated the Video plugin to the latest build.

Updated Unity version.

***Steam Support***
SteamVR support has been added. Well sort off. I now have a different version that can be downloaded that runs on SteamVR. I really hope to combine the two so that I don't have to keep releasing two versions. If anyone knows how let me know :)

3.01
Not much has happened. Well I'e fixed a few things and updated the Unity Version. Hopefully less bugs :)

3.0
A lot has happened. 

Gamepad Integration now within the same app. The quit button now brings up the gampad options.
Gamepad detection of xbox 360 and xbox one. This could well fix the problems of having the menus constantly scroll left. Let me know if it does.
Andrew Hazelden provided me with another great obj for the Ricoh Theta S camera. Thank you Andrew :)
Hotspot fixes which make them more accurate.
The secret menu now shows the hotspot locations so you can bug test them.
ROOMS!!!!!!!!!!!!!
I have a new option called rooms. This is or will be a selection of preset rooms you can watch films in. So they are restrictive in a sense, you can only have mono or over under Cinema, you can't change the size or aspect ratio in the two examples I have currently put in. The two rooms are a drive in cinema and a very basic living room. These will be improved on a lot in the near future but I just wanted to get out a proof of concept. 
Probably a Unity update. I can't remember.

2.94
Code tidy (shouldn't change anything but might add bugs, let me know if you find bugs)
TimeCodeServer Re-emerges
The TimeCodeServer was a way for the player to push out information to a network port that would allow another program to read it. This can be useful for someone who wishes to link a haptic device to the video and have it effected but curtain time point in the video. The information that is past to the port is the video name and location, the dometype of the video, the position in seconds of the video and whether the video is paused or playing. This is a the early stages and it's use will be dictated by the people using it.

How to switch it on.
To do this you will have to edit the player.ini file located in the "Whirligig\production\menu" folder and the video you wish to send the information out to the ports ini in the "Whirligig\production\menu\inis".

Within there you will find a timecodeserver option which can be set like this:
 
 timecodeserver=off (Timecodeserver is off)
 timecodeserver=on (Timecodeserver is on and set to 2000)
 timecodeserver=2200 (Timecodeserver is on and set to 2200 or whatever number you put in there.)

Once the TimeCodeServer is on you can read the output from it, an example using NetCat is below.
----------------
D:\netcat-1.11>nc localhost 2000
C "D:\Media\videos\My Holiday.mp4"
dometype = 8
S
S
S
S
----------------

As I said it's currently in developement and as I'm not using it for anything requires people who want to use it to let me know what they need to make it useful for them. So if you any suggestions or questions let me know.

2.93
The dead zone of the joystick input has been increase. This hopefully will fix the issue of some machines constantly pushing left. If you experience this still, please get in touch. I need to establish why this happens and if I need to include a different type of fix.

Custom formats added. 

----
Cube Map Horizontal Tee
Cube Map Vertical Tee
Facebook Cube Map 3x2
GardenGnome Cube Map 3x2
----
Courtesy of Andrew Hazelden http://www.andrewhazelden.com/blog/
Andrew works on a great deal of tools that aid in 360 video production from Photoshop plugins to 3dsMax and Maya shaders.

Vray Cubemap
Vray Cubemap Inverted

Custom Format bug fix.

Rotation limit to 360 rotation as this isn't needed.

2.923
Removed FOV adjustment for camera. It shouldn't of been in there and was linked to the volume control.

2.922
added a couple of extra command lines. 
-defaultsettings will reset to a standard mono flatscreen with menus etc
-mirror off/on allows you to set the mirror to off when loading the player.
-anaglyph off to turn off the anaglyth

2.921
Minor fix to the continuous play feature that will allow it to quit when it reaches the end of a film.

2.92
Updated to Unity3D 5.3.1f1
Added more command line arguments. Full command line details will appear on the website soon. For 99 percent of people this is of no concern to you.

2.91
Fixed an issue with going full screen when in Anaglyph mode.
Fixed the swap eyes option in Anaglyph mode.
Added the ability to drag and drop a video onto the exe or shotcut and have that run the video. Note this only works on the program file.shortcut, you can't drag and drop onto the video window yet.
When in non rift mode the mouse cursor disappears so you can't see it while moving the mouse around.
Added Anaglyph to Command line options. Usage Whirligig.exe -feature "c:\fred.mp4" -anaglyph GreyAnaglyph
Anaglyph Options for command line.
	GreyAnaglyph
	ColourAnaglyph
	HalfColorAnaglyph
	OptimizedAnaglyph
	TrueAnaglyph

2.9
I've added an anaglyph option for non Oculus use. To use this either start the player without the Oculus plugged in or press f10 while using the player. Once in the standard mode (non Oculus) press f7 to cycle through the 3D anaglyph options. This is the first ituration so it might have some issues. Let me know if you run into problems or if there is a feature that this doesn't have let me know.

Anaglyph Options
	GreyAnaglyph
	ColourAnaglyph
	HalfColorAnaglyph
	OptimizedAnaglyph
	TrueAnaglyph

Updated audio Oculus Audio SDK 1.0.1 for addition audio ogg files.
Unity3d version updated to 5.3.
Added Gamepad control to non Oculus looking around.
Add Over Under option to custom Format.

2.86
Updated the surround sound addition option so that you can put _C,_L,_R,_Ls,_Rs files into the folder of the same name as the media it will pick up only the ones you have placed in there.
Speaker position for Additional sound setup added to ini file.
Updated the explorer controls so that left button goes up one folder right selections option and holding down the key scrolls through the selection in the explorer.


2.85
Updated Unity Version to 5.2.3p1
Fixed jump on scroll bar when skipping forward and backward.
Fixed skipping to another video when scrolling backwards and forwards through some videos. This is a problematic issue which doesn't happen all the time so whether I have actually fixed it or not time will tell.
Fixed save dialogue and explorer dialogue being available at the same time.
Made escape and cancel cycle out of save dialogue.


2.84
Added support for Kodak PixPro SP360 in the custom formats. Fixed custom formats for Cube map vertical, cube map horizontal.

2.83
Cleaned the project and wiped the info from to rebuild all the default settings for the latest Unity. What is has done is revealed an error that was causing pinching on stills top and bottom and maybe other stuff. I've replaced all the Unity legecy textures and lighting to standard texture. Hopefully this will reduce the possibity of unknown issues and help to get things resolved if they come up.
A background texture option. I you put a Background.jpg in the menu folder it will be loaded up as a background for your player. The format for the image is Barrel OU.

2.82
Updated the load save images for standard use. The save load when clicked away with fire will disappear.

2.81
Added new options to the commandline settings and now include Octane custom format. Changed lighting from gamma to linear. This appears to produce better colour reproduction but if I've got it wrong let me know. Run in background is now on a well.


2.8
Ok so a load of stuff has gone on here. An updated version has happen which means the player is now only compatible in runtime 0.8.0. Unity version 5.2.2p3. You can download an older version from the website that should work with eariler versions of the runtime.

A save function has been added which you can use to save a bookmark to the media your looking at. When you load it will return to the media at the place you saved.

Adventure time :)
I've built in an Inventory and save system for game creation. This the first version and may or may not have bugs. There will be tutorials very soon on this, hopefully.

Fixes, probably a load of other stuff and as always I've probably added a load of bugs as well.

You can now scroll with the mouse wheel on options in the menu.

2.73
Previously you could have an ini file with the media file and when the file was loaded it would load the ini file in. That stopped working for the installed version so I have updated it so that it works for both the installed version and independent version.

2.72
Code improvement to increase loading time of images. Added Volume control, volume up and down with '-' and '='. Updated Unity to 5.2.2p1.

2.71
External sound now doesn't need the loading screen so loads a lot faster.

2.7
Updated the Unity3D build to Unity 5.2.1p2 and re-introduced the health and safty test so the player doesn't start working until it has disappeared.

2.61
tweaks made to the image playback so that you can easily jump through your images without the menu coming up each time. Also a couple of other minor bug fixes.

2.6
Added a new menu. When you press f6 you will get a full menu that allows you to access all options. This is good if your working with the publisher and want to edit options you've disabled. This option can be disabled in the disable keys and has been added to the publisher options menu.

2.531
Added agreement into the installation.
Updated LAV codec to 0.66.

2.53
Force one instance in Unity3D doesn't work so I've turned it off and you can now open sa many plays as you like.
A png load problem has reared it's ugly head again so I've reverted some code and it loads a black frame between images to prevent failed loads.
Run in background has been switched on.

2.521
Added option for goto next video in the video options (relevant if you use the publisher).
Fixed loading of 5 channel audio that is separate from the video.
Fixed 5 channel spread so you can hear the audio correctly.
5 channel audio can now accompany a video outside of the media folder.
Fixed f10 not going back to oculus.
Improved up down left right navigation.

2.52
New version of Unity3D and a new option that will allow you to have the video continue onto the next media file.

2.51
updated the NSIS installer to v3.0b2 which has basic windows 10 support.

2.5
A big update. Unity support for VR has now included per eye rendering so that I can now use all the native VR stuff for a much better and smoother experience. It appears to have improved the video playback, tracking and ability to switch backwards and forwards between rift and not rift. The screen is now resizeable and it doesn't seem to crash so much on my system. hopefully this is true on other peoples systems also.

The gamepad options has now been improved to allow changing of the settings which relate straight into the player. You can now also have multiple inputs of the same type as well. The means you can set the play/pause button to multiple buttons (up to 4).

Kown bugs.
when clicking to remove the health and safety warning the player will respond to whatever button you click.
The FOV option doesn't work in this version.
The ability to turn positional tracking off and on doesn't work either.

2.45
tests for whether the rift is on and if it isn't starts in standard mode. If the rift is unplugged it will go to standard mode.
Known bug - don't switch between fullscreen and windowed and switch back to rift, it will crash.

2.44
Time of video now changes when skipping backward and forward and stay for about 4 seconds after stopping.

2.43
Inputs edited to help with issues of scrolling input.
The movie sync and output colour reverted back again so I've refixed that.

2.42
Hotspots load fix.

2.41
Chaneged colour spacing to HD not SD also turned sync off so inprove performace and less likely to go out of sync.



