from model.project.project import Project, ProjectUid

from abc import ABC, abstractmethod

class ProjectRepository(ABC):
    @abstractmethod
    def ReadProjectUids() -> list[ProjectUid]:
        pass

    @abstractmethod
    def ReadProjectByUid(uid: ProjectUid) -> Project | None:
        pass

    @abstractmethod
    def ReadProjectNameByUid(uid: ProjectUid) -> str | None:
        pass

    @abstractmethod
    def ReadProjectDescriptionByUid(uid: ProjectUid) -> str | None:
        pass

    