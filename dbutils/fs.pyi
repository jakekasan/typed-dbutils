from typing import Dict, List, Protocol


class FileInfo(Protocol):
    path: str
    name: str
    size: int
    modificationTime: int
    
    def isDir(self) -> bool:
        ...

    def isPath(self) -> bool:
        ...

class MountInfo(Protocol):
    mountPoint: str
    source: str
    encryptionType: str

def cp(from_: str, to: str, recurse: bool = False) -> bool:
    ...

def head(file: str, max_bytes: int = 65536) -> str:
    ...

def ls(dir: str) -> List[FileInfo]:
    ...

def mkdirs(dir: str) -> bool:
    ...

def mv(from_: str, to: str, recurse: bool = False) -> bool:
    ...

def put(file: str, contest: str, overwrite: bool = False) -> bool:
    ...

def rm(dir: str, recurse: bool = False) -> bool:
    ...

def mount(source: str,
          mount_point: str,
          encryption_type: str = "",
          owner: str = None,
          extra_configs: Dict[str, str] = None) -> None:
    ...

def mounts() -> List[MountInfo]:
    ...

def refreshMounts() -> bool:
    ...

def unmount(mount_point: str) -> bool:
    ...

def updateMount(source: str,
                mount_point: str,
                encryption_type: str = "",
                owner: str = None,
                extra_configs: Dict[str, str] = None) -> bool:
    ...

