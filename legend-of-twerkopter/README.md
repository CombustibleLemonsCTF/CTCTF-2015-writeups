# CTCTF 2015: Legend of Twerkopter

### Problem

**Points**: 50

**Description**: 

> Take a look at Kelvin's newest app:  
> Twerkopter.xap

**Hint**: 

> What's a XAP file?

### Solution

XAP files are standalone files for distributing software on Windows Phones. However, they are essentially specialized ZIP files, much like DOCX and JAR files. All of these formats share the same magic numbers as the ZIP file format.

After extracting the contents of `Twerkopter.xap`, we looked through the plaintext files and stumbled across the flag in a comment on the last line of [`WMAppManifest.xml`](Twerkopter/WMAppManifest.xml).

**Flag**: `XAP_for_XNA`

### Other Resources

* None.
