class agent:
    def __init__(self, data: dict) -> None:
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])
        xyz = str(data['pos']).split(',')
        self.pos = []
        for n in xyz:
            self.pos.append(float(n))

        self.stations = []


class pokemon:
    def __init__(self, data: dict) -> None:
        self.value = data['value']
        self.type = int(data['type'])
        xyz = str(data['pos']).split(',')
        self.pos = []
        for n in xyz:
            print(n)
            self.pos.append(float(n))