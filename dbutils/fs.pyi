from typing import Dict, List, Protocol

# fsutils

class FileInfo(Protocol):
    name: str
    path: str
    
    def isDir(self) -> bool:
        ...

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

# mount

def mount(source: str,
          mount_point: str,
          encryption_type: str = "",
          owner: str = None,
          extra_configs: Dict[str, str] = None) -> None:
    ...

# TODO: is this a method or property? Docs describes it like a property on `dbutils.fs`
def mounts() -> List[str]:
    ...

# TODO: is this a method or property? Docs describes it like a property on `dbutils.fs`
def refreshMounts() -> bool:
    ...

def unmount(mountPoint: str) -> bool:
    ...

def updateMount(source: str,
                mount_point: str,
                encryption_type: str = "",
                owner: str = None,
                extra_configs: Dict[str, str] = None) -> bool:
    ...

