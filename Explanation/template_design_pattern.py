from abc import ABC, abstractmethod

# Create Abstract Base class
class DiningExperience(ABC):
    # Skeleton of the program
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()

    # Abstract methods

    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass

    @abstractmethod
    def serve_beverage(self):
        pass

# Create concernte class that implemented the template steps
class ItalianExperience(DiningExperience):
    def serve_appetizer(self):
        print("Serve italian appetizer")

    def serve_main_course(self):
        print("Serve italian main course")

    def serve_dessert(self):
        print("Serve italian dessert")

    def serve_beverage(self):
        print("Serve italian beverage")

class MexicanExperience(DiningExperience):
    def serve_appetizer(self):
        print("Serve mexican appetizer")

    def serve_main_course(self):
        print("Serve mexican main course")

    def serve_dessert(self):
        print("Serve mexican dessert")

    def serve_beverage(self):
        print("Serve mexican beverage")

if __name__ == "__main__":
    italian_experience = ItalianExperience()
    italian_experience.serve_dinner()

    mexican_experience = MexicanExperience()
    mexican_experience.serve_dinner()