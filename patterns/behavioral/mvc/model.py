import os.path


class NameModel:
    def __init__(self):
        self.filename = 'names.dat'

    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'

    def get_name_list(self):
        names = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as data_file:
                names = data_file.read().split('\n')
        return names

    def save_name(self, name):
        with open(self.filename, self._get_append_write()) as data_file:
            data_file.write("{}\n".format(name))
