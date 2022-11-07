#!/usr/bin/env

# Generate container.xml for EPUB 3 - will be part of ebookbuild-3.3.py.

"""
<?xml version="1.0" encoding="UTF-8"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
<rootfiles>
<rootfile full-path="OPS/package.opf" media-type="application/oebps-package+xml"/>
</rootfiles>
</container>
"""

from lxml import etree
import os

rootfolder = "EPUB3-test" #Test variable which I'll connect to metadata.json in the final release.

def mimetype():
    try:
        os.path.exists(rootfolder + os.sep + "mimetype")
        
    except FileNotFoundError:
        os.chdir(rootfolder)
        with open("mimetype", "w") as mt:
            mt.write("application/epub+zip")
        print("Created the mimetype file.")
        
    except FileExistsError:
        print("Mimetype file already exists.")

def metainffolder():
    try:
        os.path.exists(rootfolder + os.sep + "META-INF")
        
    except FileNotFoundError:
        os.mkdir(rootfolder + os.sep + "META-INF")
        
    except FileExistsError:
        print("META-INF folder already exists.")

def containerxml():
    try:
        os.path.exists(rootfolder + os.sep + "META-INF" + os.sep + "container.xml")
        
    except FileNotFoundError:
        os.chdir(rootfolder + os.sep + "META-INF")
        root = etree.Element("container")
        root.set("xmlns", "urn:oasis:names:tc:opendocument:xmlns:container")
        root.set("version", "1.0")

        rootfiles = etree.SubElement(root, "rootfiles")

        rootfile = etree.SubElement(rootfiles, "rootfile")
        rootfile.set("full-path", "OPS/package.opf")
        rootfile.set("media-type", "application/oebps-package+xml")

        etree.ElementTree(root).write("container.xml", encoding="utf-8", xml_declaration=True, pretty_print=True)
        print("The META-INF/container.xml has been created.")
        
    except FileExistsError:
        print("META-INF folder already exists.")

mimetype()
metainffolder()
containerxml()