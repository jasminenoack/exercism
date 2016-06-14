class Allergies:
    allergies = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self,score):
        score %= 2**len(Allergies.allergies)
        self.list = []
        for num in range(len(Allergies.allergies))[::-1]:
            if score >= 2 ** num:
                self.list.append(Allergies.allergies[num])
                score -= 2 ** num
        self.list = self.list[::-1]


    def is_allergic_to(self, item):
        return item in self.list