from .memory import SimpleMemory, SearchMemory

__all__ = [
    "SimpleMemory",
    "SearchMemory",
    "RetrievalMemory",
    "SkillsOnlyMemory",
    "SkillUpdater",
]


def __getattr__(name):
    if name == "RetrievalMemory":
        from .retrieval_memory import RetrievalMemory
        return RetrievalMemory
    if name == "SkillsOnlyMemory":
        from .skills_only_memory import SkillsOnlyMemory
        return SkillsOnlyMemory
    if name == "SkillUpdater":
        from .skill_updater import SkillUpdater
        return SkillUpdater
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
