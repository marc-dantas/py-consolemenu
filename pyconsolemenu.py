# PyConsoleMenu - Create Custom Console Menus

NUMBERED = 'numbered'
LISTED = 'listed'
NORMAL = 'normal'
CLEAN = 'clean'
DETAIL = 'detail'
LINE = '-'
THICKLINE = '▬'
DOUBLELINE = '═'


class ConsoleMenu(object):

    def __init__(self, line_width=35, center=False, menu_type=NUMBERED, subtitle_line_width=3, count_from=1) -> None:
        super().__init__()
        self.subtitle_line_width = subtitle_line_width
        self.line_width = line_width
        self.center = center
        self.type = menu_type
        self.count_from = count_from

    def new_header(self, title, subtitle=None, style=NORMAL):
        self.style = style
        if style == CLEAN:
            print()
            print(f"< {title} >".center(self.line_width))
            if subtitle != None:
                self.new_line(custom_width=self.subtitle_line_width, center=True, char_type=THICKLINE)
                print(f"{subtitle}".center(self.line_width))
                print()
            elif subtitle == None:
                print()
        
        if style == NORMAL:
            self.new_line()
            print(f"{title}".center(self.line_width))

            if subtitle != None:
                self.new_line(center=True, custom_width=self.subtitle_line_width)
                print(f"{subtitle}".center(self.line_width))

            self.new_line()

        if style == DETAIL:
            self.new_line(char_type=DOUBLELINE)
            print(f"{title}".center(self.line_width))

            if subtitle != None:
                self.new_line(center=True, custom_width=self.subtitle_line_width, char_type=DOUBLELINE)
                print(f"{subtitle}".center(self.line_width))

            self.new_line(char_type=DOUBLELINE)

    def new_line(self, custom_width=None, char_type=LINE, center=False):
        if custom_width == None:
            if center:
                print(f"{char_type * int(self.line_width)}".center(self.line_width))
            else:
                print(char_type * int(self.line_width))
        else:
            if center:
                print(f"{char_type * int(custom_width)}".center(self.line_width))
            else:
                print(char_type * int(custom_width))

    def insert_values(self, values: list):
        c = self.count_from
        for item in values:
            if self.type == NUMBERED:
                if self.center:
                    print(f"{c} - {item}".center(int(self.line_width)))
                else:
                    print(f"{c} - {item}")
                c += 1
            if self.type == LISTED:
                if self.center:
                    print(f"| {item} |".center(int(self.line_width)))
                else:
                    print(f"| {item} |")
    
    def end(self) -> None:
        if self.style == NORMAL:
            self.new_line()

        elif self.style == CLEAN:
            print('\n')

        elif self.style == DETAIL:
            self.new_line(char_type=DOUBLELINE)
