#!/usr/bin/env

# ebookbuild-3.2.py - ebookbuild for the EPUB3 standard. Licenced under GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.en.html

from lxml import etree
from collections import OrderedDict
import os, json

with open("metadata.json") as json_file:
    data = json.load((json_file), object_pairs_hook=OrderedDict) #For some reason the order is randomised, this preserves the order.

#Test variable which I'll connect to metadata.json in the final release.
#rootfolder = "e-book"
#containerfolder = "OPS"
opfname = "content.opf"

def mimetype():
    #Creates the simple mimetype file
    if os.path.isfile("mimetype") == False:
        os.chdir(data["rootFolder"])
        with open("mimetype", "w") as mt:
            mt.write("application/epub+zip")
        print("Created the mimetype file.")

    else: 
        print("Mimetype file already exists.")

def metainf_folder():
     #Create the META-INF folder
    if os.path.isdir("META-INF") == False:
        os.mkdir("META-INF")
    else:
        print("META-INF folder already exists.")
        
def containerxml():
    # Create the EPUB3 container.xml file
    if os.path.exists("META-INF" + os.sep + "container.xml") == False:
        os.chdir("META-INF")
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

        # Register the "dc" and "xml" namespaces with a prefix and URL
        etree.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
        etree.register_namespace("xml", "http://www.w3.org/XML/1998/namespace")

        # os.chdir(data["containerFolder"])
        package = etree.Element("package")
        package.set("xmlns", "http://www.idpf.org/2007/opf")
        package.set("version", "3.0")
        package.set("{http://www.w3.org/XML/1998/namespace}lang", "en")
        package.set("unique-identifier", "book-id")
        package.set("prefix", "")

        # Create the <dc:title> element with the "dc" namespace prefix
        # title = etree.Element(etree.QName("http://purl.org/dc/elements/1.1/", "title"))

        metadata = etree.SubElement(package, "metadata")
        metadata.set("{http://www.w3.org/XML/1998/namespace}xlms", "http://purl.org/dc/elements/1.1/")

        os.chdir(data["containerFolder"])
        etree.ElementTree(package).write(data["opfName"], encoding="utf-8", xml_declaration=True, pretty_print=True)
        print("The " + data["containerFolder"] + "/" + data["opfName"] + " has been created.")

mimetype()
metainf_folder()
containerxml()
opf()
# epub()