import re
import sys
import json
from pathlib import Path

DIRECTIVE_RE = re.compile(
    r'/\*\*\s*(include|variable|loopover|endloop|loopvar)'
    r'\s*([^ *]*)\s*\*\*/')


class TemplateEngine:
    def __init__(self, in_filename, out_filename, context_filename):
        self.template = open(in_filename).read()
        self.working_dir = Path.in_filename.absolute().parent
        self.pos = 0
        self.out_filename = open(out_filename, 'w')
        with open(context_filename) as cf:
            self.context = json.load(context_filename)

    def process(self):
        match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        while match:
            self.out_filename.write(self.template[self.pos:match.start()])
            directive, argument = match.groups()
            method_name = 'process_{}'.format(directive)
            getattr(self, method_name)(match, argument)
            match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        self.out_filename.write(self.template[self.pos:])

    def process_include(self, match, argument):
        with (self.working_dir / argument).open() as include_file:
            self.out_filename.write(include_file.read())
            self.pos = match.end()

    def process_variable(self, match, argument):
        self.out_filename.write(self.context.get(argument, ''))
        self.post = match.end()

    def process_loopover(self, match, argument):
        self.loop_index= 0
        self.loop_list = self.context.get(argument, [])
        self.pos = self.loop_pos = match.end()

    def process_loopvar(self, match, argument):
        self.out_filename.write(self.loop_list[self.loop_index])
        self.pos = match.end()

    def process_endloop(self, match, argument):
        self.loop_index += 1
        if self.loop_index >= len(self.loop_list):
            self.pos = match.end()
            del self.loop_index
            del self.loop_list
            del self.loop_pos
        else:
            self.pos = self.loop_pos


if __name__ == '__main__':
    in_filename, out_filename, context_filename = sys.argv[1:]
    engine = Template(in_filename, out_filename, context_filename)
    engine.process()
