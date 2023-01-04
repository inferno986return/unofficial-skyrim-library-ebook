#!/usr/bin/env

# ebookbuild-3.2.py - ebookbuild for the EPUB3 standard. Licenced under GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.en.html

from lxml import etree
from collections import OrderedDict
import os, json, datetime

os.chdir("e-book")
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
    utctime = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
    # Generate the EPUB3 .opf file

    # Register the "dc" and "xml" namespaces with a prefix and URL
    etree.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    etree.register_namespace("xml", "http://www.w3.org/XML/1998/namespace")

    # Write the <package></package> tags
    package = etree.Element("package")
    package.set("xmlns", "http://www.idpf.org/2007/opf")
    package.set("version", "3.0")
    package.set("{http://www.w3.org/XML/1998/namespace}lang", "en")
    package.set("unique-identifier", "bookid")
    package.set("prefix", "")

    # Write the <metadata></metadata> tags
    metadata = etree.SubElement(package, "metadata")
    metadata.set("{http://www.w3.org/XML/1998/namespace}dc", "http://purl.org/dc/elements/1.1/")

    title = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}title")
    title.text = data["title"]

    subject = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}subject")
    subject.text = data["subject"]

    creator = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}creator")
    creator.set("id", "creator")
    creator.text = data["creator"]

    publisher = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}publisher")
    publisher.text = data["publisher"]

    identifier = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}identifier")
    identifier.set("id", "bookid")
    identifier.text = data["ISBN"]

    date = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}date")
    date.text = utctime

    language = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}language")
    language.text = data["language"]

    rights = etree.SubElement(metadata, "{http://purl.org/dc/elements/1.1/}rights")
    rights.text = data["rights"]

    manifest = etree.SubElement(package, "manifest")
    i = 0
    for root_dir, dirs, files in os.walk(data["containerFolder"] + os.sep + data["fontsFolder"]):
        i += 1
        for file in files:
        # Check if the file is a font file (ends in .otf or .ttf)
            if file.endswith(".otf") or file.endswith(".ttf"):
                font = etree.SubElement(manifest, "item")
                font.set("id", f"font{i}")
                font.set("href", data["fontsFolder"] + "/" + file)
                
                # Set the mimetype attribute of the element
                if file.endswith(".otf"):
                    font.set("media-type", "application/vnd.ms-opentype")

                elif file.endswith(".ttf"):
                    font.set("media-type", "application/x-font-truetype")

    #Write the tags to the .opf file and save it
    os.chdir(data["containerFolder"])
    etree.ElementTree(package).write(data["opfName"], encoding="utf-8", xml_declaration=True, pretty_print=True)
    print("The " + data["containerFolder"] + "/" + data["opfName"] + " has been created.")

mimetype()
metainf_folder()
containerxml()
opf()
# epub()