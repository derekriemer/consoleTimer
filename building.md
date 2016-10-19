# consoleKurk building instructions. #

### Translations ###

- Gettext translations must be placed into `addon\locale\<lang>/LC_MESSAGES\nvda.po`. 

### To manage documentation files for your addon: ###

- Put your documentation in "readme.md"
- Documentation files (named **readme.md**) must be placed into addon\doc\<lang>/. Scons automatically does this for english.

### To package the add-on for distribution: ###

- Open a command line, change to the folder that has the **SCONSTRUCT** file (usually the root of your add-on development folder) and run the **scons** command. The created add-on, if there were no errors, is placed in the current directory.
- You can further customize variables in the **buildVars.py** file.

Note that this template only provides a basic add-on structure and build infrastructure. You may need to adapt it for your specific needs.

If you have any issues please use the NVDA addon list mentioned above.
