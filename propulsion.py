import csdl
import python_csdl_backend


# outputs the power required for a given operating condition and drivetrain/propeller efficiency

class prop(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        drag = self.declare_variable('drag')
        velocity = self.declare_variable('velocity')
        eta_p = self.declare_variable('propeller_efficiency')
        eta_d = self.declare_variable('drivetrain_efficiency')

        thrust_required = 1*drag

        total_efficiency = eta_p*eta_d

        required_power = (thrust_required*velocity)/total_efficiency

        self.register_output('required_power',required_power)


