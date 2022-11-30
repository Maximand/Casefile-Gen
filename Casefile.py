from mdutils.mdutils import MdUtils


"""
TODO: Keep changes to file and state?
"""

class Generator:

    def __init__(self, casenumber):
        self.casenumber = casenumber

        self.title           = ""
        self.name            = ""
        self.author          = ""
        self.lead            = ""
        self.excerpt         = ""
        self.product         = ""
        self.versions        = ""
        self.recommendation  = ""
        self.workaround      = ""
        self.start           = ""
        self.summary         = ""
        self.what_you_do     = ""
        self.what_we_do      = ""
        self.more_info       = ""

        self.mdFile = MdUtils(file_name = casenumber)

    def _check_requirements(self):
        try:
            assert self.title is not None,           "[!] Please provide title."
            assert self.name is not None,            "[!] Please provide name."
            assert self.author is not None,          "[!] Please provide author."
            assert self.lead is not None,            "[!] Please provide caselead."
            assert self.excerpt is not None,         "[!] Please provide author."
            assert self.product is not None,         "[!] Please provide product."
            assert self.recommendation is not None,  "[!] Please provide recommendation."
            assert self.start is not None,           "[!] Please provide start."
            assert self.summary is not None,         "[!] Please provide a summary."
            assert self.what_you_do is not None,     "[!] Please provide some advice."
            assert self.what_we_do is not None,      "[!] Please provide what DIVD does."
        except AssertionError:
            return False
        return True

    def _confirm_file():
        return
            
    def researchers(self):
        names = input("""
            [*] Please provide the names of the researchers in 
            comma-separated fashion. \n
            > """)
        name_list = names.split(", ")
        self.mdFile.new_list(name_list)

    def cves(self):
        cves = input("""
            [*] Please provide the CVE IDs in comma-separated fashion. \n
            > """)
        cve_list = cves.split(", ")
        self.mdFile.new_list(cve_list)

    # Kan dit misschien in een list?
    def timeline(self):
        event_list = []
        while True:
            print("[*] Please provide an event or type done.")
            event_start = input("When did the event start > ")
            event_desc = input("What happened during the event > ")

            if "done" in event_start or "done" in event_desc:
                break
                
            event = """
            - start: %s
              end:
              event: %s
            """ % (event_start, event_desc)
            event_list.append(event)

        for event in event_list:
            self.mdFile.new_line(event)
        return

    def write_title(self):
        self.title = input("[*] Please provide a title > ")
    def write_author(self):
        self.author = input("[*] Please provide the author > ")
    def write_lead(self):
        self.lead = input("[*] Please provide the caselead > ")
    def write_excerpt(self):
        self.excerpt = input("[*] Please provide an excerpt > ")
    def write_product(self):
        self.product = input("[*] Please provide the product(s) > ")
    def write_versions(self):
        self.versions = input("[*] Please provide the versions > ")
    def write_recommendation(self):
        self.recommendation = input("[*] Please provide your recommendation > ")
    def write_workaround(self):
        self.workaround = input("[*] Please provide an optional workaround > ")
    def write_start(self):
        self.start = input("[*] When did the case start > ")

    # Bouw compleet bestand en check requirements
    def generate(self):
        
        self.mdFile.new_line("---")
        self.mdFile.new_line("layout: case")
        self.mdFile.new_line("title: %s" % self.write_title())
        self.mdFile.new_line("author: %s" % self.write_author())
        self.mdFile.new_line("lead: %s" % self.write_lead())
        self.mdFile.new_line("status: Open")
        self.mdFile.new_line("excerpt: %s" % self.write_excerpt())
        self.mdFile.new_line("researchers:")
        self.researchers()
        self.mdFile.new_line("cves:")
        self.cves()
        self.mdFile.new_line("product: %s" % self.write_product())
        self.mdFile.new_line("versions: %s" % self.write_versions())
        self.mdFile.new_line("recommendation: %s" % self.write_recommendation())
        self.mdFile.new_line("workaround: %s" % self.write_workaround())
        self.mdFile.new_line("start: %s" % self.write_start())
        self.mdFile.new_line("end:")
        self.mdFile.new_line("timeline:")
        self.timeline()

        # Hacky hack hack
        try:
            self.mdFile.new_header(level=0, title="Fixes IndexError")
        except:
            pass
            
        self.mdFile.new_header(level=2, title="Summary")
        self.mdFile.new_paragraph(input("[*] Please write a summary > "))

        self.mdFile.new_header(level=2, title="What you can do")
        self.mdFile.new_paragraph(input("[*] What can an affected party do > "))

        self.mdFile.new_header(level=2, title="What you can do")
        self.mdFile.new_paragraph(input("[*] What is DIVD doing > "))

        self.mdFile.new_header(level=2, title="More information")
        while True:
            link = input("[*] Please provide references (type done to write out) > ")
            if "done" in link:
                break
            
            link_title = input("[*] Link title > ")
            self.mdFile.new_line("* " + self.mdFile.new_inline_link(link=link, text=link_title)) 

        #self._check_requirements()
        #self._confirm_file()
        self.mdFile.create_md_file()
        return
