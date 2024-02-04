class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if self.language != language:
            return f"{self.name} does not know {language}"

        self.skills += skills_earned

        return f"{self.name} watched {course_name}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

        if self.language == new_language:
            return f"{self.name} already knows {new_language}"

        old_language = self.language
        self.language = new_language

        return f"{self.name} switched from {old_language} to {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to 04.10.02.03.Hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
