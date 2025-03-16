from model.member.achievement import Achievement, AchievementUid

from abc import ABC, abstractmethod

class AchievementRepository(ABC):
    @abstractmethod
    def ReadRepositoryUids() -> list[AchievementUid]:
        pass

    @abstractmethod
    def ReadAchievementByUid(uid: AchievementUid) -> Achievement | None:
        pass

    @abstractmethod
    def ReadAchievementNameByUid(uid: AchievementUid) -> str | None:
        pass
