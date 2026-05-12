from dataclasses import dataclass


@dataclass
class Confine:
   state1no: int
   state2no: int

   def get_edge(self):
      return (self.state2no, self.state1no)
