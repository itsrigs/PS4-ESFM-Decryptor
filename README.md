# PS4-ESFM-Decryptor
`Trop.esfm` and `Tropconf.esfm` decryptor for PlayStation 4 Trophy files. 
These files can be extracted from the trophy00.TRP of a given PS4 game through tools such as [TRPviewer](https://web.archive.org/web/20220921172135/https://sites.google.com/site/theleecherman/trpviewer). 

# Syntax
Step one: 
Provide the path to the ESFM file alongside the NP communication ID.
Example format: `esfmd.py trop.esfm NPWR12302_00`

Step two (triggered after inputting step one):
Provide the 32 digit retail PS4 EID root key.

# Disclaimer
An EID root key cannot be included in this script lest this repo face potential DMCA.
You are encouraged to provide your own and reference publicly documented information regarding them.
The PS4 Developer wiki is a helpful location to learn about how EID root keys work and how to source your own.

# Potential issues
The usage of the crypto library may cause an error in importing the AES module if the user has multiple similar crytographic libraries being used by Python.
For this reason I have also omitted a requirements.txt outright, leaving it to the user's discretion.
