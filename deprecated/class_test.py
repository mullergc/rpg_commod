class Government :
  def __init__(self, resources) :
    self.resources = resources

  def distribute_resources(self, amount) :
    self.resources -= amount
    return amount


class Hospital :
  def __init__(self, compartments) :
    self.compartments = compartments
    self.resources = [0 for _ in compartments]

  def receive_resources(self, amount) :
    for i in range(len(self.resources)) :
      self.resources[i] += amount // len(self.resources)

    return self.resources


class Media :
  def __init__(self) :
    self.opinion = 0

  def change_opinion(self, amount) :
    self.opinion += amount
