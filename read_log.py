from pathlib import Path
from valid_data import is_valid_card

class FormatError(Exception):
    pass

class Log_Data(dict):
    def get_all(self):
        res = []
        for v in self.values():
            res += v
        return res

def read_log(file_path: Path):
    with open(file_path, "r") as f:
        lines = f.read().split("\n")
    
    sectn = None
    data = Log_Data()
    for line in lines:
        try:
            if not line:
                continue

            if line[0] == "#":
                if line[1] == "=":
                    sectn = line.replace("#","").replace("=","").strip()
                    if sectn not in data:
                        data[sectn] = []
                continue

            try:
                arc1, arc2 = line.split("|")
            except ValueError:
                raise FormatError("Expected '|'")

            arc1_num, arc1_name = arc1.strip().split(" ")
            arc2_num, arc2_name = arc2.strip().split(" ")
            if not is_valid_card(int(arc1_num), arc1_name):
                raise FormatError(f"Wrong combination {arc1_num}/{arc1_name}")
            if not is_valid_card(int(arc2_num), arc2_name):
                raise FormatError(f"Wrong combination {arc2_num}/{arc2_name}")

            if sectn == None:
                raise FormatError("Card Log outside a Section")
            data[sectn].append((arc1_num, arc2_num))

        except FormatError as e:
            raise RuntimeError(f"Error parsing line {lines.index(line)} with error '{e.args[0]}'")

    return data      

if __name__ == "__main__":
    print(read_log(Path("/mnt/P/Rayax/Public/Genshin Lunar Arcana/Teather S16.log"), None))


