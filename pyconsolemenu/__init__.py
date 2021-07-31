# PyConsoleMenu - Create Custom Console Menus

NUMBERED = 'numbered'
LISTED = 'listed'


class Menu(object):

    def __init__(self, line_width=35, center=False, menu_type='numbered', subtitle_line_width=3) -> None:
        super().__init__()
        self.subtitle_line_width = subtitle_line_width
        self.line_width = line_width
        self.center = center
        self.type = menu_type

    def new_header(self, title, subtitle=''):
        self.new_line()
        print(title.center(self.line_width))
        if subtitle != '':
            print(f"{'-' * self.subtitle_line_width}".center(self.line_width))
            print(f"{subtitle}".center(self.line_width))
        self.new_line()

    def new_line(self):
        print('-' * self.line_width)

    def insert_values(self, value: list):
        c = 1
        for item in value:
            if self.type == 'numbered':
                if self.center:
                    print(f"{c} - {item}".center(int(self.line_width)))
                else:
                    print(f"{c} - {item}")
                c += 1
            if self.type == 'listed':
                if self.center:
                    print(f"| {item} |".center(int(self.line_width)))
                else:
                    print(f"| {item} |")

        self.new_line()
