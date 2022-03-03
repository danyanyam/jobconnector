from dataclasses import dataclass, fields
from typing import Any, List as L


@dataclass
class Resume:
    _mail: str = ''
    experience: str = ''
    desirable_position: str = ''

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)


@dataclass
class ResumeHandler:
    resumes: L[Resume] = None

    def __post_init__(self):
        self.resumes = [Resume(f'dasda{i}d@mail.ru', '2 years', f'ceo_{i}') for i in range(10)]
        self._filters = self.get_filters()

    @classmethod
    def get_filters(cls):
        """ define which fileds can be used to filter resumes """
        return [i.name for i in fields(Resume) if not i.name.startswith('_')]

    def filter(self, filters) -> L[Resume]:
        valid_filters = {key: value for key, value in filters.items() if key in self._filters}

        if not valid_filters:
            return []

        return [resume for resume in self.resumes
                if all([resume[key] == value for (key, value) in valid_filters.items()])]
