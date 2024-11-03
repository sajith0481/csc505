class DeveloperTrait:
    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps

    def display_info(self):
        print(f"Trait: {self.name}")
        print(f"Description: {self.description}")
        print(f"Number of Important Steps: {len(self.steps)}")
        print("Important Steps:")
        for step in self.steps:
            print(f"- {step}")
        print("\n")


class DeveloperTraitBuilder:
    def __init__(self):
        self.trait = None

    def create_trait(self, name, description):
        self.trait = DeveloperTrait(name, description, [])

    def add_step(self, step):
        if self.trait is not None:
            self.trait.steps.append(step)

    def get_trait(self):
        return self.trait


def main():
    builder = DeveloperTraitBuilder()

    # Problem Solver Trait
    builder.create_trait(
        "Problem Solver",
        "Analytical and creative, capable of solving complex problems."
    )
    builder.add_step("Analyze the problem")
    builder.add_step("Develop potential solutions")
    builder.add_step("Implement the best solution")
    builder.add_step("Evaluate the outcome")
    problem_solver = builder.get_trait()

    # Team Player Trait
    builder.create_trait(
        "Team Player",
        "Communicative and collaborative, essential for effective teamwork."
    )
    builder.add_step("Communicate effectively with team members")
    builder.add_step("Share knowledge and resources")
    builder.add_step("Collaborate on tasks and projects")
    builder.add_step("Provide and receive constructive feedback")
    team_player = builder.get_trait()

    # Continuous Learner Trait
    builder.create_trait(
        "Continuous Learner",
        "Curious and adaptable, always eager to learn new technologies and adapt to changes."
    )
    builder.add_step("Stay updated with industry trends")
    builder.add_step("Learn new programming languages and tools")
    builder.add_step("Adapt to new methodologies and practices")
    builder.add_step("Seek feedback for improvement")
    continuous_learner = builder.get_trait()

    # Display information
    for trait in [problem_solver, team_player, continuous_learner]:
        trait.display_info()


if __name__ == "__main__":
    main()
