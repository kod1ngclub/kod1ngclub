from model.member.member import Member, MemberUid
from model.member.achievement import AchievementUid

from abc import ABC, abstractmethod

class MemberRepository(ABC):
    @abstractmethod
    def ReadMemberUids() -> list[MemberUid]:
        pass

    @abstractmethod
    def ReadMemberByUid(uid: MemberUid) -> Member | None:
        pass

    @abstractmethod
    def ReadMemberNameByUid(uid: MemberUid) -> str | None:
        pass

    @abstractmethod
    def ReadMemberBioByUid(uid: MemberUid) -> str | None:
        pass

    @abstractmethod
    def ReadMemberAchievementsByUid(uid: MemberUid) -> list[AchievementUid] | None:
        pass