# Solution: Just a Picture?

The challenge file `challenge.jpg` is a polyglot file. A ZIP archive containing the flag has been appended to the end of a standard JPG image.

---
## Tools Needed
* `binwalk`
* `unzip` (or any archive utility)

---
## Solution Steps

### 1. Initial Analysis

Viewing the `challenge.jpg` file in an image viewer shows a normal picture with no obvious signs of steganography.

### 2. File Inspection

The key is to inspect the file's structure beyond its extension.

#### Method A: Using `binwalk` (Recommended)

`binwalk` is a tool designed to find embedded files and executable code within other files. Running it on the challenge file reveals the hidden archive.

```bash
$ binwalk challenge.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30314         0x766A          Zip archive data, at least v2.0 to extract, compressed size: 104, uncompressed size: 42, name: flag.txt
