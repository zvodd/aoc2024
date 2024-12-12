
bigbuf = ""
with open("d3.input") as infile:
    bigbuf = infile.read()


class Matcher:
    def _init_(match_list, place=0):
        self.place = place
        self.match_list = self._parse_mlist(match_list)

    def peek_check(self, char, place):
        mt, mv = match_list[place]
        if mt == "str":
            if mv == char:
                return True
        if mt == "list":
            if mv in mt:
                return True
        return False

    def next_check(self, char):
        rv = self.peek_check(char, place)
        place += 1
        return rv


def parse_data(data):
    eof = len(data)
    do_state = True
    current_token = ''
    mul_args = []

    m_map = {"do":Matcher("do()".split('')), "dont":Matcher("don't()".split('')), "mul":Matcher("mul(")}
    matchers = {"do":m_map['do'], "dont":m_map['dont'], "mul":m_map['mul']}
    while i < eof:
        char = data[i]

        valid_matchers = {}
        if state == "initial":
            valid_matchers = matchers
        elif state == "`":


        [m.next_check(char) for m in matchers]


parse_data(bigbuf)