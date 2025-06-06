from func.update import update
from func.ResPack import ResPack
from func.gui.ansi import Strong
from os import chdir, path as os_path

RESOURCE = "resource"


def init(path: str) -> callable:
    older_vers = ["core", "1.16.5", "1.16.1", "1.14.4", "1.12.2", "1.10.2", "1.8.9"]
    vers = [
        "core",
        "1.17.1",
        "1.18.2",
        "1.19.2",
        "1.19.3",
        "1.19.4",
        "1.20.1",
        "1.20.2",
        "1.20.4",
        "1.20.6",
        "1.21.1",
        "1.21.3",
        "1.21.4",
        "1.21.5",
    ]

    ver_res_packs: list[ResPack] = []
    for ver in vers:
        if ver == "core":
            pack = ResPack(os_path.join(path, RESOURCE, "battlecats_core"), ver)
        else:
            pack = ResPack(
                os_path.join(path, RESOURCE, "battlecats_" + ver),
                ver,
                os_path.join(path, RESOURCE, "battlecats_core", "vers", ver),
            )
        ver_res_packs.append(pack)

    older_ver_res_packs: list[ResPack] = []
    for old in older_vers:
        if old == "core":
            pack = ResPack(os_path.join(path, RESOURCE, "battlecats_core"), old)
        else:
            pack = ResPack(
                os_path.join(path, RESOURCE, "battlecats_" + old),
                old,
                os_path.join(path, RESOURCE, "battlecats_core", "vers", old),
            )
        older_ver_res_packs.append(pack)

    def update_older() -> None:
        for i in range(1, len(older_ver_res_packs), 1):
            print(Strong(f"{older_ver_res_packs[i].version():-^50}"))
            update(older_ver_res_packs[i - 1], older_ver_res_packs[i])

    def update_newer() -> None:
        for i in range(1, len(ver_res_packs), 1):
            print(Strong(f"{ver_res_packs[i].version():-^50}"))
            update(ver_res_packs[i - 1], ver_res_packs[i])

    return update_older, update_newer
