"""
Arbeidskrav 1

Sammenligning av årlige kostnader for elbil og bensinbil

Programmet beregner og sammenligner de årlige totalkostnadene
for en elbil og en bensinbil

Kostnader som tas med er:
- Forsikring
- Trafikkforsikringsavgift
- Drivstoff/strøm
- Bomavgift

Av Kristina Oddden Krogsæther (kristinaok@live.no)

Oppdatert 2026 09 24

"""
#%% Likt på elbil og bensinbil

Km = 10000  # Antall km kjørt per år
Dager_i_år = 365
Tfa_per_dag = 8.38  # Trafikkforsikringsavgift per dag
Tfa_per_år = Dager_i_år * Tfa_per_dag  # Trafikkforsikringsavgift per år

#%% Beregning elbil

Forsikring_el = 5000  # Forsikring elbil per år
Drivstoff_el = 0.2  #Drivstoff elbil per kwh per km
Strøm = 2  # Strømpris i kr per kwh
Bom_el = 0.1  # Bomavgift elbil per km

Drivstoff_el_tot = Strøm * Drivstoff_el * Km
Bom_el_tot = Bom_el * Km

Sum_el = Forsikring_el + Drivstoff_el_tot + Bom_el_tot + Tfa_per_år  # Total årlig kostnad elbil

#%% Beregning bensinbil

Forsikring_b = 7500  # Forsikring bensinbil per år
Drivstoff_b = 1  # Drivstoff bensinbil i kr per km
Bom_b = 0.3  # Bomavgift bensinbil per km

Drivstoff_b_tot = Drivstoff_b * Km  
Bom_b_tot = Bom_b * Km

Sum_b = Forsikring_b + Drivstoff_b_tot + Bom_b_tot + Tfa_per_år  # Total årlig kostnad bensinbil


#%% Beregning kostnadsdifferansen

Kostnadsdifferanse = Sum_b - Sum_el

#%% Presentasjon av resultat

print("Sammenligning av årlige bilkostnader")
print()
print("Kjørelengde:", Km, "km per år")
print("-------------------------------------------------")
print("Elbil")
print("Forsikring:", Forsikring_el, "kr")
print("Trafikkforsikringsavgift:", Tfa_per_år, "kr")
print("Drivstoff:", Drivstoff_el_tot, "kr")
print("Bomkostnad:", Bom_el_tot, "kr")
print()
print("Totalkostnad for elbil per år:", Sum_el, "kr")
print()
print("-------------------------------------------------")
print("Bensinbil")
print("Forsikring:", Forsikring_b, "kr")
print("Trafikkforsikringsavgift:", Tfa_per_år, "kr")
print("Drivstoff:", Drivstoff_b_tot, "kr")
print("Bomkostnad:", Bom_b_tot, "kr")
print()
print("Totalkostnad for bensinbil per år:", Sum_b, "kr")
print()
print("--------------------------------------------------")
print("Årlig kostnadsdifferanse:", Kostnadsdifferanse, "kr")

