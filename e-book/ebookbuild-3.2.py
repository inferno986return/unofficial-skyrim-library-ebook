#!/usr/bin/env

# ebookbuild-3.2.py - ebookbuild for the EPUB3 standard. Licenced under GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.en.html

from lxml import etree
import os

#Test variable which I'll connect to metadata.json in the final release.
rootfolder = "e-book"
containerfolder = "OPS"
opfname = "content.opf"

def mimetype():
    #Creates the simple mimetype file
    if os.path.isfile(rootfolder + os.sep + "mimetype") == False:
        os.chdir(rootfolder)
        with open("mimetype", "w") as mt:
            mt.write("application/epub+zip")
        print("Created the mimetype file.")

    else: 
        print("Mimetype file already exists.")

def metainf_folder():
     #Create the META-INF folder
    if os.path.isdir(rootfolder + os.sep + "META-INF") == False:
        os.chdir(rootfolder)
        os.mkdir("META-INF")
    else:
        print("META-INF folder already exists.")
        
def containerxml():
    # Create the EPUB3 container.xml file
    if os.path.exists(rootfolder + os.sep + "META-INF" + os.sep + "container.xml") == False:
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

    else:
        print("META-INF folder already exists.")
              
def opf():
# Generate the EPUB3 .opf file
        os.chdir(rootfolder + os.sep + containerfolder)
        root = etree.Element("package")
        root.set("xmlns", "http://www.idpf.org/2007/opf")
        root.set("version", "3.0")
        root.set("xml:lang", "en")
        root.set("unique-identifier", "isbn")
        root.set("prefix")

        rootfiles = etree.SubElement(root, "rootfiles")

        rootfile = etree.SubElement(rootfiles, "rootfile")
        rootfile.set("full-path", "OPS/package.opf")
        rootfile.set("media-type", "application/oebps-package+xml")

        etree.ElementTree(root).write(opfname, encoding="utf-8", xml_declaration=True, pretty_print=True)
        print("The " + containerfolder + "/" + opfname + " has been created.")

mimetype()
metainf_folder()
containerxml()
opf()