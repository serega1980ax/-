class Element:

    def agg_state(self, t, transfer):
        if transfer == 'f':
            t = Iron.convert_to_c(self, t)
        elif transfer == 'k':
            t = Iron.convert_to_k(self, t)
        if t <= self.t_solid:
            return('solid_state')
        elif t > self.t_solid and t <= self.t_gas:
            return('liquid')
        else:
            return('gas')
       
    def convert_to_c(self, t):
        return(t - 32) * 5/9   
    def convert_to_k(self, t):
        return 273.15 + t       
class Iron(Element):
    t_solid = 1538
    t_gas = 2862
           
t = Iron()

print(t.agg_state(2500, 'f'))