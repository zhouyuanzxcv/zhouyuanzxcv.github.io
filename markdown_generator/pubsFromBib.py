#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

from shutil import copyfile


#todo: incorporate different collection types rather than a catch all publications, requires other changes to template

# publist = {
#     "proceeding": {
#         "file" : "conferences.bib",
#         "venuekey": "booktitle",
#         "venue-pretext": "In the proceedings of ",
#         "collection" : {"name":"publications",
#                         "permalink":"/publication/"}
#
#     },
#     "journal":{
#         "file": "journals.bib",
#         "venuekey" : "journal",
#         "venue-pretext" : "",
#         "collection" : {"name":"publications",
#                         "permalink":"/publication/"}
#     }
# }

my_publication_file = 'My publication.bib'

my_first_name = 'Yuan'
my_last_name = 'Zhou'

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&prime;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)





parser = bibtex.Parser()
bibdata = parser.parse_file(my_publication_file)

#loop through the individual references in a given bibtex file
for bib_id in bibdata.entries:
    #reset default date
    pub_year = "1900"
    pub_month = "01"
    pub_day = "01"

    b = bibdata.entries[bib_id].fields

    try:
        pub_year = f'{b["year"]}'

        if 'booktitle' in b.keys():
            pubtype = 'conference'
        elif 'journal' in b.keys():
            pubtype = 'journal'
        else:
            pubtype = 'other'

        #todo: this hack for month and day needs some cleanup
        if "month" in b.keys():
            if(len(b["month"])<3):
                pub_month = "0"+b["month"]
                pub_month = pub_month[-2:]
            elif(b["month"] not in range(12)):
                tmnth = strptime(b["month"][:3],'%b').tm_mon
                pub_month = "{:02d}".format(tmnth)
            else:
                pub_month = str(b["month"])
        if "day" in b.keys():
            pub_day = str(b["day"])


        pub_date = pub_year+"-"+pub_month+"-"+pub_day

        #strip out {} as needed (some bibtex entries that maintain formatting)

        title_for_filename = b["title"].replace("{", "").replace("}", "").replace('\\textendash ', '-').replace("\\", "")

        url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", title_for_filename.replace(" ", "-"))
        url_slug = url_slug.replace("--","-")

        md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
        html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

        #Build Citation from text
        citation = ""

        #citation authors - todo - add highlighting for primary author?
        for author in bibdata.entries[bib_id].persons["author"]:
            if author.first_names[0] == my_first_name and author.last_names[0] == my_last_name:
                author_name = '<b>' + author.first_names[0] + " " + author.last_names[0] + '</b>'
            else:
                author_name = author.first_names[0] + " " + author.last_names[0]

            citation = citation+" "+author_name+", "

        #citation title
        title_for_html = html_escape(title_for_filename)

        if "url" in b.keys():
            title_for_citation = '<a href=\"' + b['url'] + '\">' + title_for_html + '</a>'
        else:
            title_for_citation = title_for_html

        citation = citation + "\"" + title_for_citation + ".\""

        #add venue logic depending on citation type
        if pubtype == 'journal':
            venuekey = 'journal'
        elif pubtype == 'conference':
            venuekey = 'booktitle'
        venue = b[venuekey].replace('\\textendash', '-').replace("{", "").replace("}","").replace("\\","")

        citation = citation + " " + '<i>' + html_escape(venue) + '</i>'
        citation = citation + ", " + pub_year + "."


        ## YAML variables
        md = "---\ntitle: \"" + title_for_html + '"\n'

        md += """collection: """ +  'publications'

        md += """\npermalink: """ + '/publication/'  + html_filename

        note = False
        if "note" in b.keys():
            if len(str(b["note"])) > 5:
                md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                note = True

        md += "\ndate: " + str(pub_date)

        md += "\npubtype: " + pubtype

        md += "\nvenue: '" + html_escape(venue) + "'"

        if 'code' in b.keys():
            md += '\ncode: ' + b['code']

        if 'file' in b.keys():
            file_path = b['file']
            filedir, filename = os.path.split(file_path)
            new_path = os.path.join('../files/papers/', filename)
            if not os.path.isfile(new_path):
                copyfile(file_path, new_path)

            md += '\npdf: ' + new_path


        url = False
        if "url" in b.keys():
            if len(str(b["url"])) > 5:
                md += "\nurl: '" + b["url"] + "'"
                url = True

        md += "\ncitation: '" + citation + "'"

        md += "\n---"


        ## Markdown description for individual page
        if note:
            md += "\n" + html_escape(b["note"]) + "\n"

        if url:
            md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n"
        else:
            md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q=" + html.escape(title_for_filename.replace("-", "+")) + "){:target=\"_blank\"} for full citation"

        md_filename = os.path.basename(md_filename)

        with open("../_publications/" + md_filename, 'w') as f:
            f.write(md)
        print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
    # field may not exist for a reference
    except KeyError as e:
        print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
        continue
