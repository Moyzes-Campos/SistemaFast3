from django.db import models


areas = (
    ('Aerodinâmica', 'Aerodinâmica'),
    ('Direção', 'Direção e Suspenção'),
    ('Elétrica', 'Elétrica'),
    ('Estrutura', 'Estrutura'),
    ('Freio e Ergonomia', 'Freio e Ergonomia'),
    ('Powewtrain', 'Powewtrain'),
    ('Comercial', 'Comercial'),
    ('Financeiro', 'Financeiro'),
    ('Gestão', 'Gestão de Pessoas'),
    ('Marketing', 'Marketing'),
    ('NA', 'Nenhuma'),
)


class Regulamento(models.Model):

    T1_choices = (
        ('GR - General Regulations', 'GR - General Regulations'),
        ('AD - Administrative Regulations', 'AD - Administrative Regulations'),
        ('DR - Document Requirements', 'DR - Document Requirements'),
        ('V - Vehicle Requirements', 'V - Vehicle Requirements'),
        ('F - Chassis and Structural ', 'F - Chassis and Structural'),
        ('T - Technical Aspects ', 'T - Technical Aspects'),
        ('VE - Vehicle and Driver Equipament', 'VE - Vehicle and Driver Equipament'),
        ('IC - Internal Combustion Engine Vehicles', 'IC - Internal Combustion Engine Vehicles'),
        ('IN - Technical Inspection', 'IN - Technical Inspection'),
        ('S - Static Events', 'S - Static Events'),
        ('D - Dynamic Events', 'D - Dynamic Events'),
    )
    T2_choices = (
        ('GR.1 - Formula SAE Competition Objective', 'GR.1 - Formula SAE Competition Objective'),
        ('GR.2 Formula SAE Rules and Organizer Authority', 'GR.2 Formula SAE Rules and Organizer Authority'),
        ('GR.3 Rules of Conduct', 'GR.3 Rules of Conduct'),
        ('GR.4 Rules format and Use', 'GR.4 Rules format and Use'),
        ('GR.5 Rules question', 'GR.5 Rules question'),
        ('GR.6 Protests', 'GR.6 Protests'),
        ('GR.7 Vehicle Elegibility', 'GR.7 Vehicle Elegibilty'),
        ('AD.1 The Formula SAE Series', 'AD.1 The Formula SAE Series'),
        ('AD.2 Official Information Sources', 'AD.2 Official Information Sources'),
        ('AD.3 Individual Participation Requirements', 'AD.3 Individual Participation Requirements'),
        ('AD.4 Individual Registration Requirements', 'AD.4 Individual Registration Requirements'),
        ('AD.5 Team Advisors and Officers', 'AD.5 Team Advisors and Officers'),
        ('AD.6 Competition Registration', 'AD.6 Competition Registration'),
        ('AD.7 Competition Site', 'AD.7 Competition Site'),
        ('DR.1 Documentation', 'DR.1 Documentation'),
        ('DR.2 Submission Details', 'DR.2 Submission Details'),
        ('DR.3 Submission Penalties', 'DR.3 Submission Penalties'),
        ('V.1 Configuration', 'V.1 Configuration'),
        ('V.2 Driver', 'V.2 Driver'),
        ('V.3 Suspension and Steering', 'V.3 Suspension and Steering'),
        ('V.4 Wheels and Tires', 'V.4 Wheels and Tires'),
        ('F.1 Definitions', 'F.1 Definitions'),
        ('F.2 Documentation', 'F.2 Documentation'),
        ('F.3 Tubing and Material', 'F.3 Tubing and Material'),
        ('F.4 Composite and Other Materials', 'F.4 Composite and Other Materials'),
        ('F.5 Chassis Requirements', 'F.5 5 Chassis Requirements'),
        ('F.6 Tube Frames', 'F.6 Tube Frames'),
        ('F.7 Monocoque', 'F.7 Monocoque'),
        ('F.8 Front Chassis Protection', 'F.8 Front Chassis Protection'),
        ('F.9 Fuel System', 'F.9 Fuel System'),
        ('T.1 Cockpit', 'T.1 Cockpit'),
        ('T.2 Driver Acomodation', 'T.2 Driver Acomodation'),
        ('T.3 Brake System', 'T.3 Brake System'),
        ('T.4 Eletronic Throttle Components', 'T.4 Eletronic Throttle Components'),
        ('T.5 Powertrain', 'T.5 Powertrain'),
        ('T.6 Pressurized Systems', 'T.6 Pressurized Systems'),
        ('T.7 Bodywork and Aerodynamic Devices', 'T.7 Bodywork and Aerodynamic Devices'),
        ('T.8 Fasteners', 'T.8 Fasteners'),
        ('T.9 Eletrical Equipament', 'T.9 Eletrical Equipament'),
        ('VE.1 Vehicle Indentification', 'VE.1 Vehicle Indetification'),
        ('VE.2 Vehicle Equipament', 'VE.2 Vehicle Equipament'),
        ('VE.3 Driver Equipament', 'VE.3 Driver Equipament'),
        ('IC.1 General Requirements', 'IC.1 General Requirements'),
        ('IC.2 Air Intake System', 'IC.2 Air Intake System'),
        ('IC.3 Throttle', 'IC.3 Throttle'),
        ('IC.4 Eletronic Throttle Control', 'IC.4 Eletronic Throttle Control'),
        ('IC.5 Fuel and Fuel System', 'IC.5 Fuel and Fuel System'),
        ('IC.6 Fuel Injection', 'IC.6 Fuel Injection'),
        ('IC.7 Exhaust and Noise Control', 'IC.7 Exhaust and Noise Control'),
        ('IC.8 Eletrical', 'IC.8 Eletrical'),
        ('IC.9 Shutdown System', 'IC.9 Shutdown System'),
        ('IN.1 Inspection Requirements', 'IN.1 Inspection Requirements'),
        ('IN.2 Inspecition Conduct', 'IN.2 Inspecition Conduct'),
        ('IN.3 Initial Inspection', 'IN.3 Initial Inspection'),
        ('IN.4 Eletrical Technical Inspection', 'IN.4 Eletrical Technical Inspection'),
        ('IN.5 Driver Cockpit Checks', 'IN.5 Driver Cockpit Checks'),
        ('IN.6 Driver Template Inspections', 'IN.6 Driver Template Inspections'),
        ('IN.7 Cockpit Template Inspecions', 'IN.7 Cockpit Template Inspecions'),
        ('IN.8 Mechanical Technical Inspection', 'IN.8 Mechanical Technical Inspection'),
        ('IN.9 Tilt Test', 'IN.9 Tilt Test'),
        ('IN.10 Noise and Switch Test', 'IN.10 Noise and Switch Test'),
        ('IN.11 Rain Test', 'IN.11 Rain Test'),
        ('IN.12 Brake Test', 'IN.12 Brake Test'),
        ('IN.13 Inspection Approval', 'IN.13 Inspection Approval'),
        ('IN.14 Modifications and Repairs', 'IN.14 Modifications and Repairs'),
        ('IN.15 Reinspection', 'IN.15 Reinspection'),
        ('S.1 General Static', 'S.1 General Static'),
        ('S.2 Presentation Event', 'S.2 Presentation Event'),
        ('S.3 Cost and Manufacturing Event', 'S.3 Cost and Manufacturing Event'),
        ('S.4 Design Event', 'S.4 Design Event'),
        ('D.1 General Dynamic', 'D.1 General Dynamic'),
        ('D.2 Pit and Paddock', 'D.2 Pit and Paddock'),
        ('D.3 Driving', 'D.3 Driving'),
        ('D.4 Flags', 'D.4 Flags'),
        ('D.5 Weather Conditions', 'D.5 Weather Conditions'),
        ('D.6 Tires and Tire Changes', 'D.6 Tires and Tire Changes'),
        ('D.7 Driver Limitations', 'D.7 Driver Limitations'),
        ('D.8 Definitions', 'D.8 Definitions'),
        ('D.9 Acceleration Event', 'D.9 Acceleration Event'),
        ('D.10 Skidpad Event', 'D.10 Skidpad Event'),
        ('D.11 Autocross Event', 'D.11 Autocross Event'),
        ('D.12 Endurance Event', 'D.12 Endurance Event'),
        ('D.13 Efficiency Event', 'D.13 Efficiency Event'),
        ('D.14 Post Endurance', 'D.14 Post Endurance'),
    )

    t1 = models.CharField('Título 1', max_length=50, choices=T1_choices)
    t2 = models.CharField('Título 2', max_length=50, choices=T2_choices)
    t3 = models.CharField('Título 3', max_length=100, default='Default')
    resumo = models.TextField(help_text='Escreva o resumo')
    area = models.CharField(max_length=100, choices=areas)

    class Meta:
        verbose_name = 'Regulamento'
        verbose_name_plural = 'Regulamento'

    def __str__(self):
        return self.t3
