def convert_si_to_cgs(length_m: float = 1.0, mass_kg: float = 1.0, time_s: float = 1.0) -> str:
    return f"Lenght in CGS {round(length_m*100, 1)} cm, Mass in CGS {round(mass_kg*1000, 1)} g, Time in CGS {time_s} s."
print(convert_si_to_cgs(5, 0.02, 365))