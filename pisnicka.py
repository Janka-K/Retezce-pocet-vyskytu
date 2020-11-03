#Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce a zjisti, kolikrát je v něm použito písmeno K.

pisnicka = """Nikde žádnej sníh
Všude spousta slev
Po kostkách dlažebních
Stéká kapří krev
Ve švech praská máj
A úsměv na tváři
V těchhle svátečních dnech maj
Snad jen lichváři
Ač vánoce dávno nejsou o lásce
Spíš je to deal, co fakt dobře prodává se
Ač dávno nejsou o klidu a míru
Spíš o obžerství stresu a balicím papíru
Ač každej rok slýchám ze všech repráků
Ten samej výběr tupejch vánočních fláků
Ač jsou vánoce kýč jak verše z jejich slok
Tak je to kýč, na kterej se těším celej rok
Panna Maria
Dala život děťátku
Proto jsme teď ty i já
Ve frontě v Palládku
Ježíšek už tmou
Jen v plenkách uhání
Snad ho v parku nezatknou
Za veřejné obnažování
Ač vánoce dávno nejsou o lásce
Spíš je to deal, co fakt dobře prodává se
Ač dávno nejsou o klidu a míru
Spíš o obžerství stresu a balicím papíru
Ač každej rok slýchám ze všech repráků
Ten samej výběr tupejch vánočních fláků
Ač jsou vánoce kýč jak verše z jejich slok
Tak je to kýč, na kterej se těším celej rok"""

pocet = 0

for pismeno in pisnicka.upper():
  if pismeno == "K":
    pocet +=1
print(f"Pocet pismen 'K' v pisni Nikde zadnej snih je {pocet}")

