class Joseph:
    def __init__(self):
        self.communication = {}
        self.planning = {}
        self.modeling = {}
        self.construction = {}
        self.deployment = {}

    def input_communication(self):
        self.communication['project_initiation'] = input("Enter the project initiation steps: ")
        self.communication['requirement_gathering'] = input("Enter the requirement gathering steps: ")

    def input_planning(self):
        self.planning['estimating'] = input("Enter the estimating steps: ")
        self.planning['scheduling'] = input("Enter the scheduling steps: ")
        self.planning['tracking'] = input("Enter the tracking steps: ")
        self.planning['risk_management'] = input("Enter the risk management steps (potential risks and how to mitigate them): ")

    def input_modeling(self):
        self.modeling['analysis'] = input("Enter the analysis steps: ")
        self.modeling['design'] = input("Enter the design steps: ")
        self.modeling['early_testing'] = input("Enter the steps for early testing to validate the design: ")

    def input_construction(self):
        self.construction['code'] = input("Enter the coding steps: ")
        self.construction['ongoing_testing'] = input("Enter the steps for ongoing testing during construction: ")
        self.construction['peer_validation'] = input("Enter the peer validation steps: ")

    def input_deployment(self):
        self.deployment['delivery'] = input("Enter the delivery steps: ")
        self.deployment['support'] = input("Enter the support steps: ")
        self.deployment['feedback'] = input("Enter the feedback steps: ")

    def display_model(self):
        print("\nSample Model Breakdown:")
        print("Communication:", self.communication)
        print("Planning:", self.planning)
        print("Modeling:", self.modeling)
        print("Construction:", self.construction)
        print("Deployment:", self.deployment)

    def run_model(self):
        self.input_communication()
        self.input_planning()
        self.input_modeling()
        self.input_construction()
        self.input_deployment()

        self.display_model()


if __name__ == "__main__":
    model = Joseph()
    model.run_model()
