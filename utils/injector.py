
def Repository(cls: type):
    hasOnStart = "init_repository" in cls.__dict__

    if hasOnStart:
        cls.init_repository()

    else:
        raise Exception(f"Repository must has init_repository method")

    return cls
