
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
        self.road = []
        self.mode = 0

    def __repr__(self) -> str:
        f'{self.value},'


class pokemon:
    def __init__(self, data: dict) -> None:
        self.value = data['value']
        self.type = int(data['type'])
        p = str(data['pos']).split(',')
        self.pos = []
        for i in p:
            self.pos.append(float(i))
        self.src = None
        self.dest = None
        self.mode = 0

    def __repr__(self) -> str:
        return f'{self.pos} ' f'{self.src} 'f'{self.dest} 'f'{self.type} 'f'{self.value}'